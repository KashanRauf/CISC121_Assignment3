def bisection_zero(f_x, a_i, b_i):
    """
    Finds one zero of the polynomial by using the bisection method.
    This value is within a small error range to provide a highly approximate value.
    This is because the exact value may take too many iterations to be found.

    Use: zero_f = bisection_zero(f_x,a_0,b_0)

    Parameters:   
     f_x - a polynomial function (list)
     a_0 - a test point with f(a_0) < 0 (float)
     b_0 - a test point with f(b_0) > 0 (float)

    Returns:
     m_i - an approximation of a zero of the polynomial f(m_i) = 0 (float)
    """

    # Midpoint and function value
    m_i = (a_i+b_i)/2
    f_a, f_m, f_b = func_eval(f_x, a_i), func_eval(f_x, m_i), func_eval(f_x, b_i)

    # Iterates while f(a) and f(b) are on either side of 0 and f(m) is outside of error margin
    while f_a < 0 and f_b > 0 and abs(f_m) > 1e-010:
        if f_m == 0:
            return m_i
        elif f_m < 0:
            a_i = m_i
        else:
            b_i = m_i
        
        m_i = (a_i+b_i)/2
        f_a, f_m, f_b = func_eval(f_x, a_i), func_eval(f_x, m_i), func_eval(f_x, b_i)
    return m_i

# Evaluates polynomial function 'f' (given as list) at point 'x'
def func_eval(f, x):
    val = 0
    order = len(f)-1
    for i in f:
        val += i * (x**order)
        order -= 1
    return val


# Defining polynomial function as a list, function and test cases are hard-coded
f_x = [1,-7,10] # x^2 -7x +10
a_0, b_0 = 4,1

zero_f = bisection_zero(f_x, a_0, b_0)
zero_f = '{0:.3g}'.format(zero_f)
print("A zero of the function is located at approximately x =", zero_f)
