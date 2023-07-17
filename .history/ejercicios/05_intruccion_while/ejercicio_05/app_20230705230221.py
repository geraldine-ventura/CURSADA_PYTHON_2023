import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


"""
Enunciado:
Al presionar el botón ‘Validar letra’, mediante prompt solicitar al usuario que ingrese una letra. 
Se deberá validar que la letra sea 'U', 'V' o 'R' (en mayusculas) 
En caso no coincidir con ninguna de las letras, volverla a solicitar hasta que la condición se cumpla
"""


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_validar_letra = customtkinter.CTkButton(
            master=self, text="Ingresar", command=self.btn_validar_letra_on_click
        )
        self.btn_validar_letra.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_letra_on_click(self):
        letra = prompt(
            title="validar", prompt="ingrese una letra: 'U', 'V' o 'R'"
        ).upper()

        while letra == "U" and letra == "V" and letra == "R":
            letra = prompt(
                title="validar", prompt="Error, ingrese una letra: 'U', 'V' o 'R' "
            )

    alert(title="veificacion", message="la letra fue validada correctamnete")


if __name__ == "__main__":
    app = App()
    app.mainloop()
