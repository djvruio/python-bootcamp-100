import time
num_seconds = 3

for countdown in reversed(range(num_seconds + 1)):
    if countdown > 0:
        print(countdown, end='...')
        time.sleep(1)
    else:
        print('Go!!')