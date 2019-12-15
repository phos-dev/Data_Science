import matplotlib.pyplot as plt
import pandas as pd

file = pd.read_csv("/home/phos/Desktop/time-series-pam/a2_MANCHAS.csv")

file[:30].plot("Ano","manchas", label="Manchas", grid=True)
plt.title("Aparecimento de manchas solares p/ ano", fontsize=17, color="r", style="italic", family="monospace")
plt.xlabel("Ano", fontsize=13); plt.ylabel("Qtd. de manchas", fontsize=13)
plt.xticks(rotation="vertical")
plt.tight_layout()
plt.savefig("Boxplot_M")