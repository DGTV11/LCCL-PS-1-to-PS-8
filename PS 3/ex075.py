"""
Initialize d to the smaller of m and n.
While d does not evenly divide m or d does not evenly divide n do
    Decrease the value of d by 1
Report d as the greatest common divisor of n and m
"""

n = abs(int(input('n = ')))
m = abs(int(input('m = ')))

d = min(n, m)

while d % n != 0 or d % m != 0:
    d -= 1

print(f"Greatest Common Divisor --> {d}")