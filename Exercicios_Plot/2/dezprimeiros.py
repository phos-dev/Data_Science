import matplotlib.pyplot as plt
import pandas as pd

file = pd.read_csv("/home/phos/Desktop/time-series-pam/a2_MANCHAS.csv")
x = list(file["Ano"])[:10]
y = list(file["manchas"])[:10]
plt.plot(x, y)
plt.savefig("10primeiros.png")