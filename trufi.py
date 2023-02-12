import pandas as pd
data = pd.read_csv("trufi.csv")
#print(data)
semana6 = data[data["week"] == 6]
#print(semana6)
filtro = semana6[["Net Income"]]
print(filtro)
print(filtro.sum())
