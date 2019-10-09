from GAUSS import gauss


def main():
    N = 6
    m = 1
    xx = [0.164, 0.328, 0.656, 0.984, 1.312, 1.640]
    x = [0] * N
    for i in range(N):
        x[i] = 1 / xx[i];
    print(x)
    y = [0.448, 0.432, 0.421, 0.417, 0.414, 0.412]
    POWERX = [0] * (2 * m);
    for k in range(2 * m):
        for i in range(N):
            POWERX[k] += pow(x[i], k + 1)
    SUMX = [[0] * (m + 1) for i in range(m + 1)]
    for l in range(m + 1):
        for j in range(m + 1):
            if j + l:
                SUMX[l][j] = POWERX[l + j - 1]
            else:
                SUMX[l][j] = N
    PRAW = [0] * (m + 1)
    for l in range(m + 1):
        for i in range(N):
            PRAW[l] += y[i] * pow(x[i], l)
    a = gauss(SUMX, PRAW, m + 1)
    print(a)

main()