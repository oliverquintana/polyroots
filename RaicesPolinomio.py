import numpy as np

def rec2pol(n):
    y = n.imag
    x = n.real

    theta = np.arctan2(y,x)
    r = np.sqrt((y**2) + (x**2))

    return r, np.degrees(theta)

def pol2rec(r, theta):
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    return complex(x,y)

def derivate(poly):

    pol = poly.copy()
    pol.reverse()

    for i,n in enumerate(pol):
        pol[i] = i * n

    pol.reverse()
    temp = [0]
    for i in pol:
        temp.append(i)

    a = temp[:-1]

    return a

def eval_pol(poly,value):
    pol = poly.copy()
    pol.reverse()
    temp = [pol[0]]

    for i in range(len(pol) - 1):
        t = pol[i+1] * (value ** (i+1))
        temp. append(t)

    temp.reverse()

    return sum(temp)

def roots(pol, xn = complex(1,0)):

    print("Coeficientes del Polinomio: {} Grado: {}".format(pol, len(pol) - 1))
    dpol = derivate(pol)
    counter = 0
    epsilon = 0.005
    xn = complex(1, 1)
    step = 360 / (len(pol) - 1)
    p_roots = []

    for i in range(len(pol) - 1):

        while abs(eval_pol(pol,xn)) > epsilon:

            t1 = eval_pol(pol, xn)
            t2 = eval_pol(dpol, xn)
            t = t1 / t2
            xn = xn - t

        p_roots.append((xn))
        r, theta = rec2pol(xn)
        new_theta = theta + step
        xn = pol2rec(r, np.radians(new_theta))

    return p_roots

if __name__ == "__main__":

    poly = [1, 2, 3, 4]
    roots = (roots(poly))
    print("Raíces: ")
    for i in roots:
        print(i)
