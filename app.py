import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Julieta
apellido: Digifico
---
Ejercicio: parcial
---
Enunciado:
De 5  mascotas que ingresan a una veterinaria se deben tomar y validar los siguientes datos.

Nombre
Tipo (gato ,perro o exotico)
Peso ( entre 10 y 80)
Sexo( F o M  )
Edad(mayor a 0)

Pedir datos por prompt y mostrar por print, se debe informar:
Informe A- Cuál fue el sexo menos ingresado (F o M)
Informe B- El porcentaje de mascotas que hay por tipo (gato ,perro o exotico)
Informe C- El nombre y tipo de la mascota menos pesada
Informe D- El nombre del perro más joven
Informe E- El promedio de peso de todas las mascotas

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        CANTIDAD_ITERACIONES = 5
        contador_sexo_f = 0
        contador_sexo_m = 0
        contador_gatos = 0
        contador_perros = 0
        contador_exoticos = 0
        acumulador_mascotas = 0
        peso_mascota_menos_pesada = 81
        nombre_mascota_menos_pesada = ""
        tipo_mascota_menos_pesada = ""
        edad_perro_joven = 0
        nombre_perro_joven = ""
        acumulador_peso_total = 0

        for i in range(CANTIDAD_ITERACIONES):
            nombre = prompt("Nombre", "Ingrese el nombre de su mascota")
            while nombre == None or nombre == "":
                nombre = prompt("Error", "Por favor, ingrese el nombre correctamente")

            tipo = prompt("Tipo", "Indicar si su mascota es un gato, perro o exotico").lower()
            while tipo != "gato" and tipo != "perro" and tipo != "exotico":
                tipo = prompt("Error", "Por favor, indicar correctamente el tipo (gato, perro o exotico)")
            
            peso = prompt("Peso", "Ingrese el peso de su mascota")
            while not peso.isdigit() or int(peso) < 10 or int(peso) > 80:
                peso = prompt("Error", "Por favor, ingrese el peso nuevamente")

            sexo = prompt("Sexo", "Ingrese sexo de su mascota (F o M)").upper()
            while sexo != "F" and sexo != "M":
                sexo = prompt("Error", "Por favor, ingrese el sexo correctamente (F o M)")

            edad = prompt("Edad", "Ingrese la edad de su mascota")
            while not edad.isdigit() or int(edad) == 0:
                edad = prompt("Error", "Por favor, ingrese la edad correctamente")

            if sexo == "F":
                contador_sexo_f += 1
            if sexo == "M":
                contador_sexo_m += 1

            if tipo == "gato":
                contador_gatos += 1
            elif tipo == "perro":
                contador_perros += 1
            elif tipo == "exotico":
                contador_exoticos += 1

            if int(peso) < peso_mascota_menos_pesada:
                peso_mascota_menos_pesada = int(peso)
                nombre_mascota_menos_pesada = nombre
                tipo_mascota_menos_pesada = tipo

            acumulador_peso_total += int(peso)
            
            if tipo == "perro":
                if edad_perro_joven == 0 or int(edad) < edad_perro_joven:
                    edad_perro_joven = int(edad)
                    nombre_perro_joven = nombre

        acumulador_mascotas = contador_gatos + contador_perros + contador_exoticos
        porcentaje_gatos = (contador_gatos / acumulador_mascotas) * 100
        porcentaje_perros = (contador_perros / acumulador_mascotas) * 100
        porcentaje_exoticos = (contador_exoticos / acumulador_mascotas) * 100

        print("Porcentaje de gatos:", porcentaje_gatos)
        print("Porcentaje de perros:", porcentaje_perros)
        print("Porcentaje de exoticos:", porcentaje_exoticos)

        if contador_sexo_f < contador_sexo_m:
             sexo_menos_ingresado = "F"
        elif contador_sexo_m < contador_sexo_f:
            sexo_menos_ingresado = "M"
        else:
            sexo_menos_ingresado = "Ambos sexos se ingresaron igualmente"

        print("El sexo menos ingresado fue:", sexo_menos_ingresado)

        print("La mascota menos pesada es:", nombre_mascota_menos_pesada)
        print("Tipo:", tipo_mascota_menos_pesada)
        print("Peso", peso_mascota_menos_pesada)

        if nombre_perro_joven != "":
             print("El perro más joven es:", nombre_perro_joven)
             print("Edad:", edad_perro_joven)
        else:
            print("No se ingresaron perros")

        promedio_peso_mascotas = acumulador_peso_total / CANTIDAD_ITERACIONES
        print("El promedio de peso de todas las mascotas es:", promedio_peso_mascotas)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()