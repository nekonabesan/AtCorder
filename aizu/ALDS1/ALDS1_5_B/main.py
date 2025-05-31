from MergeSort import MergeSort

if __name__ == '__main__':
    A = []
    N = 0
    N = int(input())
    console = input().split()
    for i in range(len(console)):
        A.append(int(console[i]))
    sort = MergeSort()
    cnt,A = sort.merge_sort(A, N, 0, N)

    for i in range(len(A)):
        if i == len(A) - 1:
            print(A[i])
        else:
            print(A[i], end=' ')
    print(cnt)

