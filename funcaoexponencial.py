import matplotlib.pyplot as plt
import numpy as np

base = float(input('Digite o valor da base'))

if(base > 0) and (base != 1):
    x = np.array([-3,-2,-1,0,1,2,3])
    y = 0

    def Funcaoexpo(y, x):
        y = base**x
        if(y[0] > y[4]):
            print('Esta função é decrescente')
        else:
            print('Esta função é crescente')
        print(y)
        return y

    plt.grid(color='gray', linestyle='-.', linewidth=0.5)

    plt.xlabel('y')
    plt.ylabel('x')

    plt.plot(x.flatten(), Funcaoexpo(y, x).flatten())
    plt.show()
else:
    print('Base negativo, igual a zero ou igual a 1')

