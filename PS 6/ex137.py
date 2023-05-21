from random import randint

if __name__ == '__main__':
    totals = list()
    totals_percent_count = {
        2   : 0,
        3   : 0,
        4   : 0,
        5   : 0,
        6   : 0,
        7   : 0,
        8   : 0,
        9   : 0,
        10  : 0,
        11  : 0,
        12  : 0
    }
    for i in range(1000):
        totals.append(randint(1, 6) + randint(1, 6))
    
    for item in totals:
        totals_percent_count[item] += 0.1
    
    print(f'''
    Total  Expected  Simulated
    2        02.78%     {totals_percent_count[2]:0>5.2f}%
    3        05.56%     {totals_percent_count[3]:0>5.2f}%
    4        08.33%     {totals_percent_count[4]:0>5.2f}%
    5        11.11%     {totals_percent_count[5]:0>5.2f}%
    6        13.89%     {totals_percent_count[6]:0>5.2f}%
    7        16.67%     {totals_percent_count[7]:0>5.2f}%
    8        13.89%     {totals_percent_count[8]:0>5.2f}%
    9        11.11%     {totals_percent_count[9]:0>5.2f}%
    10       08.33%     {totals_percent_count[10]:0>5.2f}%
    11       05.56%     {totals_percent_count[11]:0>5.2f}%
    12       02.78%     {totals_percent_count[12]:0>5.2f}%
    ''')