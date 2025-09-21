__author__ = "Pinkas Matěj - pinka"
__maintainer__ = "Pinkas Matěj - pinka"
__email__ = "pinkas.matej@gmail.com"
__credits__ = []
__created__ = "20/09/2025"
__date__ = "20/09/2025"
__status__ = "Prototype"
__version__ = "0.1.0"
__copyright__ = ""
__license__ = ""

"""
Project: Health_scanner
Filename: main.py
Directory: /
"""


import xml.etree.ElementTree as ET

# Načtení souboru
tree = ET.parse("apple_health_export/export.xml")
root = tree.getroot()

# Prohlédnutí základní struktury
print(root.tag, root.attrib)

# Procházíme záznamy
for record in root.findall("Record"):
    record_type = record.get("type")
    start_date = record.get("startDate")
    end_date = record.get("endDate")
    value = record.get("value")

    print(record_type, start_date, end_date, value)

if __name__ == '__main__':
    pass
