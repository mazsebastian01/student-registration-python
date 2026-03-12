# lista donde se guardaran los estudiantes
estudiantes = []
# Función para registrar estudiantes
def registrar_estudiantes():
    while True:
        nombre = input("Nombre del estudiante: ")
        estudiantes.append(nombre)
        continuar = input("¿desea agregar otro estudiante? (si/no): ")
        if continuar.lower() != "si":
            break
# función para mostrar estudiantes
def mostrar_estudiantes():
    print("Lista de estudiantes registrados: ")
    for estudiante in estudiantes:
        print("-" + estudiante)

registrar_estudiantes()
mostrar_estudiantes()

estudiantes = {} #diccionario donde se guardan los estudiantes
#registrar materias y notas
def registrar_materia():
    nombre = input("Nombre del estudiante: ")
    if nombre not in estudiantes:
        estudiantes[nombre] = {}

    materia = input("Nombre de la materia: ")
    nota = float(input("Nota de la materia: "))
    estudiantes[nombre][materia] = nota
    print("Materia y notas registradas correctamente")

#mostrar datos guardados
def mostrar_datos():
    for estudiante, materias in estudiantes.items():
        print(f"\nEstudiante: {estudiante}")

        for materia, nota in materias.items():
            print(f"{materia}: {nota}")

#menu
while True:
    print("\n1. Registrar materia y nota")
    print("2. Mostrar informacion")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        registrar_materia()
    elif opcion == "2":
        mostrar_datos()
    elif opcion == "3":
        break
