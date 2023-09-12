primos = []
i = 1

while 0< i <=100:
    if i%2 != 0:
        if i%3 != 0:
            if i%5 != 0:
                if i%7 != 0:
                    primos = [i]
i = i+1

