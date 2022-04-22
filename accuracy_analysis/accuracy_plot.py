import matplotlib.pyplot as plt
import csv


def load_csv(filepath, _delimeter=','):
    data = []
    with open(filepath) as datafile:
        datac = csv.reader(datafile, delimiter=_delimeter)
        for row in datac:
            if len(row) != 0:
                data.append(row)
    return data


# 6 features test data = red
filep = './accuracy_6_0.3.txt'
data = load_csv(filep)
treeno = [int(x[0]) for x in data]
accuracy = [float(x[1]) for x in data]
plt.plot(treeno, accuracy, 'r-')

filep = './accuracy_6_0.5.txt'
data = load_csv(filep)
treeno = [int(x[0]) for x in data]
accuracy = [float(x[1]) for x in data]
plt.plot(treeno, accuracy, 'r:')

filep = './accuracy_6_0.8.txt'
data = load_csv(filep)
treeno = [int(x[0]) for x in data]
accuracy = [float(x[1]) for x in data]
plt.plot(treeno, accuracy, 'r--')


# 5 features test data = blue
filep = './accuracy_5_0.3.txt'
data = load_csv(filep)
treeno = [int(x[0]) for x in data]
accuracy = [float(x[1]) for x in data]
plt.plot(treeno, accuracy, 'b-')

filep = './accuracy_5_0.5.txt'
data = load_csv(filep)
treeno = [int(x[0]) for x in data]
accuracy = [float(x[1]) for x in data]
plt.plot(treeno, accuracy, 'b:')

filep = './accuracy_5_0.8.txt'
data = load_csv(filep)
treeno = [int(x[0]) for x in data]
accuracy = [float(x[1]) for x in data]
plt.plot(treeno, accuracy, 'b--')

# 4 features test data = black
filep = './accuracy_4_0.3.txt'
data = load_csv(filep)
treeno = [int(x[0]) for x in data]
accuracy = [float(x[1]) for x in data]
plt.plot(treeno, accuracy, 'k-')

filep = './accuracy_4_0.5.txt'
data = load_csv(filep)
treeno = [int(x[0]) for x in data]
accuracy = [float(x[1]) for x in data]
plt.plot(treeno, accuracy, 'k:')

filep = './accuracy_4_0.8.txt'
data = load_csv(filep)
treeno = [int(x[0]) for x in data]
accuracy = [float(x[1]) for x in data]
plt.plot(treeno, accuracy, 'k--')

# 3 features test data = green
filep = './accuracy_3_0.3.txt'
data = load_csv(filep)
treeno = [int(x[0]) for x in data]
accuracy = [float(x[1]) for x in data]
plt.plot(treeno, accuracy, 'g-')

filep = './accuracy_3_0.5.txt'
data = load_csv(filep)
treeno = [int(x[0]) for x in data]
accuracy = [float(x[1]) for x in data]
plt.plot(treeno, accuracy, 'g:')

filep = './accuracy_3_0.8.txt'
data = load_csv(filep)
treeno = [int(x[0]) for x in data]
accuracy = [float(x[1]) for x in data]
plt.plot(treeno, accuracy, 'g--')

# 2 features test data = magenta
filep = './accuracy_2_0.3.txt'
data = load_csv(filep)
treeno = [int(x[0]) for x in data]
accuracy = [float(x[1]) for x in data]
plt.plot(treeno, accuracy, 'm-')

filep = './accuracy_2_0.5.txt'
data = load_csv(filep)
treeno = [int(x[0]) for x in data]
accuracy = [float(x[1]) for x in data]
plt.plot(treeno, accuracy, 'm:')

filep = './accuracy_2_0.8.txt'
data = load_csv(filep)
treeno = [int(x[0]) for x in data]
accuracy = [float(x[1]) for x in data]
plt.plot(treeno, accuracy, 'm--')

plt.show()
