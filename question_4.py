# You have a list of integers, and for each index you want to find the product of every integer except the integer
# at that index. Write a function get_products() that takes a list of integers and returns a list of the products.

# For example, given:
# [1, 7, 3, 4]
# your function would return:
# [84, 12, 28, 21]
# by calculating:
# [7 * 3 * 4, 1 * 3 * 4, 1 * 7 * 4, 1 * 7 * 3]

def get_products(arrays):
    res = []
    for x in range(len(arrays)):
        total = 0
        for i, v in enumerate(arrays):
            if i == x:
                continue
            else:
                if total != 0:
                    total *= v
                else:
                    total += v
        res.append(total)
    return res
        
print(get_products([1, 7, 3, 4]))