'''
Create a program that determines whether or not it is possible to construct a particular total using a specific number of
coins. For example, it is possible to have a total of $1.00 using four coins if they are all quarters. However, there is no
way to have a total of $1.00 using 5 coins. Yet it is possible to have $1.00 using 6 coins by using 3 quarters, 2 dimes and a
nickel. Similarly, a total of $1.25 can be formed using 5 coins or 8 coins, but a total of $1.25 cannot be formed using 4, 6
or 7 coins. Your program should read both the dollar amount and the number of coins from the user. Then it should display a
clear message indicating whether or not the entered dollar amount can be formed using the number of coins indicated. Assume
the existence of quarters, dimes, nickels and pennies when completing this problem. Your solution must use recursion. It
cannot contain any loops.


Penny 	-> $0.01
Nickel 	-> $0.05
Dime	-> $0.10
Quarter	-> $0.25


function search_alg(tgt_value: target value in dollars, no_coins: number of coins remaining):
    If no_coins is 0
        If tgt_value is not 0.00:
            return False
        return True
        
    Set nxt_no_coins equal to no_coins - 1
    search_penny 	= search_alg(tgt_value-0.01, nxt_no_coins)
    search_nickel	= search_alg(tgt_value-0.05, nxt_no_coins)
    search_dime		= search_alg(tgt_value-0.10, nxt_no_coins)
    search_quarter	= search_alg(tgt_value-0.25, nxt_no_coins)
    
    If any of the aforementioned values are True:
        return True
    return False
    
    TLDR version:
    search for each of the four coin types and check if any are possible
'''

from decimal import *

getcontext().prec = 2

PENNY_VAL 	= Decimal(1) / Decimal(100)
NICKEL_VAL 	= Decimal(1) / Decimal(20)
DIME_VAL	= Decimal(1) / Decimal(10)
QUARTER_VAL	= Decimal(1) / Decimal(4)

def search(tgt_value: Decimal, no_coins: int) -> bool:
    if no_coins == 0:
        return tgt_value == Decimal(0)
    elif tgt_value < Decimal(0):
        return False
    
    nxt_no_coins: int = no_coins - 1
    
    # Search for quarter
    if search(tgt_value-QUARTER_VAL, nxt_no_coins):
        return True
    # Search for dime
    if search(tgt_value-DIME_VAL, nxt_no_coins):
        return True
    # Search for nickel
    if search(tgt_value-NICKEL_VAL, nxt_no_coins):
        return True
    # Search for penny
    if search(tgt_value-PENNY_VAL, nxt_no_coins):
        return True

    
    return False

if __name__ == '__main__':
    tgt_value: Decimal = Decimal(input('Please input dollar amount: $'))
    no_coins: int = int(input('Please input number of coins to construct dollar amount: '))
    
    can_construct: bool = search(tgt_value, no_coins)
    
    if can_construct:
        print(f'${tgt_value} can be constructed with {no_coins} coins')
    else:
        print(f'${tgt_value} cannot be constructed with {no_coins} coins')