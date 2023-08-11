# Write a simple function to give result like below and the size will follow as the given value to the function.
# Example n = 5 Example n = 4
# 1**45678 1**4567
# 12**5678 12**567
# 123**678 123**67
# 1234**78 1234**7
# 12345**8

def solution(nbr):
    if not isinstance(nbr, int):
        return -1
    size = nbr + 4
    for i in range(nbr):
        res = []
        for x in range(1, size):
            if x - 2 == i or x - 3 == i:
                res.append("*")
            else:
                res.append(str(x))
        print("".join(res))

def main():
    userinput = input()
    if userinput.isnumeric():
        solution(int(userinput))
    else:
        return -1

main()
