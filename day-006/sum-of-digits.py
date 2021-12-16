t = int(input())

for _ in range(t):
    n = int(input())
    sm = 0
    #print(f'n:{n}', f'sm:{sm}')
    while n > 0:
        sm = sm + n % 10
        # print(f'n:{n}', f'sm:{sm}')
        n = n//10
    print(sm)