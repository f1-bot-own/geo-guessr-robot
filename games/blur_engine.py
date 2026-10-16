"""
Blur and Zoom-In Reveal Image Processing Engine for GeoGuru & GeoGuessr.
Provides 3-stage progressive unblur processing for flags, landmarks, and streetviews.
"""

import io
import logging
from typing import Tuple, Optional, Dict
import aiohttp
from PIL import Image, ImageFilter

logger = logging.getLogger(__name__)

# In-memory cache for processed blur stages (image_url -> (stage1_bytes, stage2_bytes, stage3_bytes))
BLUR_STAGES_CACHE: Dict[str, Tuple[bytes, bytes, bytes]] = {}

# Raw image bytes cache
RAW_IMAGE_CACHE: Dict[str, bytes] = {}


def process_image_to_stages(image_bytes: bytes) -> Tuple[bytes, bytes, bytes]:
    """
    Process raw image bytes into 3 progressive reveal stages:
    Stage 1: Heavy Gaussian blur (radius=22) + center zoom (1.15x)
    Stage 2: Medium Gaussian blur (radius=8) + subtle zoom (1.05x)
    Stage 3: Crystal clear image (radius=0, zoom=1.0x)
    """
    orig = Image.open(io.BytesIO(image_bytes))

    # Convert transparent PNG or palette to solid RGB on white background
    if orig.mode in ("RGBA", "LA") or (orig.mode == "P" and "transparency" in orig.info):
        alpha = orig.convert("RGBA")
        bg = Image.new("RGBA", alpha.size, (255, 255, 255, 255))
        bg.paste(alpha, mask=alpha)
        base_img = bg.convert("RGB")
    else:
        base_img = orig.convert("RGB")

    w, h = base_img.size

    def _render_stage(blur_radius: int, zoom_factor: float) -> bytes:
        img = base_img.copy()
        if zoom_factor > 1.0:
            crop_w = int(w / zoom_factor)
            crop_h = int(h / zoom_factor)
            left = (w - crop_w) // 2
            top = (h - crop_h) // 2
            img = img.crop((left, top, left + crop_w, top + crop_h))
            img = img.resize((w, h), Image.Resampling.LANCZOS)
        if blur_radius > 0:
            img = img.filter(ImageFilter.GaussianBlur(radius=blur_radius))
        out = io.BytesIO()
        img.save(out, format="JPEG", quality=85)
        return out.getvalue()

    stage1 = _render_stage(blur_radius=22, zoom_factor=1.15)
    stage2 = _render_stage(blur_radius=8, zoom_factor=1.05)
    stage3 = _render_stage(blur_radius=0, zoom_factor=1.0)

    return (stage1, stage2, stage3)


async def get_blur_stages(image_url: str) -> Optional[Tuple[bytes, bytes, bytes]]:
    """
    Fetch and return (stage1, stage2, stage3) image bytes for a given image URL.
    Uses in-memory cache for instantaneous repeated accesses.
    """
    if not image_url or not isinstance(image_url, str):
        return None

    if image_url in BLUR_STAGES_CACHE:
        return BLUR_STAGES_CACHE[image_url]

    # Check raw cache or fetch
    raw_bytes = RAW_IMAGE_CACHE.get(image_url)
    if not raw_bytes:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36 GeoGuruBot/2.0"
            ),
            "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8"
        }
        try:
            timeout = aiohttp.ClientTimeout(total=8, connect=4)
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.get(image_url, headers=headers) as resp:
                    if resp.status == 200:
                        raw_bytes = await resp.read()
                        RAW_IMAGE_CACHE[image_url] = raw_bytes
                    else:
                        logger.warning(f"Failed to fetch image for blur: {image_url} (HTTP {resp.status})")
                        return None
        except Exception as e:
            logger.warning(f"Exception downloading image for blur {image_url}: {e}")
            return None

    try:
        stages = process_image_to_stages(raw_bytes)
        BLUR_STAGES_CACHE[image_url] = stages
        return stages
    except Exception as e:
        logger.error(f"Error processing blur stages for {image_url}: {e}")
        return None
