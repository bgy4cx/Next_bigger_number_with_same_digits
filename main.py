def next_bigger(digits):
    l_digits = [int(a) for a in str(digits)]    
    m = -1
    # The below code determine the first smaller number backward. 
    for i in reversed(range(len(l_digits))):
        j = i - 1
        print(j,i)
        if l_digits[i] > l_digits[j]:
            # It has to check the bigger number what is the smallest in the values. 
            bigger_digits = [k for k in l_digits[j:len(l_digits)] if l_digits[j] < k]
            m = min(bigger_digits) 
            # It has to remove the bigger but smallest number because we are change the l_digits[j] with this number.
            last_digits = l_digits[j:]
            last_digits.remove(m)
            # It have to sort the rest of numbers because it ensure the smallest but bigger number. 
            last_digits.sort()   
            # It adds the smallest bigger number and the rest of sorted numbers. 
            l_digits[j:] = [m] + last_digits   
            break
    return int(''.join([str(a) for a in l_digits])) if m != -1 else m