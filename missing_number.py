def find_missing(list1, list2):
    # parameters passed should be only list
    try:
        if isinstance(list1, list) and isinstance(list2, list):
            if list1 == [] and list2 == []:
                return 0
            else:
                # cast both list to sets
                set_a = set(list1)
                set_b = set(list2)
                list_new = set_a ^ set_b 
               
                if list_new == set():
                    return 0
                return int(list(list_new)[0]) # cast to list then to int and return
    except ValueError():
        return 'Lists only'