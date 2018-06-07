try:
    height = input("Enter the height: ")
    while True:
        height = int(height)
        while height > 0:
            print("*" * height)
            height -= 1
        height = input("Ingresa otro valor")
except:
    print("No es numerico")