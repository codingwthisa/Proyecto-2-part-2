from CRUD.actualizarDatos import actualizar_factura
from CRUD.registro import crear_sistema_facturacion, crear_factura
from CRUD.buscarCedula import buscar_por_cedula
from CRUD.guardarDatos import cargar_datos
from CRUD.guardarDatos import guardar_datos
from CRUD.actualizarDatos import actualizar_factura
from CRUD.eliminarDatos import eliminar_cliente
from ui.menu_main import mostrar_menu
from prettytable import PrettyTable

def main():
    clientes = cargar_datos()
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            productos_control, antibioticos, clientes = crear_sistema_facturacion()
            crear_factura(clientes[-1], productos_control + antibioticos)
            guardar_datos(clientes)
        
        elif opcion == "2":
            buscar_por_cedula(clientes)
        
        elif opcion == "3":
            actualizar_factura(clientes)
        
        elif opcion == "4":   
            print("Lista de clientes:")
            table = PrettyTable()
            table.field_names = ["Nombre", "Cédula"]
            for cliente in clientes:
                table.add_row([cliente.nombre, cliente.cedula])
            print(table)
            cedula = input("Ingrese la cédula del cliente que desea eliminar: ")
            eliminar_cliente(clientes, cedula)
        
        elif opcion == "5":
            break
        else:
            print("Opción inválida, por favor intente de nuevo")

main()
