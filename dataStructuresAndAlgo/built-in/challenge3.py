def count_low_high(num_list):
    lows =0
    highs =0
    for i in num_list:
        if(i >50 or i %3 ==0):
            highs+=1
        else:
            lows+=1
    return [lows,highs]

num_list = [20, 9, 51, 81, 50, 42, 77]


print(count_low_high(num_list))