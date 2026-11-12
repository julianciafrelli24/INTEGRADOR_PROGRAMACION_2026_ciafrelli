import Menu
import Gestion_stock
def main():
    Gestion_stock.inicializar()
    opcion = 0

    while opcion != 4:
        opcion = Menu.mostrar_menu()
        if opcion == 1:
            Gestion_stock.cargar_stock()
        elif opcion == 2:
            Gestion_stock.mostrar_stock()
        elif opcion == 3:
            print("Categorias disponibles:")
            print("enlatados, frutas, congelados, panaderia")
            categoria = input("Ingrese la categoria: ").lower()

            if categoria in Gestion_stock.stock_cantidades:
                lista = Gestion_stock.stock_cantidades[categoria]
                Gestion_stock.contar(lista)
            else:
                print("la categoria incorrecta")
        elif opcion == 4:
            print("Saliendo")
        else:
            print("no se puede")

if __name__ == "__main__":
    main()
    
        
        