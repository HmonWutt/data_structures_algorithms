dirs = [(-1,-1,"LU,"),(-1,1,"RU,"),(1,-1,"LD,"),(1,1,"RD,"),(0,1,"R,"),(1,0,"D,"),(-1,0,"U,"),(0,-1,"L,")]
end_x = 4
end_y = 4

def is_in_bound(current_x,current_y,add_x,add_y):
    return 0 <=current_x<end_x and 0<=current_y <end_y
def traverse(start_x,start_y,path,visited):
    paths = []
    if start_x == end_x and start_y == end_y:
        paths.append(path[:-1])
        return paths
    for x,y,dir in dirs:
        if is_in_bound(start_x,start_y,x,y) and (start_x+x,start_y+y) not in visited:
            visited.append((start_x+x,start_y+y))
            paths+=traverse(start_x+x,start_y+y,path+dir,visited)
            visited.remove((start_x+x,start_y+y))
    return paths

        
paths = traverse(0,0,"",[(0,0)])
print(paths)
print(len(paths))

