def fibonnaci(end, start = 0):
    a, b = 0, 1

    for _ in range(start, end):
        print(a, end=" \n")
        a,b = b, a + b

fibonnaci(10)