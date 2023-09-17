import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  

data = np.genfromtxt("lcurve.out", names=True)

plt.figure(figsize=(10,7), dpi=300)
for name in data.dtype.names[1:-1]:
# for name in data.dtype.names[-3:-1]:
    plt.plot(data['step'], data[name], rasterized=True, label=name)
plt.legend()
plt.xlabel('Step')
plt.ylabel('Loss')
# plt.xscale('symlog')
plt.yscale('log')
plt.grid()
plt.savefig('LearnCurve.png', bbox_inches='tight')
plt.savefig('LearnCurve.svg', bbox_inches='tight')
