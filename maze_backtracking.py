def path_finder(start,end,visited, direction,path,paths):
    start_x,start_y = start
    end_x,end_y = end
    if start_x == end_x and start_y == end_y:
        coordinates = [x for x in visited]
        #path.append(coordinates)
        path+=direction
        paths.append(path)
        return paths
    if (start_x,start_y) not in visited:
        path+=direction
        visited.append((start_x,start_y))
   
    else:
        return 
    
    if start_x<end_x:
        path_finder((start_x+1,start_y),end,visited,"D",path,paths)
    if start_x >0:
        path_finder((start_x-1,start_y),end,visited,"U",path,paths)
    if start_y <end_y:
        path_finder((start_x,start_y+1),end,visited,"R",path,paths)
    if start_y >0:
        path_finder((start_x,start_y-1),end,visited,"L",path,paths)
    visited.remove((start_x,start_y))
    return paths
print(path_finder((0,0), (2,2), [],"","",[]))



	
