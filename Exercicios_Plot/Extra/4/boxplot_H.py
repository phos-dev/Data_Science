import matplotlib.pyplot as plt
import pandas as pd
import math
file = pd.read_csv("/home/phos/Desktop/time-series-pam/a2_MANCHAS.csv")[:30]

primeiro_quartil, segundo_quartil, terceiro_quartil = round(file.manchas.quantile([0.25, 0.5, 0.75]), 2)

menor, maior = file.manchas.min(), file.manchas.max()

plt.boxplot(file["manchas"])
plt.title("Aparecimento de manchas solares p/ ano (30 primeiros anos)", fontsize=12, color="r", style="italic", family="monospace")
plt.ylabel("Quantidade de manchas p/ ano", fontsize=10)
plt.legend(["1º quartil = " + str(primeiro_quartil), "2º quartil = " + str(segundo_quartil), "3º quartil = " + str(terceiro_quartil), "Maior qtd. = " + str(maior), "Menor qtd. = " + str(menor)], loc="upper right")  
plt.grid()
plt.savefig("30primeirosanos.jpg")