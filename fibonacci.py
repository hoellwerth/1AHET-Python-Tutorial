def fibonacci(start, end):
  temp = 0
  for i in range(start, end+1):
    temp = i + temp
    print(f"{i}: {temp}")

fibonacci(1, 10)