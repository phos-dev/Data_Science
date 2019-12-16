import matplotlib.pyplot as plt
import pandas as pd

file = pd.read_csv("/home/phos/Desktop/time-series-pam/a2_MANCHAS.csv")

x_2 = list(file["Ano"])[0:10]
y_2 = list(file["manchas"])[:10]

plt.title("Qtd. de manchas solares (10 primeiros anos)", fontsize = 15, color="#b30000", style="oblique")
plt.plot(x_2, y_2, color = "green")
plt.xlabel("Ano",color="blue", style="italic")
plt.ylabel("Manchas",color="blue", style="italic")
plt.legend(["Manchas"])
plt.savefig("dezprimeiros_s.jpg")