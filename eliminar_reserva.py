from conexion import SessionLocal
from modelos import Reserva

def cancelar_reserva(id_reserva):
    """Elimina la reserva y libera la sala. Devuelve True si se canceló."""
    with SessionLocal.begin() as session:
        reserva = session.get(Reserva, id_reserva)

        if reserva is None:
            print("No existe una reserva con ese ID.")
            return False

        reserva.sala.disponible = True
        session.delete(reserva)

    print("Reserva cancelada. La sala vuelve a estar disponible.")
    return True 