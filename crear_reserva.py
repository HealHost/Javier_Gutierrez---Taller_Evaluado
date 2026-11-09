from datetime import datetime
from conexion import SessionLocal
from modelos import Sala, Reserva

def fecha_valida(fecha):
    if len(fecha) != 10:
        return False
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def registrar_reserva(estudiante, sala_id, fecha):
    estudiante = estudiante.strip()
    fecha = fecha.strip()

    if not estudiante:
        print("El nombre del estudiante es obligatorio")
        return None

    if len(estudiante) > 100:
        print("El nombre del estudiante no puede superar los 100 caracteres")
        return None

    if not fecha_valida(fecha):
        print("Ingrese la fecha correctamente(por ejemplo 2026-11-10)")
        return None

    with SessionLocal.begin() as session:
        sala = session.get(Sala, sala_id)

        if sala is None:
            print("No existe una sala con ese ID.")
            return None

        if not sala.disponible:
            print("La sala no está disponible.")
            return None

        reserva = Reserva(estudiante=estudiante, sala_id=sala.id, fecha=fecha)
        session.add(reserva)
        sala.disponible = False

    print(f"Reserva registrad--ID: {reserva.id}")
    return reserva.id