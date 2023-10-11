import time

# The exponentiation algorithm which runs at a time complexity of O(log n), where n is exponent
def pow(a, n):
    if n == 0:
        return 1
    x = pow(a, n//2)
    if n%2==0:
        return x*x
    else:
        return a*x*x 

if __name__ == '__main__':
    a, n = 34, 40
    t = []

    for n in range(50):
        start = time.time()
        pow(a, n)
        end = time.time()
        t.append(round((end - start)*(1000000), 3))

    print('average running time is', sum(t)/len(t), 'microseconds')
