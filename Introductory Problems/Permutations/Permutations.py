#%% md
# A permutation of integers 1,2,\ldots,n is called beautiful if there are no adjacent elements whose difference is 1.
# Given n, construct a beautiful permutation if such a permutation exists.
# Input
# The only input line contains an integer n.
# Output
# Print a beautiful permutation of integers 1,2,\ldots,n. If there are several solutions, you may print any of them. If there are no solutions, print "NO SOLUTION".
# Constraints
# 
# 1 \le n \le 10^6
# 
# Example 1
# Input:
# 5
# 
# Output:
# 4 2 5 3 1
# Example 2
# Input:
# 3
# 
# Output:
# NO SOLUTION
#%%
def inputs() -> int:
    n = int(input())
    return n
#%%
def outputs(n: int) -> str | list[int]:
    if n in [3, 2]:
        return "NO SOLUTION"
    else:
        arr = []
        for i in range(n -1, 0, -2):
            arr.append(i)

        for i in range(n, 0, -2):
            arr.append(i)
        return arr
#%%
n = inputs()
arr = outputs(n)
print(arr) if isinstance(arr, str) else print(*arr)