T = int(input())
for t in range(1, T+1):
    m, n = map(int, input().split())
    # m rows, n columns

    matrix = []

    for i in range(m):
        ln = list(map(int, input().split()))
        matrix.append(ln)

    transposed_matrix = [['']*m for i in range(n)]
    
    for i in range(n):
        for j in range(m):
            transposed_matrix[i][j] = matrix[j][i]
    
    custom_matrix = [['']* m for i in range(n)]
    for i in range(n):
        for j in range(m):
            custom_matrix[i][j] = transposed_matrix[i][m-j-1]

    moves = 0
    for i in range(n):
        boxes = 0
        for j in range(m):
            if custom_matrix[i][j]:
                moves += (j - boxes)
                boxes += 1
    
    print(moves)