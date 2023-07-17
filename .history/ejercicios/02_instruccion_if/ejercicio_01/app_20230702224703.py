import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: instrucion_if_01
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener contenido en la caja de texto txt_edad, transformarlo en número, 
si coincide con el valor 18, mostrar el mensaje “Usted tiene 18 años” utilizando el Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        edad_str= self.txt_edad.get()
        edad_num= int(edad_str)
 self.txt_Edad.delete(0,100)
            self.txt_Edad.insert(0,edad_num)
        

        if (edad_num==18):
            mensaje = "Usted tiene {0} años".format(edad_str)
            alert( title="edad",message=mensaje)
            
        else:
            mensaje1 = "Ingrese otra edad"
            alert( title="edad",message=mensaje1)
           




if __name__ == "__main__":
    app = App()
    app.mainloop()