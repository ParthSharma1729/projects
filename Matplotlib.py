import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 3, 100)

y=2*x


plt.plot(x, y, label='linear')
# plt.plot(x, x**2, label='quadratic')
# plt.plot(x, x**3, label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')

plt.title("Simple Plot")

plt.legend()

plt.show()
plt.title('SAMPLE')
# x=[]
# y=[]

#
# for i in range(-50,51,1):
#     x.append(i)
#     # if i<0:
#     #     y.append(-1*i)
#     # else:
#     #     y.append(i)
#
#
#
#
#
# plt.plot(x, y)
# plt.show()
