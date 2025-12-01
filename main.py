from src.gestor import GestorAvenida

if __name__ == "__main__":
    print("Inicio de la Simulación/App")
    gestor = GestorAvenida()
    gestor.actualizar_vehiculo(1, pos=(10, 13), vel=90)
    gestor.actualizar_vehiculo(2, pos=(11, 12), vel=50)

    # Reporte manual
    gestor.reportar_incidente("choque", (11, 11))

    print("\nFin de la aplicación.")
