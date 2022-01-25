import random
from pip._vendor.msgpack.fallback import xrange
from math import floor
def prime_test(N, k):
	# This is main function, that is connected to the Test button. You don't need to touch it.
	return fermat(N,k), miller_rabin(N,k)


def mod_exp(x, y, N):
    # You will need to implement this function and change the return value.

    #Time Complexity
    #   O(n^3)

    if y == 0:              #Formulated from seudocode in book
        return 1
    a = mod_exp(x, floor(y / 2), N)
    if (y % 2) == 0:
        return a * a % N    # a squared with remainder
    else:
        return x * a * a % N    #x*a squared check remainder




def fprobability(k):
    # You will need to implement this function and change the return value.

    # Time Complexity
    #   O(n)

    v = (1-pow(1/2, k))*100     # gathered from figure 1.7 and 1.8 of textbook
    return v


def mprobability(k):
    # You will need to implement this function and change the return value.

    # Time Complexity
    #   O(n)

    p = (1-(1/(pow(4,k))))*100      # formulated from pg 28 of book
    return p                        # Used 1/4 because of the Miller Rabin test Instead of Fermat's


def fermat(N,k):
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.

    # Time complexity
    #   O( k  log N)
    #   k is the number of iterations
    #   N is the number input

    # Got main Ideas from book and Design Experience
    if N == 2 or N == 3: # return prime if N =2
        return 'prime'
    if N % 2 == 0: #Return Composite if N is divisible by 2
        return 'composite'
    for i in range(k):
        z = random.randint(2, N - 1)  # random integer (low, high)
        if pow(z, N - 1, N) != 1:
            return 'composite'
    return 'prime'



def miller_rabin(N,k):
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.

    # time complexity
    #   O( n log^3 N )
    #   n is k
    #   N is the number input



    if N == 2 or N == 3:
        return 'prime'  #Return "prime" if N = 2 or 3
    if N % 2 == 0:
        return 'composite' #Return "composite" if N is divisible by 2

    l = 0
    m = N - 1

    while m & 1 == 0:
        l += 1
        m = m // 2
    for i in range(k):
        z =2 +  random.randint(1, N - 4) # random int (low, high)
        x = mod_exp(z, m, N)
        if x == 1 or x == N - 1:
            continue                # tests using modulor exponentation
        for j in xrange(l - 1):
            x = mod_exp(x, 2, N)    # calls Mod_Exp from above
            if x == N - 1:
                break
        else:
            return 'composite'
    return 'prime'
