# Entrenamiento
# Actividad: Sistema de validación de productos
# Definir variable
def pedir_entero_positivo(numero):
    while True :
        try :
            valor = int(input(numero))
            if valor >= 0:
                return valor
            else:
                print("Error:Digita un numero entero positivo.")
        except ValueError:
            print("Error:Digita un numero válido.")
# Nombre del producto
nombreproducto = input("Digita el nombre del producto: ")

# Precio unitario (convertimos a número decimal)
preciounitario = pedir_entero_positivo("Digita el precio unitario del producto: ")

# Cantidad de productos (convertimos a número entero)
cantidad = pedir_entero_positivo("Digita la cantidad de productos adquiridos: ")

# Porcentaje de descuento (convertimos a número decimal)
Descuento = pedir_entero_positivo("Digita el porcentaje de descuento (0-100): ")

while Descuento > 100:
    print("Error: el descuento no puede ser mayor a 100%.")
    Descuento = pedir_entero_positivo("Ingresa un descuento valido (0-100): ")

# Cálculos
costosindescuento = preciounitario * cantidad  # preciounitario * cantidad
montodescuento = (Descuento / 100) * costosindescuento  # cuánto se descuenta
costototal = costosindescuento - montodescuento  # total a pagar

# Resultados solo si no hay errores
print("Producto:", nombreproducto)
print("Costo sin descuento: $", costosindescuento)
print("Descuento aplicado:", Descuento, "%")
print(f"Costo total a pagar: ${costototal:.2f}")



