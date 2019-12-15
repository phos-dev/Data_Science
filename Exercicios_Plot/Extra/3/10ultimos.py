import matplotlib.pyplot as plt
import pandas as pd

file = pd.read_csv("/home/phos/Desktop/time-series-pam/a2_MANCHAS.csv")

x = list(file["Ano"])[-10:]
y = list(file["manchas"])[-10:]

plt.title("Qtd. de manchas solares (10 últimos anos)", fontsize = 15, color="#b30000", style="oblique")
plt.plot(x, y, color = "green")
plt.xlabel("Ano", style="italic", fontsize = 10)
plt.ylabel("Qtd. de Manchas", style="italic", fontsize = 10)
plt.legend(["Manchas"])
plt.savefig("dezultimos.jpg");