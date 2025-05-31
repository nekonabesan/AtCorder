from SelectionSort import SelectionSort

if __name__ == '__main__':
    A = []
    N = 0
    N = int(input())
    console = input().split()
    for i in range(len(console)):
        A.append(int(console[i]))
    sort = SelectionSort()
    ret = sort.sort(A, N)