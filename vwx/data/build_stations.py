"""
Builds the main station list

Source file for airports.csv and runways.csv can be downloaded from
http://ourairports.com/data/

Source file for stations.txt can be downloaded from
https://www.aviationweather.gov/docs/metar/stations.txt
"""

import csv
import json
import logging
from contextlib import suppress
from datetime import date
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple
import httpx
from vwx.data.mappers import FILE_REPLACE, SURFACE_TYPES

LOG = logging.getLogger("vwx.data.build_stations")


def load_stations(path: Path) -> Iterable[str]:
    """ Loads a station set from a path """
    return set(path.read_text().strip().split("\n"))


_FILE_DIR = Path(__file__).parent
_DATA = _FILE_DIR / "files"
GOOD_PATH = _DATA / "good_stations.txt"
OUT = _DATA / "stations.json"

DATA_ROOT = "https://davidmegginson.github.io/ourairports-data/"
