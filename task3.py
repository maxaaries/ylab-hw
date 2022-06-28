
def zeros(n):
    return 0 if int(n//5) < 1 else int(n//5) + int(zeros(n//5))


n = int(input())
print(zeros(n))
