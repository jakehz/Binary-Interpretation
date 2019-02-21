import math 
def rep_signed_int(x):
    # represent the inputted binary number list as a signed integer
    m = len(x)
    operator1 = 0
    for i in range(1, m-1):
        # array index:
        # 0 1 2 3
        #[1,0,1,0]
        # 3 2 1 0
        # binary power

        # binary numbers are essentially backwards arrays, so we calculate
        # the power by taking the length minus 1, and subtracting the current index
        power = m - 1 - i
        #then calculate the sum of each of the binary numbers before the sign bit
        operator1 += x[i]*(2**power)

    return operator1 - (x[0]*(2**(m-1)))

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

def round(x):
    return math.floor(x+0.5)

def floating_point_convert(mantissa, power):
    #NOT WORKING

    # takes the mantissa and power of a base 10
    # floating point number and returns the power
    # and mantissa of a base 2

    # power of base 2 exponent, 'e2'
    power2 = 0

    if power < 0:
        while power < 0: # 'as long as m is less than or equal to the largest numerator
            #  value minus 5 divided by 2' ??
            #  not sure what above means
            mantissa *= 2
            power2 -= 1

            mantissa = round(mantissa/10)
            power += 1
    if power > 0:
        while power > 0:
            mantissa = round(mantissa/2)
            power2 += 1

            mantissa *= 10
            power -= 1

    return [mantissa, power2]
