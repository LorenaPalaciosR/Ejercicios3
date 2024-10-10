"""Ejercicio7
HAZ UN SOFTWARE TOTALMENTE LIBRE QUE RESUELVA UN PROBLEMA EN ESPECÍFICO
¿QUÉ DEBEN USAR?
-TODO LO QUE SE VIO EN CLASE HASTA EL TEMA DE POO (CLASES) NO SE ACEPTARÁ HERENCIA"""
class Estudiante:
    def __init__(self, nombre, calificaciones):
        self.nombre = nombre
        self.calificaciones = calificaciones

    def promedio(self):
        return sum(self.calificaciones) / len(self.calificaciones) if self.calificaciones else 0

    def estado(self):
        return "Aprobado" if self.promedio() >= 6 else "Reprobado"


class GestorEstudiantes:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, nombre, calificaciones):
        nuevo_estudiante = Estudiante(nombre, calificaciones)
        self.estudiantes.append(nuevo_estudiante)

    def mostrar_estudiantes(self):
        for estudiante in self.estudiantes:
            print(f"Nombre: {estudiante.nombre}, Promedio: {estudiante.promedio()}, Estado: {estudiante.estado()}")

    def estudiantes_aprobados(self):
        return [estudiante for estudiante in self.estudiantes if estudiante.estado() == "Aprobado"]

    def estudiantes_reprobados(self):
        return [estudiante for estudiante in self.estudiantes if estudiante.estado() == "Reprobado"]


# Ejemplo de uso
if __name__ == "__main__":
    gestor = GestorEstudiantes()
    
    gestor.agregar_estudiante("Alice", [6, 7, 8])
    gestor.agregar_estudiante("Bob", [4, 5, 5])
    gestor.agregar_estudiante("Charlie", [7, 8, 9])
    
    print("Lista de estudiantes:")
    gestor.mostrar_estudiantes()
    
    print("\nEstudiantes aprobados:")
    for est in gestor.estudiantes_aprobados():
        print(est.nombre)

    print("\nEstudiantes reprobados:")
    for est in gestor.estudiantes_reprobados():
        print(est.nombre)
