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
Filename: plotter.py
Directory: utils/
"""

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def plot_time_data(x:list=None, y:list=None):
    plt.figure(figsize=(22, 5))
    plt.scatter(x, y, color='blue')
    plt.plot(x,y, color='red', linestyle='--', marker=' ')

    y_average = 0
    for item in zip(x,y):
        print(item)
        y_average += item[1]

    y_average /= len(y)
    print('average', y_average)
    plt.plot([x[0], x[-1]], [y_average, y_average], color='green', linestyle='--')
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=2))
    plt.xticks(rotation=45)
    plt.show()

if __name__ == '__main__':
    pass
