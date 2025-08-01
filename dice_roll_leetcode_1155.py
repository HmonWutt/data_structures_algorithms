def dice_rolls(faces,num,target):
    count = 0
    if num==0:
        count+=1
        return count
    if num < 0:
        return 0
    for face in range(1,faces+1):
        if face<=target:
            count+=dice_rolls(faces,num-face,target)
    return count
print(dice_rolls(6,4,3))