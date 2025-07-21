def delete_target_character(string,target):
    if not string:
        return ""
    if string[0] != target:
        return string[0]+delete_target_character(string[1:],target)  
    return delete_target_character(string[1:],target)

print(delete_target_character("abeacaecd", "a"))