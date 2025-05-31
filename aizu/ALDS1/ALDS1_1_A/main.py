from InsertSort import InsertSort

if __name__ == '__main__':
    A = []
    N = 0
    N = int(input())
    console = input().split()
    for i in range(len(console)):
        A.append(int(console[i]))
    sort = InsertSort()
    sort.trace(A)
    ret = sort.sort(A, N)

    
