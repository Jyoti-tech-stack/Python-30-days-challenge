n = 5  # rows

for i in range(1, n + 1):
    # spaces print karo
    for j in range(1, n - i + 1):
        print(" ", end="")
    
    # stars print karo  
    for k in range(1, 2*i):
        print("*", end="")
    
    print()  # next line
