import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

"""
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera 
hasta que presione el botón Cancelar (en el prompt). 
Luego determinar el máximo y el mínimo 
e informarlos en los cuadros de textos txt_maximo y txt_minimo respectivamente

"""


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.txt_minimo = customtkinter.CTkEntry(master=self, placeholder_text="Mínimo")
        self.txt_minimo.grid(row=0, padx=20, pady=20)

        self.txt_maximo = customtkinter.CTkEntry(master=self, placeholder_text="Máximo")
        self.txt_maximo.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(
            master=self,
            text="Comenzar Ingreso",
            command=self.btn_comenzar_ingreso_on_click,
        )
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")

    def btn_comenzar_ingreso_on_click(self):
        flag_continuar = True
        num_max = None
        num_min = None

        while flag_continuar:
            numeros_str = prompt(
                title="solicitud", prompt="Ingrese los numeros que desea: "
            )
            if numeros_str == None:
                flag_continuar = False
            else:
                numero_num = int(numeros_str)

                if num_max == None or numero_num > num_max:
                    num_max = numero_num

                if num_max == None or numero_num < num_min:
                    num_min = numero_num

    self.txt_minimo.insert(0, num_min)
    self.txt_minimo.delete(0, 10000000)


if __name__ == "__main__":
    app = App()
    app.mainloop()
