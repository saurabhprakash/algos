# Longest Increasing Subsequence 

ar = [int(i) for i in input().split(' ')]
print ('ar=', ar)
n = len(ar)
res = [1 for i in range(0, n)]
i = 1
while i < n:
    j = 0
    while j < i:
        if ar[i] > ar[j]:
            res[i] = max(res[j] + 1, res[i]) 
        j += 1
    i += 1 

print (res)
print (max(res))
