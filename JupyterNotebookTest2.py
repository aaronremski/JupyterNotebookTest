# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.6.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

x = np.arange(-3, 6, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.show()
# -


