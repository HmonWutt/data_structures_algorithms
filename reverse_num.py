import math 
def reverse_number_recursive(n, reversed_num=0):
    if n == 0:
        return reversed_num
    return reverse_number_recursive(n // 10, reversed_num * 10 + n % 10)
print(reverse_number_recursive(355))

def check_if_palindrome(num):
    if num==0:
        return True
    digits =int(math.log(num,10))
    first = num//(10**digits)
    last = num%10
    if first != last:
        return False
    temp = num%(10**digits)//10
    return check_if_palindrome(temp)
print(check_if_palindrome(1234321))