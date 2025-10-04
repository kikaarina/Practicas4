def suma(a, b):
    try:
        # Convertir a float para manejar numeros enteros y decimales
        a = float(a)
        b = float(b)
        return a + b
    except ValueError:
        return "error"