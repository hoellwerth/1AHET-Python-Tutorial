def fibonacci(start, end):      # Definiert fibonacci Funktion mit Parameter start und end
  temp = 0                      # Setzt temporäre variable auf 0
  for i in range(start, end+1): # Wiederhole von start bis end+1 (end ist inkludiert)
    temp += i                   # Addiert i zu temp
    print(f"{i}: {temp}")       # Gibt i und temp in formatierten string aus
                                # 
fibonacci(1, 10)                # Führt fibonacci Funktion mit start=1 und end=10 aus