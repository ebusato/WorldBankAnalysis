import wbdata
import matplotlib.pyplot as plt
import pandas as pd

sources = wbdata.get_source()
print(sources)
print(wbdata.get_indicator(source=25))
indicators = {"EN.POP.DNST": "Population density", "SP.URB.TOTL.IN.ZS": "Urban population (%)", "SP.RUR.TOTL.ZS": "Rural population (%)"}
#indicators = {"EN.POP.DNST": "Population density"}
#data = wbdata.get_dataframe(indicators, country="USA")
data = wbdata.get_dataframe(indicators, country="FR")
print(type(data))
print(data.head(100))

data.index = pd.to_datetime(data.index)

data[["Urban population (%)", "Rural population (%)"]].plot()

#print(data.index)

#fig, ax = plt.subplots()
#data.plot(x=data.index, ax=ax)

#indicators = {"NY.GDP.PCAP.PP.KD": "toto"}
#df = wbdata.get_dataframe(indicators, country="USA")
#df.info(verbose=True)
#print(df.index)

#df.plot()

plt.show()