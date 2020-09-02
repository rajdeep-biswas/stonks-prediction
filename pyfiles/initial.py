import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../datasheets/tesla.csv")
y = (df.High + df.Low) / 2
X = list(range(len(y)))

plt.plot(X, y, linewidth=0.7)
plt.show()
