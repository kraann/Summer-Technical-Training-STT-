def sort_tuples(tuples_list):
   
    
    return sorted(tuples_list, key=lambda x: x)


tuples_list = [(3, 4), (1, 2), (5, 0), (2, 3)]
    
sorted_list = sort_tuples(tuples_list)

print("Sorted list:", sorted_list)
