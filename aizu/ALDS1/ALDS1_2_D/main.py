from ShellSort import ShellSort

if __name__ == '__main__':
    A = []
    N = 0
    N = int(input())
    for i in range(N):
        A.append(int(input()))
    sort = ShellSort()
    ret = sort.sort(A, N)