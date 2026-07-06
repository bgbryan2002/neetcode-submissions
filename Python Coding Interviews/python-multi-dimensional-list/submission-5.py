from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    nlist =[]
    for llist in nested_arr:
        high_v = 0   
        for element in llist:
            if len(llist) >= 1:
                if element > high_v:
                    high_v = element
        nlist.append(high_v)
    return nlist    


# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
