import numpy as np
import pandas as pd

date = inputs['Date']
time = inputs['Time']
moisture = inputs['Moisture']

last_of_date = date[-1]
second_of_date = date[-2]
third_of_date = date[-3]
fourth_of_date = date[-4]
fifth_of_date = date[-5]

last_of_time = time[-1]
second_of_time = time[-2]
third_of_time = time[-3]
fourth_of_time = time[-4]
fifth_of_time = time[-5]

last_of_moisture = moisture[-1]
second_of_moisture = moisture[-2]
third_of_moisture = moisture[-3]
fourth_of_moisture = moisture[-4]
fifth_of_moisture = moisture[-5]


moisture = np.array(moisture, dtype=np.float32)

data = {'Date':date, 'Time':time, 'Moisture':moisture}
df = pd.DataFrame(data)
print (df)
latest_moisture_level = moisture[-1]
print(latest_moisture_level)

outputs['latest_moisture_level'] = latest_moisture_level
outputs['last_of_date'] = last_of_date
outputs['second_of_date'] = second_of_date
outputs['third_of_date'] = third_of_date
outputs['fourth_of_date'] = fourth_of_date
outputs['fifth_of_date'] = fifth_of_date

outputs['last_of_time'] = last_of_time
outputs['second_of_time'] = second_of_time
outputs['third_of_time'] = third_of_time
outputs['fourth_of_time'] = fourth_of_time
outputs['fifth_of_time'] = fifth_of_time

outputs['last_of_moisture'] = last_of_moisture
outputs['second_of_moisture'] = second_of_moisture
outputs['third_of_moisture'] = third_of_moisture
outputs['fourth_of_moisture'] = fourth_of_moisture
outputs['fifth_of_moisture'] = fifth_of_moisture
