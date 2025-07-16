#%% md
# You are given all numbers between 1,2,\ldots,n except one. Your task is to find the missing number.
# Input
# The first input line contains an integer n.
# The second line contains n-1 numbers. Each number is distinct and between 1 and n (inclusive).
# Output
# Print the missing number.
# Constraints
# 
# 2 \le n \le 2 \cdot 10^5
# 
# Example
# Input:
# 5
# 2 3 1 5
# 
# Output:
# 4
# 
#%%
n = int(input())
arr: list[int] = list(map(int, input().split(" ")))
#%%
arr.sort()
for i in range(len(arr)-1):
    if arr[i]+1 != arr[i+1]:
        print(arr[i]+1)
        break
else:
    if arr[0]!=1:
        print(1)
    else:
        print(n)
#%%
arr