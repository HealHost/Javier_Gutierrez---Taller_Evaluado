from sqlalchemy import select
from conexion import SessionLocal
from modelos import Sala

def consultar_salas():
    with SessionLocal() as session:
        salas = session.scalars(select(Sala).order_by(Sala.id)).all()

        if not salas:
            print("No hay salas registradas.")
            return

        print("\n--- LISTADO DE SALAS ---")

        for sala in salas:
            estado = "Disponible" if sala.disponible else "No disponible"
            print(
                f"ID: {sala.id} | "
                f"Nombre: {sala.nombre} | "
                f"Capacidad: {sala.capacidad} | "
                f"Estado: {estado}"
            )