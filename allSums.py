def allSumsDP(arr):
    n = len(arr)
    result_set = set()

    dp = [[False] * (sum(arr) + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(sum(arr) + 1):
            dp[i][j] = dp[i - 1][j] or (arr[i - 1] <= j and dp[i - 1][j - arr[i - 1]])

    for j in range(sum(arr) + 1):
        if dp[n][j]:
            result_set.add(j)

    return result_set