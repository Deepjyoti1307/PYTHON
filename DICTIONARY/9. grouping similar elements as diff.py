#Given a list of elements, perform grouping of similar elements, as different key-value lists in a
#dictionary.
#output : {4: [4, 4, 4], 6: [6, 6], 2: [2, 2], 8: [8, 8], 5: [5]}
def elements(list):
    dict = {}  
    for item in list:
        dict.setdefault(item, []).append(item)
    return dict
list1 = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8]
output1 = elements(list1)
print("Output for test_list1:", output1)