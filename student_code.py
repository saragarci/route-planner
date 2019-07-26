from scipy.spatial import distance
import heapq


def get_distance(M, p1, p2):
    point_one = M.intersections[p1]
    point_two = M.intersections[p2]
    return distance.euclidean(point_one, point_two)


def a_star(M, successors, goal):
    current_path = heapq.heappop(successors)
    node = current_path[1][len(current_path[1])-1]

    if node == goal:
        heapq.heappush(successors, current_path)
        return
    
    for element in M.roads[node]:
        if len(current_path[1]) == 1:
            h = get_distance(M, node, element) + get_distance(M, element, goal)
            previous_nodes = [node, element]
            g = get_distance(M, node, element)
        else:
            h = current_path[2] + get_distance(M, node, element) + get_distance(M, element, goal)
            previous_nodes = current_path[1].copy()
            previous_nodes.append(element)
            g = current_path[2] + get_distance(M, node, element)     
        new_node = [h, previous_nodes, g, get_distance(M, element, goal)]      
        heapq.heappush(successors, new_node)
                
    a_star(M, successors, goal)   
    

def shortest_path(M, start, goal):
    if start == goal:
        return [start]
    successors = []
    heapq.heapify(successors)
    heapq.heappush(successors, [0,[start]])
    a_star(M, successors, goal)
    return heapq.heappop(successors)[1]


