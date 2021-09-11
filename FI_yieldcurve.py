import datetime
import pandas_datareader as pdr
import matplotlib.pyplot as plt

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2017, 1, 1)
bondYields = pdr.fred.FredReader(["TB3MS","TB6MS","TB1YR","GS5","GS10","GS30"], start, end).read()
plt.plot([.25,.5,1,5,10,30],bondYields.iloc[0,:])
plt.plot([.25,.5,1,5,10,30],bondYields.iloc[-1,:])
plt.title("Yield Curve")
plt.xlabel("Maturity")
plt.ylabel("Yield")
plt.legend(["2010","2017"])
plt.show()

