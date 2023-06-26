import matplotlib.pyplot as plt 1.8
import numpy as np

def fib(n): 1.6

if n <= 1:
return 1 1.4
t = fib(n -1) fib(n-2)
return t

grlist=[] 1.2

grind=[]
def call_fibo(n):
for i in range(n): 1.0 -

fib_n fib(i+1)
fib_n_1 fib(i)
gr=fib_n/fib_n_1
grlist. append(gr)
print("i: {0}, \tfib_n: (1}, \t\tfib_n_1:{2}\t\tratio={3}"
• format (i, fib_n, fib_n_1, gr))

call_fibo(15)
X np. linspace(0, 10, 100)
plt.plot (grlist, label= 'Golden Ratio')
plt. legend()
plt. show()