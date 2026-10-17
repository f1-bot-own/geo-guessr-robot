# -*- coding: utf-8 -*-
"""
Generate complete Part 4: Blitz (zakovat_376 to zakovat_500) - 125 questions.
"""
import os
import json
import sys

from gen_blitz_chunk1 import CHUNK_1
from gen_blitz_chunk2 import CHUNK_2

all_items = CHUNK_1 + CHUNK_2
print(f"Total raw items loaded for Blitz: {len(all_items)}")
assert len(all_items) == 125, f"Expected 125 items, got {len(all_items)}"

questions = []
for idx, item in enumerate(all_items):
    q_id = f"zakovat_{376 + idx}"
    (c_uz, c_ru, c_en,
     d_uz, d_ru, d_en,
     q_uz, q_ru, q_en,
     fact_uz, fact_ru, fact_en,
     aliases) = item

    correct_idx = idx % 4

    opts_uz = list(d_uz)
    opts_uz.insert(correct_idx, c_uz)

    opts_ru = list(d_ru)
    opts_ru.insert(correct_idx, c_ru)

    opts_en = list(d_en)
    opts_en.insert(correct_idx, c_en)

    assert len(opts_uz) == 4, f"{q_id} uz options != 4"
    assert len(opts_ru) == 4, f"{q_id} ru options != 4"
    assert len(opts_en) == 4, f"{q_id} en options != 4"
    assert opts_uz[correct_idx] == c_uz
    assert opts_ru[correct_idx] == c_ru
    assert opts_en[correct_idx] == c_en

    q_dict = {
        "id": q_id,
        "type": "blitz",
        "question": {
            "uz": q_uz,
            "ru": q_ru,
            "en": q_en
        },
        "options": {
            "uz": opts_uz,
            "ru": opts_ru,
            "en": opts_en
        },
        "correct_index": correct_idx,
        "correct_answer": {
            "uz": c_uz,
            "ru": c_ru,
            "en": c_en
        },
        "image_url": None,
        "fun_fact": {
            "uz": fact_uz,
            "ru": fact_ru,
            "en": fact_en
        },
        "aliases": aliases
    }
    questions.append(q_dict)

print(f"Generated {len(questions)} Blitz questions.")

out_path = os.path.join(os.path.dirname(__file__), "part4_blitz.py")
with open(out_path, "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""\nPart 4: Blitz Questions (zakovat_376 to zakovat_500) - 125 questions\n"""\n\n')
    json_str = json.dumps(questions, ensure_ascii=False, indent=2)
    py_content = json_str.replace(': null', ': None')
    f.write(f"BLITZ_QUESTIONS = {py_content}\n")

print(f"Saved to {out_path}")
