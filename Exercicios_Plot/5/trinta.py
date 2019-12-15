import matplotlib.pyplot as plt
import pandas as pd

file = pd.read_csv("/home/phos/Desktop/time-series-pam/a2_MANCHAS.csv")[:30]
x = list(file["Ano"]); y = list(file["manchas"])
plt.plot(x, y)
plt.title("Aparecimento de manchas solares p/ ano (30 primeiros anos)",fontsize=12, color="r", style="italic", family="monospace")
plt.xlabel("Ano", size=12); plt.ylabel("Quantidade de Manchas", size=12)
plt.xticks(rotation="vertical")
plt.grid()
plt.tight_layout()
plt.savefig("trintaprimeiros.png")