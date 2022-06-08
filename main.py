def next_bigger(digits):
    s_digits = str(digits)
    l_digits = list(s_digits)
    c = -1
    for i in reversed(range(len(l_digits))):
        if c >= 0:
            break
        for j in reversed(range(i)):
            if int(l_digits[i]) > int(l_digits[j]):
                print(l_digits[j:len(l_digits)])
                bigger_digits = [int(k) for k in l_digits[j:len(l_digits)] if int(l_digits[j]) < int(k)]
                m = min(bigger_digits)
                print(bigger_digits)
                print(m) 
                last_digits = [int(k) for k in l_digits[j:len(l_digits)]]
                last_digits.remove(m)
                last_digits.sort()
                print('After sort: ',last_digits)
                c = m     
                l_digits[j] = str(m)
                n=0
                for k in range(i,len(l_digits)):
                    l_digits[k] = str(last_digits[n])
                    n += 1
                print(l_digits)
                break
            else:
                break
    return int(''.join(l_digits)) if c != -1 else c