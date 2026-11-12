stock_productos = {
    "enlatados": [],
    "frutas": [],
    "congelados": [],
    "panaderia": []
}
stock_cantidades = {
    "enlatados": [],
    "frutas": [],
    "congelados": [],
    "panaderia": []
}
def inicializar():
    for categoria in stock_productos:
        stock_productos[categoria] = []

    for categoria in stock_cantidades:
        stock_cantidades[categoria] = []

def cargar_stock():
    print("Categorias disponibles:")
    print("enlatados, frutas, congelados, panaderia")

    categoria = input("Ingrese la categoria: ").lower()

    if categoria in stock_productos:
        producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad: "))
        stock_productos[categoria].append(producto)
        stock_cantidades[categoria].append(cantidad)
        
        print("se cargo bien el producto.")
    else:
        print("no existe esa categoia.")

def mostrar_stock():
    print("---STOCK DE PRODUCTOS ---")

    for categoria in stock_productos:
        print("Categoria:", categoria)

        for i in range(len(stock_productos[categoria])):
            producto = stock_productos[categoria][i]
            cantidad = stock_cantidades[categoria][i]
            print(producto, "-", cantidad, "unidades")
