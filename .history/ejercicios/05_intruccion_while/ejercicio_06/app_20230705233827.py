import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar 5 números mediante prompt. 
Calcular la suma acumulada y el promedio de los números ingresados. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_promedio

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_promedio = customtkinter.CTkEntry(master=self, placeholder_text="Promedio")
        self.txt_promedio.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        
        contador_num=int(0)
        suma_num=int(0)
        numeros=int(prompt(title="pedir numeros",prompt="Ingrese 5 numeros: "))
        
        while(contador_num<=5)
            suma_num += numeros
            contador_num += 1
        
        promedio_num= suma_num / contador_num
        
        suma_num=self.txt_suma_acumulada.get()
        promedio_num=self.txt_promedio.get() 
        
        #alert(title="rsultados",message="la suma es{},y el promedio es{}".format(suma_num,promedio_num))

    
if __name__ == "__main__":
    app = App()
    app.mainloop()
