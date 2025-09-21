__author__ = "Pinkas Matěj - pinka"
__maintainer__ = "Pinkas Matěj - pinka"
__email__ = "pinkas.matej@gmail.com"
__credits__ = []
__created__ = "21/09/2025"
__date__ = "21/09/2025"
__status__ = "Prototype"
__version__ = "0.1.0"
__copyright__ = ""
__license__ = ""

"""
Project: Health_scanner
Filename: panda.py
Directory: /
"""

import xml.etree.ElementTree as ET
import csv
from datetime import datetime

# Načti XML
tree = ET.parse("apple_health_export_new/export.xml")
root = tree.getroot()

with open("heart_rate.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    # Hlavička
    writer.writerow(["date", "time", "bpm"])

    for record in root.findall("Record"):
        if record.get("type") == "HKQuantityTypeIdentifierHeartRate":
            dt = record.get("startDate")
            # Převod na datetime (ignoruje časové pásmo)
            dt_obj = datetime.fromisoformat(dt.replace("Z", "+00:00"))
            date_str = dt_obj.strftime("%Y-%m-%d")
            time_str = dt_obj.strftime("%H:%M:%S")
            bpm = record.get("value")

            writer.writerow([date_str, time_str, bpm])

print("Hotovo! Data jsou v heart_rate.csv")

if __name__ == '__main__':
    pass
