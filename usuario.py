class Usuario:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.tareas = []

    def agregarTarea(self, tarea):
        self.tareas.append(tarea)

    def listarTareas(self):
        for tarea in self.tareas:
            if tarea.estaLista():
<<<<<<< HEAD
                print(f"[X] {tarea.obtenerNombre()}" )
                print(f"[ ] {tarea.obtenerNombre()}" )
=======
                print(f"[X] {tarea.obtenerNombre()}" )
>>>>>>> a2496f638a4510ea5d6f1dd1746a9e9b1e732687
