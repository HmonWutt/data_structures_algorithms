def reduce_to_zero(num,steps):
    if num==0:
        return steps
    steps +=1
    if num%2 == 0:
        return reduce_to_zero(num//2,steps)

    return reduce_to_zero(num-1,steps)

print(reduce_to_zero(8,0))

