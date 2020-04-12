import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

day = inputs['Date']
time = inputs['Time']
moisture = inputs['Moisture']

moisture = np.array(moisture, dtype=np.float32)

data = {"Date":day, "Time":time, "Moisture":moisture}
df = pd.DataFrame(data)

print(day[0])

plt.style.use("seaborn")

times = pd.to_datetime(pd.Series(time))

plt.title("Moisure Throughout the Day")
plt.xlabel("Time")
plt.ylabel("Moisture")
plt.plot_date(times, moisture, linestyle='solid')

date_format = mpl_dates.DateFormatter("%d, %b, %Y")

plt.tight_layout()
plt.show()