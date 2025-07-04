import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,10,100)
y = np.cos(x)
plt.plot(x,y,label ='cos(x)',color='pink',linestyle='--')
plt.title('line plot of cos(x)')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()