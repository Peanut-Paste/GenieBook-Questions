# In order to win the prize for most cookies sold, my friend Alice and I are going to merge our Girl Scout Cookies orders and enter as one unit.
# Each order is represented by an "order id" (an integer).
# We have our lists of orders sorted numerically already, in lists. Write a function to merge our lists of orders into one sorted list.

# For example:
# my_list = [3, 4, 6, 10, 11, 15]
# alices_list = [1, 5, 8, 12, 14, 19]
# print merge_lists(my_list, alices_list)
# # prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]

# Do not use predefined array functions to merge and sort (array_merge, array_sort, .sort(),
# .merge() or any other similar functions).

def merge_list(l1, l2):
    res = l1 + l2
    for i in range(len(res)):
        for x in range(len(res) - 1):
            if res[x] > res[x + 1]:
                temp = res[x]
                res[x] = res[x + 1]
                res[x + 1] = temp
    return res

print(merge_list([3, 4, 6, 10, 11, 15], [1, 5, 8, 12, 14, 19]))