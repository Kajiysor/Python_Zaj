# poly1(x) + poly2(x)
def add_poly(poly1: list, poly2: list) -> list:
    size = max(len(poly1), len(poly2))
    sum = [0 for i in range(size)]

    for i in range(len(poly1)):
        sum[i] = poly1[i]

    for i in range(len(poly2)):
        sum[i] += poly2[i]

    while sum[-1] == 0 and len(sum) > 1:
        sum.pop()

    return sum


# poly1(x) - poly2(x)
def sub_poly(poly1: list, poly2: list) -> list:
    size = max(len(poly1), len(poly2))
    sub = [0 for i in range(size)]

    for i in range(len(poly1)):
        sub[i] = poly1[i]

    for i in range(len(poly2)):
        sub[i] -= poly2[i]

    while sub[-1] == 0 and len(sub) > 1:
        sub.pop()

    return sub


# poly1(x) * poly2(x)
def mul_poly(poly1: list, poly2: list) -> list:
    size = (len(poly1) + len(poly2) - 1)
    prod = [0 for i in range(size)]

    for i in range(len(poly1)):
        for j in range(len(poly2)):
            prod[i + j] += poly1[i] * poly2[j]

    while prod[-1] == 0 and len(prod) > 1:
        prod.pop()

    return prod


# bool, [0], [0,0], itp.
def is_zero(poly: list) -> bool:
    return False if set(poly) != {0} else True


# bool, porównywanie poly1(x) == poly2(x)
def eq_poly(poly1: list, poly2: list) -> bool:
    for poly in [poly1, poly2]:
        while poly[-1] == 0 and len(poly) > 1:
            poly.pop()

    return poly1 == poly2


# poly(x0), algorytm Hornera
def eval_poly(poly: list, x0: float) -> float:
    res = False
    for x in reversed(poly):
        if not res:
            res = x
            continue
        res = res * x0 + x

    return res


# poly1(poly2(x)), trudne!
def combine_poly(poly1: list, poly2: list) -> list:
    res = [0]
    for it, pos in enumerate(poly1):
        res = add_poly(res, [pos * el for el in pow_poly(poly2, it)])
    return res


# poly(x) ** n
def pow_poly(poly: list, n: int) -> list:
    res = [1]
    for i in range(n):
        res = mul_poly(res, poly)

    while res[-1] == 0 and len(res) > 1:
        res.pop()

    return res


# pochodna wielomianu
def diff_poly(poly: list) -> list:
    poly.reverse()
    return [poly[i] * i for i in range(1, len(poly))]

# p1 = [2, 1]                   # W(x) = 2 + x
# p2 = [2, 1, 0]                # jw  (niejednoznaczność)
# p3 = [-3, 0, 1]               # W(x) = -3 + x^2
# p4 = [3]                      # W(x) = 3, wielomian zerowego stopnia
# p5 = [0]                      # zero
# p6 = [0, 0, 0]                # zero (niejednoznaczność)
