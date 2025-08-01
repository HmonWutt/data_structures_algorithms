def reduce_to_zero(num,steps):
    if num==0:
        return steps
    return reduce_to_zero(num//2,steps+1)

print(reduce_to_zero(4,0))