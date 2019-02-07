import matplotlib.pyplot as plt
from fractions import Fraction
import subprocess

def circulo_f(h, k):
	x0 = h/k
	y0 = 1/(2*k**2)
	r = y0
	ax.add_artist(plt.Circle((x0, y0), r, fill = False))
	ax.add_artist(plt.Circle((x0, -1*y0), r, fill = False))

fracs = []
for i in range(0, 101):
	for j in range(1, 11):
		f = Fraction(i, j)
		if f not in fracs:
			fracs.append(f)

fig, ax = plt.subplots()
ax.set_xlim((-1, 1))
ax.set_ylim((-0.45, 0.45))
ax.axis('off')
ax.set_aspect('equal', )#, adjustable = "datalim")

circulos = []
for f in fracs:
	circulos.append((f.numerator, f.denominator))
	circulos.append((-1*f.numerator, f.denominator))

for c in circulos:
	circulo_f(c[0], c[1])

fig.savefig("imagen.png")
subprocess.call(["open", "imagen.png"])