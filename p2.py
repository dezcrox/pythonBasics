try:
    while True:
        one = int(input("Primer numero: "))
        two = int(input("Segundo numero:"))
        sum = one + two
        if sum < 10:
            print (f"La suma es {sum}")
        else:
            break
except:
    pass
    print("Adios")


   