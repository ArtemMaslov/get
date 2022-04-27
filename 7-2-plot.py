import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

values = np.loadtxt('measureData.txt', dtype = float)

T = 0
deltaU = 0
with open('settings.txt', 'r') as f:
    str = f.read().split('\n')
    T = float(str[0])
    deltaU = float(str[1])

tInc = values.argmax() / len(values) * T
tDec = T - tInc

#values = values * deltaU
t = np.array([val /len(values) *  T for val in range(0, len(values))], dtype = float)

values = values[::3]
t = t[::3]

xmin = 0
xmax = 90

ymin = 0
ymax = 3.5001

ymajorstep = 0.5
yminorstep = 0.1

xminorstep = 1
xmajorstep = 10

mpl.rcParams['font.size'] = 16

fig = plt.figure(figsize = (10, 10), dpi = 400)
axes = fig.add_subplot()

plt.title('График измерения зависимости напряжения от времени')
plt.xlabel('Время $t$, с')
plt.ylabel('Напряжение $U$, В')

plt.errorbar(t, values, fmt = '.', color = 'green')

plt.plot(t, values, label = 'Зависимость $U(t)$', color = 'green')

plt.text(55, 3, 'Время зарядки {:.1f} с\nВремя разрядки {:.1f} с'.format(tInc, tDec))

def getticks(min, max, step):
    return np.arange(min, max, step)

axes.set_yticks(getticks(ymin, ymax, ymajorstep))
axes.set_yticks(getticks(ymin, ymax, yminorstep), minor = True)

axes.set_xticks(getticks(xmin, xmax, xmajorstep))
axes.set_xticks(getticks(xmin, xmax, xminorstep), minor = True)

plt.xlim([xmin, xmax])
plt.ylim([ymin, ymax])

plt.legend()

plt.grid(b = True, which = 'major', c = 'black', alpha = 0.9)
plt.grid(b = True, which = 'minor', c = 'black', alpha = 0.3)

#plt.show()
fmt = 'png'
plt.savefig('RC_plot.' + fmt, format = fmt)