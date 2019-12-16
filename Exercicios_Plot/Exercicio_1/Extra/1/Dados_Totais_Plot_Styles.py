import matplotlib.pyplot as plt
import pandas as pd

file = pd.read_csv("/home/phos/Desktop/time-series-pam/a2_MANCHAS.csv")
file.plot(x="Ano", y="manchas", label="Manchas", color="green")
plt.title("Aparecimento de manchas solares p/ ano", fontsize=16, color="#991820", style="italic", family="monospace")
plt.xticks(rotation="vertical")
plt.xlabel("Ano", fontsize=13, style="oblique", color="red")
plt.ylabel("Quantidade de Manchas", fontsize=13, style="oblique", color="red");
plt.grid()
plt.tight_layout()
plt.savefig("total.jpg")