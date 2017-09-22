val = input().split(" ")
a, b, c = val
pi = 3.14159

atr = (float(a) * float(c))/2
ac = (float(c) * float(c))  * float(pi)
at = ((float(a) + float(b))/2) * float(c)
q = float(b) * float(b)
r = float(a) * float(b)

print('TRIANGULO: {0:0.3f}'.format(atr))
print('CIRCULO: {0:0.3f}'.format(ac))
print('TRAPEZIO: {0:0.3f}'.format(at))
print('QUADRADO: {0:0.3f}'.format(q))
print('RETANGULO: {0:0.3f}'.format(r))