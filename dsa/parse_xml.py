import json
from pathlib import Path
import xml.etree.ElementTree as et

def xml_to_json():
    xml_file = Path("../data/raw/modified_sms_v2.xml")
    json_file = Path("../data/processed/modified_sms_v2.json")
    tree = et.parse(xml_file)
    root = tree.getroot()

    sms_records = []

    for sms in root.findall("sms"):
        sms_records.append(sms.attrib)

    if json_file:
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(sms_records, f, indent=4, ensure_ascii=False)
    
    return sms_records

if __name__ == "__main__":
    xml_to_json()