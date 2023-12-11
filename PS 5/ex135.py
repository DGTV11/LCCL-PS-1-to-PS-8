'''
The Sieve of Eratosthenes is a technique that was developed more than 2,000 years ago to easily find all of the prime numbers between 
2 and some limit, say 100. A description of the algorithm follows:

Write down all of the numbers from 0 to the limit Cross out 0 and 1 because they are not prime
Set p equal to 2
While p is less than the limit do
    Cross out all multiples of p (but not p itself)
    Set p equal to the next number in the list that is not crossed out
Report all of the numbers that have not been crossed out as prime

The key to this algorithm is that it is relatively easy to cross out every nth number on a piece of paper. This is also an easy task 
for a computer—a for loop can simulate this behavior when a third parameter is provided to the range function. When a number is crossed out, 
we know that it is no longer prime, but it still occupies space on the piece of paper, and must still be considered when computing later 
prime numbers. As a result, you should not simulate crossing out a number by removing it from the list. Instead, you should simulate 
crossing out a number by replacing it with 0. Then, once the algorithm completes, all of the non-zero values in the list are prime.

Create a Python program that uses this algorithm to display all of the prime numbers between 2 and a limit entered by the user. 
If you implement the algorithm correctly you should be able to display all of the prime numbers less than 1,000,000 in a few seconds.
'''

def primes(l): # l -> limit
    if l < 2:
        raise ValueError('INVALID LIMIT!')

    paper = list(range(0, l+1))
    paper[1] = 0
    x = list()
    p = 2

    while p < l:
        mn = 2
        while mn*p <= l:
            paper[mn*p] = 0
            mn += 1
        p += 1
        while paper[p] != 0:
            p += 1
    for item in paper:
        if item != 0:
            x.append(item)
    
    return x

if __name__ == '__main__':
    print(primes(int(input('Please input an integer limit more than or equal to 2: '))))