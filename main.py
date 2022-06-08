def next_bigger(digits):
    l_digits = [int(a) for a in str(digits)]    
    m = -1
    # The below code determine the first smaller number backward. 
    for i in reversed(range(len(l_digits))):
        if m >= 0:
            break
        for j in reversed(range(i)):
            if l_digits[i] > l_digits[j]:
                # It has to check the bigger number what is the smallest in the values. 
                bigger_digits = [k for k in l_digits[j:len(l_digits)] if l_digits[j] < k]
                m = min(bigger_digits) 
                # It has to remove the bigger but smallest number because we are change the l_digits[j] with this number.
                last_digits = [k for k in l_digits[j:len(l_digits)]]
                last_digits.remove(m)
                # It have to sort the rest of numbers because it ensure the smallest but bigger number. 
                last_digits.sort()   
                l_digits[j] = m
                # It changes the rest of the numbers with the sorted list. 
                n=0
                for k in range(i,len(l_digits)):
                    l_digits[k] = last_digits[n]
                    n += 1
                break
            else:
                break
    return int(''.join([str(a) for a in l_digits])) if m != -1 else m