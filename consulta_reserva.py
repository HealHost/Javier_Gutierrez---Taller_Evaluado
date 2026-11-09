from sqlalchemy import select
from conexion import SessionLocal
from modelos import Reserva

def consultar_reservas():
    with SessionLocal() as session:
        reservas = session.scalars(select(Reserva).order_by(Reserva.id)).all()

        if not reservas:
            print("No hay reservas registradas.")
            return

        print("\n--- LISTADO DE RESERVAS ---")

        for reserva in reservas:
            print(
                f"ID: {reserva.id} | "
                f"Estudiante: {reserva.estudiante} | "
                f"Sala: {reserva.sala.nombre} | "
                f"Fecha: {reserva.fecha}"
            )