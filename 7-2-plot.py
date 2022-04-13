import matplotlib.pyplot as plt

values = []
with open('measureData.txt', 'r') as f:
    values = f.read(-1).split('\n')
    print(values[0])

T = 0
with open('settings.txt', 'r') as f:
    str = f.read().split('\n')
    T = float(str[1][18:])

t = [val * T for val in range(0, len(values))]
for st in range(0, len(values)):
    print('{:.03f} = {:.3f}'.format(t[st], float(values[st])))

plt.plot(t, values)
plt.show()