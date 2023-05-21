import math

a = abs(float(input('Please key in the numerical value for a (Any negative numbers will be absoluted): ')))
b = abs(float(input('Please key in the numerical value for b (Any negative numbers will be absoluted): ')))

sum = a+b
diff = a-b
prod = a*b
intdiv = a//b
mod = a%b
log10 = math.log10(a)
a_power_b = a**b

print(f'''- The sum of a and b: {sum}
- The difference when b is subtracted from a: {diff}
- The product of {a} and {b}: {prod}
- The quotient when {a} is divided by {b}: {intdiv}
- The remainder when {a} is divided by {b}: {mod}
- The result of log10({a}): {log10}
- The result of {a}^{b}: {a_power_b}
''')