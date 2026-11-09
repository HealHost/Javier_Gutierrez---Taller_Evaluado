from conexion import SessionLocal
from modelos import Sala

def insertar_sala(nombre, capacidad):
    nombre = nombre.strip()

    if not nombre:
        print("El nombre de la sala es obligatorio.")
        return None

    if len(nombre) > 100:
        print("El nombre no puede superar los 100 caracteres.")
        return None

    # Conversión segura del parámetro recibido
    try:
        capacidad = int(capacidad)
    except (ValueError, TypeError):
        print("Debe ingresar un número entero válido.")
        return None

    if capacidad <= 0:
        print("La capacidad de la sala debe ser mayor a 0.")
        return None

    with SessionLocal() as session:
        sala = Sala(nombre=nombre, capacidad=capacidad)
        session.add(sala)
        session.commit()

    print(f"Sala registrada. ID: {sala.id}")
    return sala.id