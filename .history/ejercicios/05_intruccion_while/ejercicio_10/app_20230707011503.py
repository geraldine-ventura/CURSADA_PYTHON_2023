import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

"""
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

"""


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self,
            text="Comenzar Ingreso",
            command=self.btn_comenzar_ingreso_on_click,
        )
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")

    def btn_comenzar_ingreso_on_click(self):
        flag_continuar = True
        acumulador_num_pos = 0
        contador_pos = 0
        acumulador_num_neg = 0
        contador_neg = 0
        contador_ceros = 0

        while flag_continuar=True:
            numero_str = prompt(title="calculos", prompt="Ingrese los num que deseé: ")

            if numero_str == None:
                flag_continuar = False
            else:
                numero_num = int(numero_str)
                if numero_num > 0:
                    acumulador_num_pos += numero_num
                    mensaje = f"La suma acumulada de los positivos:{acumulador_num_neg}"
                    contador_pos += 1
                    mensaje = (
                        f"Cantidad de números positivos ingresadoss:{contador_pos}"
                    )

                elif numero_num < 0:
                    acumulador_num_neg += numero_num
                    mensaje = f"La suma acumulada de los negativos:{acumulador_num_neg}"
                    contador_neg += 1
                    mensaje = f"Cantidad de números negativos ingresados:{contador_neg}"
                else:
                    contador_ceros += 1
                    mensaje = f"Cantidad de ceros:{contador_ceros}"

        resta_pos_neg = acumulador_num_pos - acumulador_num_neg
        mensaje = f" Diferencia entre la cantidad de los números positivos ingresados y los negativos: {resta_pos_neg}"

        alert(title="Datos pedidos", message=mensaje)


if __name__ == "__main__":
    app = App()
    app.mainloop()
