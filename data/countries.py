"""Backward-compatibility proxy for gamedata.countries."""
from gamedata.countries import *  # noqa: F401, F403
from gamedata.countries import COUNTRIES, COUNTRIES_BY_CODE, get_country, search_country_by_name  # noqa: F401
