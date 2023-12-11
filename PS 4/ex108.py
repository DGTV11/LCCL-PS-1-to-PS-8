# 1 cup        -> 16 tablespoons
# 1 tablespoon -> 3 teaspoons

def reduMeas(cu, ta, te):
    x = te // 3
    ta += x
    te %= 3

    x = ta // 16
    cu += x
    ta %= 16

    return cu, ta, te

if __name__ == '__main__':
    a1 = int(round(float(input("No. of cups: "))))
    b1 = int(round(float(input("No. of tablespoons: "))))
    c1 = int(round(float(input("No. of teaspoons: "))))

    a2, b2, c2 = reduMeas(a1, b1, c1)

    print(f"""{a1} cups, {b1} tablespoons, {c1} teaspoons 
=
{a2} cups, {b2} tablespoons, {c2} teaspoons""")