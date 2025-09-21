import csv
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

timestamps = []
bpm_values = []

#plt.style.use('dark_background')

# Načti CSV
with open("heart_rate.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        dt_str = f"{row['date']} {row['time']}"
        dt_obj = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
        timestamps.append(dt_obj)
        bpm_values.append(float(row['bpm']))

# Filtr posledního dne
cutoff = datetime.now() - timedelta(days=5)
timestamps_filtered = []
bpm_filtered = []
for t, v in zip(timestamps, bpm_values):
    if t >= cutoff:
        timestamps_filtered.append(t)
        bpm_filtered.append(v)

if not timestamps_filtered:
    print("⚠️ V posledním dni nejsou žádné záznamy!")
else:
    plt.figure(figsize=(22, 5))

    # Vykresli body tepu podle času
    plt.plot(timestamps_filtered, bpm_filtered, marker=".", linestyle=" ", alpha=0.7, color='red')

    # Nastav osy X rovnoměrně po hodinách
    plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=1))  # každou hodinu
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))  # zobrazení HH:MM
    plt.xlim([datetime.now() - timedelta(days=5), datetime.now()])  # posledních 24h

    plt.title("Srdeční tep - poslední den")
    plt.xlabel("Čas")
    plt.ylabel("Tep [bpm]")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("heart_rate_plot.png", dpi=150)
    plt.show()
    print("Graf uložen do heart_rate_plot.png")
