"""
This is an implementation of the AKS primality test by Agrawal, Kayal and 
Saxena (2004) in Python.

The algorithm outline:

Input n > 1

1. Check that n is not a perfect power a^b for some a>1 and b>1.
   If it is output composite

2. Find smallest r such that ord_r(n) > (log_2 n)^2. Skip this r if 
   gcd(r,n) != 1

3. For all 2 <= a <= min(r, n-1), check a does not divide n. Otherwise output
   composite. 
   
4. If n <= r output prime. 

5. For a = 1 to floor( sqrt(totient(r)) log2(n)) do
        if (X + a)^n != X^n +a mod (X^r -1, n) output composite

6. Output prime. 


References:
    PRIMES is in P, Annals of Mathematics. 160 (2): 781-793
_________________________________________________________________________

Author: Tang U-Liang
Email: tang_u_liang@sp.edu.sg
_________________________________________________________________________
"""

import math
import decimal
from decimal import Decimal
import sys

if sys.version_info < (3,):
    input = raw_input

def gcd(m,n):
    while m%n != 0:
        m, n = n, m%n

    return n

def perfect_power(n):
    """
    Checks that n is a perfect power i.e. n=a^b for a>1 and b>1
    
    Returns
        bool, True indicates that it is a perfect power. Therefore,
              False indicates that the algorithm continues.
    """
    ctx = decimal.getcontext()
    ctx.prec = 1002
    tol = Decimal('1E-999')
    
    # print(ctx)
    M = math.ceil(math.log(n, 2))
    for b in range(2, M):
        
        a = ctx.power(n, ctx.power(b, -1))
        # print(a)

        if abs(ctx.to_integral_exact(a)-a) <= tol:
            return True

    return False

def main():

    n = input("Enter prime\n>>")
    n = int(n)

    if perfect_power(n):
        return "Composite"

    # get smallest r ... (step 2)

    for a in range(2, min(r, n-1)+1):
        if n%a == 0:
            return "Composite"

    if r <= n:
        return "Prime"

if __name__ == "__main__":
    main()

