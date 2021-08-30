T = int(input())
L = []
for i in range(T):
    n = input()
    L.append(int(n))
L.sort()
for item in L:
    print(item)