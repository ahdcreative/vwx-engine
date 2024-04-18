import json
import re
from pathlib import Path
import httpx

DN_URL = "https://en.wikipedia.org/wiki/List_of_ICAO_aircraft_type_designators"
OUT_PATH = Path(__file__).parent / "files" / "aircraft.json"
TAG = re.compile(r"<[^>]*>")


def main() -> int:
    """ Build or update aircraft.json file """
    resp = httpx.get(DN_URL)
    if resp.status_code != 200:
        return 1
    text = resp.text
    text = text[text.find("<caption>ICAO"):]
    rows = text[: text.find("</table>")].split("<tr>")[2:]
    craft = {}
    for row in rows:
        cols = row.split("\n")
        name = TAG.sub("", cols[3]).strip()
        if "deprecated" in name:
            continue
        code = TAG.sub("", cols[1]).strip()
        if code not in craft:
            craft[code] = name

    json.dump(craft, OUT_PATH.open("w", encoding="utf8"))
    return 0


if __name__ == "__main__":
    main()
