def solution(H):
    n = len(H)
    stack = [0]
    brojac = 0

    for i in range(0, n):
        while H[i] < stack[-1]:
            stack.pop()

        if H[i] == stack[-1]:
            continue
        elif H[i] > stack[-1]:
            stack.append(H[i])
            brojac += 1

    return brojac

"""
if __name__ == '__main__':
    print("Test 1:", solution([8, 8, 5, 7, 9, 8, 7, 4, 8]))
    print("Test 2:", solution([8, 15, 17, 25, 23, 20, 25, 4, 7, 15, 10, 10]))
    print("Test 3:", solution([10]))
    print("Test 4:", solution([]))

"""
