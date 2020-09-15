import numpy as np

xs = np.linspace(0, 3.5, 10)

ys = []
for x in xs:
  ys.append(3.8 / (1 + np.exp(-x * 2)) - 1)

print_line = '{'
for ind, _ in enumerate(xs):
  print_line += '(' + str(xs[ind] - 2) + ', ' + str(ys[ind] - 3.9) + ') '
print_line = print_line[:-1]
print_line += '}'

print(print_line)

