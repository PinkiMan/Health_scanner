__author__ = "Pinkas Matěj - Pinki"
__maintainer__ = "Pinkas Matěj - Pinki"
__email__ = "pinkas.matej@gmail.com"
__credits__ = []
__created__ = "25/09/2025"
__date__ = "25/09/2025"
__status__ = "Prototype"
__version__ = "0.1.0"
__copyright__ = ""
__license__ = ""

"""
Project: Health_scanner
Filename: exporter.py
Directory: utils/
"""

from datetime import datetime
import xml.etree.ElementTree as ElementTree

class Exporter:
    def __init__(self, filename):
        self.filename = filename
        self.tree = ElementTree.parse(self.filename)
        self.root = self.tree.getroot()

    def get_hearth_rate_records(self):
        for record in self.root.findall("Record"):
            if record.get("type") == "HKQuantityTypeIdentifierHeartRate":
                pass

    def get_all_tags(self):
        tags = set()
        for elem in self.root.iter():
            tags.add(elem.tag)
        return tags

    def get_all_types(self, tag):
        types = set()
        for item in self.root.findall(tag):
            types.add(item.get('type'))

        return list(types)

    def get_type(self, item_tag, item_type):
        item_list = []
        for item in self.root.findall(item_tag):
            if item.get('type') == item_type:
                item_list.append(item)

        return item_list

    def get_temperature(self):
        temperature_list = self.get_type('Record', 'HKQuantityTypeIdentifierAppleSleepingWristTemperature')
        data_list=[]
        for temperature in temperature_list:
            start_date = temperature.attrib['startDate']
            end_date = temperature.attrib['endDate']
            value = temperature.attrib['value']
            start_datetime = datetime.fromisoformat(start_date).strftime('%d.%m.%Y %H:%M:%S')
            end_datetime = datetime.fromisoformat(end_date).strftime('%d.%m.%Y %H:%M:%S')
            data = {'start_datetime':start_datetime, 'end_datetime':end_datetime, 'value':value}
            data_list.append(data)
        return data_list

if __name__ == '__main__':
    ah = Exporter('../data/export.xml')
    datas = ah.get_temperature()

    from utils.plotter import plot_time_data
    x_list = []
    y_list = []
    for item in datas:
        x_list.append(item['start_datetime'])
        y_list.append(float(item['value']))
    #plot_time_data(x_list[-60:],y_list[-60:])
    plot_time_data(x_list, y_list)
    #35,2873
    #print(ah.get_type('Record', 'HKQuantityTypeIdentifierAppleSleepingWristTemperature'))
