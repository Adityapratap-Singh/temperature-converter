# temperature_converter.py

def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

def c_to_k(c):
    return c + 273.15

def k_to_c(k):
    return k - 273.15

def f_to_k(f):
    return c_to_k(f_to_c(f))

def k_to_f(k):
    return c_to_f(k_to_c(k))
