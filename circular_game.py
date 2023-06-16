n=6
k=5

def remove_zeros(nums):
    for i in nums:
        if i==0:
            nums.remove(i)
    return nums

players=[i for i in range(0,n+1)]
N=len(players)
index=0
start=0



while len(players)!=1:

    
    players.remove(players[index])
    index+=k-1
    index=index%len(players)

print(players[0])