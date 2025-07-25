#%% md
# You are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.
# Input
# The only input line contains a string of n characters.
# Output
# Print one integer: the length of the longest repetition.
# Constraints
# 
# 1 \le n \le 10^6
# 
# Example
# Input:
# ATTCGGGA
# 
# Output:
# 3
#%%
def inputs() -> str:
    return input()
#%%
def outputs(dna: str) -> int:
    current = dna[0]
    highest = 0
    track = 1
    for c in dna[1:]:
        if current == c:
            track += 1
        else:
            current = c
            highest = max(track, highest)
            track = 1
    highest = max(track, highest)
    return highest
#%%
dna = inputs()
highest = outputs(dna)
print(highest)