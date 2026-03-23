def cuenta_regresiva(n):
    if n == 0:  # caso base
        print("Fin")
    else:       # caso recursivo
        print(n)
        cuenta_regresiva(n - 1)

cuenta_regresiva(5)