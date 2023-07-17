import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

"""
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar 5 números mediante prompt. 
Calcular la suma acumulada y el promedio de los números ingresados. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_promedio

"""


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.txt_suma_acumulada = customtkinter.CTkEntry(
            master=self, placeholder_text="Suma acumulada"
        )
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_promedio = customtkinter.CTkEntry(
            master=self, placeholder_text="Promedio"
        )
        self.txt_promedio.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(
            master=self,
            text="Comenzar Ingreso",
            command=self.btn_comenzar_ingreso_on_click,
        )
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")

    def btn_comenzar_ingreso_on_click(self):
        contador_num = 0
        suma_num = 0

        while contador_num < 5:
            numeros_num = int(
                prompt(title="pedir numeros", prompt="Ingrese 5 numeros: ")
            )

            suma_num += numeros_num
            contador_num += 1

        promedio_num = suma_num / contador_num

        mensaje = "la suma es {0} y el promdio es {1}".format(suma_num, promedio_num)
        print(mensaje)

        self.txt_suma_acumulada.delete(
            0, 10000000
        )  # Limpiar el contenido actual del widget
        self.txt_suma_acumulada.insert(0, str(suma_num))

        self.txt_promedio.delete(
            0, 1000000000
        )  # Limpiar el contenido actual del widget
        self.txt_promedio.insert(0, str(promedio_num))


"""'
        suma_num = str(suma_num)
        promedio_num = str(promedio_num)

        self.txt_suma_acumulada.get(suma_num)
        self.txt_promedio.get(promedio_num)
""" ""

if __name__ == "__main__":
    app = App()
    app.mainloop()