import sqlite3
import os
import pandas as pd
from datetime import datetime
import numpy as np

#Create the data
data = pd.DataFrame(list(range(1,101)) * 10)
data.columns = ["ID"]
l = []
for date in pd.date_range(datetime(2019,1,1), datetime(2019,1,10)):
    l.extend([date] * 100)
data['Date'] = l
data['Sector'] = ["Healthcare", "Financials", "Energy", "Consumer Staples", "Consumer Discretionary"] * 200
np.random.seed(1)
data['Return'] = np.random.normal(0,.01,1000)
print(data.head(5))

conn = sqlite3.connect('Stock.db')
#Set index to false
data.to_sql("Returns", conn, index=False)

query = "SELECT AVG(Return) FROM Returns"
df = pd.read_sql(query, conn)
print(df)