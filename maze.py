def navigate_maze(start,end,path,one_path):
    start_x,start_y = start
    end_x,end_y = end

    if start_x == end_x and start_y== end_y:
        path.append(one_path)
        return path 
    if (start_x < end_x) and (start_y < end_y):
        navigate_maze((start_x+1,start_y+1),end,path,one_path+'D')
    if (start_x < end_x):
        navigate_maze((start_x+1,start_y),end,path, one_path+'V')
    if (start_y < end_y):
        navigate_maze((start_x,start_y+1),end,path, one_path+'H')
    return path


    
print(navigate_maze((0,0),(2,2),[],""))