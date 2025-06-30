N =input().strip()
reversed_N = N[::-1].lstrip("0")
print(reversed_N)
if N==N[::-1]:
    print("True")
else:
    print("False")
