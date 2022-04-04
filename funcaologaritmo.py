import matplotlib.pyplot as plt
import numpy as np

base = float(input('Digite o valor da base '))

if(base > 0) and (base != 1):
    x = np.array([0.25,0.5 ,1,2,4])
    y = 0

    def Funcaolog(y, x):

        y = np.log(x) / np.log(base)

        if(y[0] > y[4]):
            print('Esta função é decrescente')
        else:
            print('Esta função é crescente')
        print(y)
        return y

    plt.grid(color='gray', linestyle='-.', linewidth=0.5)

    plt.xlabel('x')
    plt.ylabel('y')

    plt.plot(x.flatten(), Funcaolog(y, x).flatten())
    plt.show()
else:
    print('Base negativo, igual a zero ou igual a 1')

