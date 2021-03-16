def solution(A, B):
    n = len(A)
    stack = []
    brojac = n

    for i in range(0, n):
        if B[i] == 1:
            stack.append(A[i])
        elif B[i] == 0:
            while stack:
                if stack[-1] > A[i]:
                    brojac -= 1
                    break
                else:
                    brojac -= 1
                    stack.pop()

    return brojac