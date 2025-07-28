def dice(target,combination,lst):
   
    if target == 0:
        lst.append(combination)
        return lst
    for i in range(1,7):
        if i <=target:
            dice(target-i,combination+[i],lst)
    return lst
       

print(dice(4,[],[]))