import matplotlib.pyplot as plt
import pandas as pd

file = pd.read_csv("/home/phos/Desktop/time-series-pam/a2_MANCHAS.csv")

file[:30].plot("Ano","manchas", label="Manchas", grid=True)
plt.title("Aparecimento de manchas solares p/ ano (30 Primeiros Anos)", fontsize=12, color="r", style="italic", family="monospace")
plt.xlabel("Ano", fontsize=13); plt.ylabel("Qtd. de manchas", fontsize=13)
plt.xticks(rotation="vertical")
plt.tight_layout()
plt.savefig("TrintaPrimeiros_Anos_Styles")