'''
Given a list of numbers and a number k, return whether any two numbers from
the list add up to k. For example, given [10, 15, 3, 7] and k of 17, return 
true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''
def is_sum_up(arr, k):
    cache = []
    for i in arr:
        if i in cache:
            return True
        else:
            diff = k - i
            cache.append(diff)
    return False