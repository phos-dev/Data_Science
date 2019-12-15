import matplotlib.pyplot as plt
import pandas as pd

file = pd.read_csv("/home/phos/Desktop/time-series-pam/a2_MANCHAS.csv")
x = list(file["Ano"])
y = list(file["manchas"])
plt.plot(x, y)
plt.savefig("total.png")