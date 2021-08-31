n=int(input())
for i in range(n):
    n1 = input()
    if n1[::-1] == n1:
        print("wins")
    else:
        print("loses")