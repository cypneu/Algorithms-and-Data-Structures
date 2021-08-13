def knapsack(W, P, MaxW):
    n = len(W)
    F = [[0 for _ in range(MaxW + 1)] for _ in range(n)]

    for w in range(W[0], MaxW + 1):
        F[0][w] = P[0]
    

    for i in range(1, n):
        for w in range(1, MaxW + 1):
            if w < W[i]:
                F[i][w] = F[i - 1][w]
            else:
                F[i][w] = max(F[i - 1][w], F[i - 1][w - W[i]] + P[i])
 
 
    return F[n - 1][MaxW], F



def getSolution(F, W, P, i, w):
    if i == 0:
        if w >= W[0]:
            return [0]
        return []

    if w >= W[i] and F[i][w] == F[i - 1][w - W[i]] + P[i]:
        return getSolution(F, W, P, i - 1, w - W[i]) + [i]
    return getSolution(F, W, P, i - 1, w)



P = [10, 8, 4, 5, 3, 7]
W = [4, 5, 12, 9, 1, 13]
res, F = knapsack(W, P, 15)
print(res, getSolution(F, W, P, len(W) - 1, 15))