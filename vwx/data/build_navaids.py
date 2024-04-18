import json
from pathlib import Path
from typing import Tuple, Dict, Set
import httpx

# redirect https://ourairports.com/data/navaids.csv
SOURCE = "https://davidmegginson.github.io/ourairports-data/navaids.csv"
OUT = Path(__file__).parent / "files" / "navaids.json"


def main() -> None:
    """ Build the navaids """
    text = httpx.get(SOURCE).text
    lines = text.strip().split("\n")
    lines.pop(0)
    data: Dict[str, Set[Tuple[float, float]]] = {}
    for line_str in lines:
        line = line_str.split(",")
        try:
            ident, lat, lon = line[2].strip('"'), float(line[6]), float(line[7])
        except ValueError:
            continue

        if not ident:
            continue

        try:
            data[ident].add((lat, lon))
        except KeyError:
            data[ident] = {(lat, lon)}

    output = {k: list(v) for k, v in data.items()}
    json.dump(output, OUT.open("w"), sort_keys=True)


if __name__ == "__main__":
    main()
