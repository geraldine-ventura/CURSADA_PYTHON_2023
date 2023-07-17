import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Enunciado:
Obtener el destino seleccionado en el combobox_destino, luego al presionar el botón 
‘Informar’ indicar mediante alert si en el destino hace frío o calor la mayoría 
de las estaciones del año.
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        destinos = ['Bariloche', 'Mar del plata', 'Cataratas', 'Ushuaia']
        self.combobox_destino = customtkinter.CTkComboBox(master=self, values=destinos)
        self.combobox_destino.grid(row=1, column=0, padx=20, pady=(10, 10))
        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        destino=self.combobox_destino.get()
        mensaje="Hace frio la maryor parte del año"
        mensaje1="Hace calor la mayor parte del año"
        match(destino):
            case 'Bariloche':
                alert(title="info",message=mensaje)
            case 'Mar del plata':
                alert(title="info",message=mensaje1)
            case 'Cataratas':
                alert(title="info",message=mensaje1)
            case 'Ushuaia':
                alert(title="info",message=mensaje)
    
    
if __name__ == "__main__":
    app = App()
    app.mainloop()