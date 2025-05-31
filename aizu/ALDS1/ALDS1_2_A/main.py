from BubbleSort import BubbleSort

if __name__ == '__main__':
    A = []
    N = 0
    N = int(input())
    console = input().split()
    for i in range(len(console)):
        A.append(int(console[i]))
    sort = BubbleSort()
    ret = sort.sort(A, N)

    
