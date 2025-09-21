import csv
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Tmavý režim
plt.style.use('dark_background')

timestamps = []
bpm_values = []

# Načti CSV
with open("heart_rate.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        dt_str = f"{row['date']} {row['time']}"
        dt_obj = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
        timestamps.append(dt_obj)
        bpm_values.append(float(row['bpm']))

if not timestamps:
    print("⚠️ CSV neobsahuje žádná data!")
else:
    plt.figure(figsize=(30, 5))

    # Spojnice s kulatými body
    plt.plot(
        timestamps,
        bpm_values,
        linestyle=' ',
        marker='.',
        markersize=1,
        color='red',
        alpha=0.7
    )

    # Osa X: automaticky podle dat
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
    plt.xticks(rotation=45, color='white')
    plt.yticks(color='white')

    plt.title("Srdeční tep - všechna data", color='white')
    plt.xlabel("Datum a čas", color='white')
    plt.ylabel("Tep [bpm]", color='white')
    plt.grid(True, color='gray', alpha=0.5)
    plt.tight_layout()

    plt.savefig("heart_rate_all_data.png", dpi=1000)
    plt.show()
    print("Graf uložen do heart_rate_all_data.png")
