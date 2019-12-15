import matplotlib.pyplot as plt
import pandas as pd
file = pd.read_csv("/home/phos/Desktop/time-series-pam/a2_MANCHAS.csv")

plt.boxplot(file["manchas"])
plt.savefig("boxplot")
