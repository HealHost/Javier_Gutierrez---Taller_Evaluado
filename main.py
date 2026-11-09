from crear_tabla import crear_tablas
from crear_sala import insertar_sala
from consulta_sala import consultar_salas
from crear_reserva import registrar_reserva
from consulta_reserva import consultar_reservas
from eliminar_reserva import cancelar_reserva


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje).strip())
        except ValueError:
            print("Debe ingresar un número entero válido.")


def menu():
    crear_tablas()

    while True:
        print("\n===== RESERVA DE SALAS=====")
        print("1. Registrar sala")
        print("2. Consultar salas")
        print("3. Registrar reserva")
        print("4. Consultar reservas")
        print("5. Cancelar reserva")
        print("0. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre de la sala: ")
            capacidad = leer_entero("Capacidad: ")
            insertar_sala(nombre, capacidad)

        elif opcion == "2":
            consultar_salas()

        elif opcion == "3":
            estudiante = input("Nombre del estudiante: ")
            sala_id = leer_entero("ID de la sala: ")
            fecha = input("Fecha (AAAA-MM-DD): ")
            registrar_reserva(estudiante, sala_id, fecha)

        elif opcion == "4":
            consultar_reservas()

        elif opcion == "5":
            id_reserva = leer_entero("ID de la reserva a cancelar: ")
            cancelar_reserva(id_reserva)

        elif opcion == "0":
            print("Hasta luego.")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    try:
        menu()
    except (KeyboardInterrupt, EOFError):
        print("\nPrograma finalizado.")