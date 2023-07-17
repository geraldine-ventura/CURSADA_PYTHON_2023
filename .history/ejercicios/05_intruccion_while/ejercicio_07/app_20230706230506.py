import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

"""
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera, 
hasta que presione el botón Cancelar (en el prompt). 
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
        flag_continuar = True
        contador_num = 0
        suma_num = 0  # acumulador de num

        while flag_continuar:
            numeros_str = prompt(
                title="pedir numeros", prompt="Ingrese los numeros que desea: "
            )
            if numeros_str == None:
                flag_continuar = False
                print("Saliste")

            else:
                numeros_num = int(numeros_str)
                suma_num += numeros_num
                contador_num += 1

        if contador_num != 0:
            promedio_num = suma_num / contador_num
        else:
            promedio_num = 0

        mensaje = "la suma es {0} y el promdio es {1}".format(suma_num, promedio_num)
        print(mensaje)

        self.txt_suma_acumulada.delete(0, 10000000)
        self.txt_suma_acumulada.insert(0, str(suma_num))

        self.txt_promedio.delete(0, 1000000000)
        self.txt_promedio.insert(0, str(promedio_num))


if __name__ == "__main__":
    app = App()
    app.mainloop()
