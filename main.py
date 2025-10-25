def isOdd(value):
    if isinstance(value, bool):
        return False
    if isinstance(value, int):
        if value % 2 != 0:
            return True
        else:
            return False
    else:
        return False
if __name__ == "__main__":
    N = input()
    num = isOdd(N)
    print(num)
