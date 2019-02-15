def rep_signed_int(x):
    # represent the inputted binary number list as a signed integer
    # CAUTION: not sure if this works
    m = len(x)
    operator1 = 0
    for i in range(0, m - 2):
        operator1 += x[i]*(2**i)

    return operator1 - x[m-1]*(2**(m-1))

def find_max_size(power):
    # takes size of the binary integer
    # returns the maximum size of that binary integer
    sum = 0
    # goes from 0 to one less than power
    # e.g. for bits from 0 to 51 for a
    # 52 bit binary number
    for i in range(0, power):
        sum += 2**i;
    return sum


