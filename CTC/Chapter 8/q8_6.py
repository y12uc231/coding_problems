import timeit
def toh(n,a,b,c):
    if n == 1:
        print('Move From '+a+' to '+c)
        return;
    toh(n-1,a,c,b)
    print('Move From ' + a + ' to ' + c)
    toh(n - 1, b, a, c)

start = timeit.default_timer()
toh(3,'A','B','C')
stop = timeit.default_timer()

print(stop-start)