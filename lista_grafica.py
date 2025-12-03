from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class ListaApp(App):
    def build(self):
        self.title = "Aplicación Listas"
        self.lista = []
        layout = BoxLayout(
            orientation='vertical',
            padding = 20,
            spacing = 10
        )
        self.encabezado = Label(
            text="Gestor de Lista",
            font_size = "32sp",
            bold = True,
            color = [1,1,1,1],
            size_hint_y=0.2
        )
        layout.add_widget(self.encabezado)

        self.input = TextInput(
            hint_text="Escribe un elemento...",
            size_hint_y=0.15,
            font_size = "20sp",
            multiline = False,
            background_color = [0.2, 0.2, 0.2, 1],
            foreground_color = [1,1,1,1],
            padding=[10,10]
            )
        layout.add_widget(self.input)

        btn_agregar = Button(
            text="Agregar", 
            size_hint_y = 0.12,
            font_size = "20sp",
            background_color = [0.13, 0.55, 0.25, 1]
            )
        btn_agregar.bind(on_press=self.agregar)
        layout.add_widget(btn_agregar)

        btn_eliminar = Button(
            text="Eliminar", 
            size_hint_y = 0.15,
            font_size = "20sp",
            background_color = [0.60,0.15,0.15,1]
            )
        btn_eliminar.bind(on_press=self.eliminar)
        layout.add_widget(btn_eliminar)

        btn_eliminar_pos = Button(
            text="Eliminar por posición", 
            size_hint_y = 0.12,
            font_size = "20sp",
            background_color = [0.25,0.25,0.7,1]
            )
        btn_eliminar_pos.bind(on_press=self.eliminar_pos)
        layout.add_widget(btn_eliminar_pos)

        btn_buscar_pos = Button(
            text="Buscar por posición", 
            size_hint_y = 0.12,
            font_size = "20sp",
            background_color = [0.20,0.40,0.8,1]
            )
        btn_buscar_pos.bind(on_press=self.buscar_pos)
        layout.add_widget(btn_buscar_pos)

        btn_modificar = Button(
            text="Modificar por posición", 
            size_hint_y = 0.12,
            font_size = "20sp",
            background_color = [0.50,0.30,0.7,1]
            )
        btn_modificar.bind(on_press=self.modificar_posicion)
        layout.add_widget(btn_modificar)

        self.mensaje = Label(
            text="",
            size_hint_y=0.10,
            font_size = "18sp",
            color = [1,0.3,0.3,1]
            )
        layout.add_widget(self.mensaje)

        self.label = Label(
            text="(lista vacia)",
            size_hint_y=0.5,
            font_size = "22sp",
            color = [1,1,1,1]
            )
        layout.add_widget(self.label)
        return layout

    def actualizar(self):
        if self.lista:
            self.label.text = "\n".join(self.lista)
        else:
            self.label.text = "(lista vacia)"

    def agregar(self, instance):
        elemento = self.input.text.strip()
        if elemento:
            self.lista.append(elemento)
            self.input.text = ""
            self.mensaje.text= ""
            self.actualizar()

    def eliminar(self,instance):
        elemento=self.input.text.strip()
        if elemento in self.lista:
            self.lista.remove(elemento)
            self.input.text=""
            self.mensaje.text = ""
            self.actualizar()
        else:
            self.mensaje.text = "Elemento no encontrado"
            if len(self.lista)>0:
                self.actualizar
            else:
                self.label.text=""
    
    def eliminar_pos(self, instance):
        try:
            pos = int(self.input.text.strip())
            if 0<=pos < len(self.lista):
                self.lista.pop(pos)
                self.input.text = ""
                self.mensaje.text = ""
                self.actualizar()
            else:
                self.mensaje.text = 'Posición fuera de rango'
        except ValueError:
            self.mensaje.text = "Debes ingresar un número válido"

    def buscar_pos(self, instance):
        try:
            pos = int(self.input.text.strip())
            if 0<=pos < len(self.lista):
                elemento =  self.lista[pos]
                self.mensaje.text = f"Posición {pos}: {elemento}"
            else:
                self.mensaje.text = "Posición fuera de rango"
        except ValueError:
            self.mensaje.text = "Debes ingresar un número entero"
    
    def modificar_posicion(self, instance):
        try:
            datos = self.input.text.strip()
            if "," not in datos:
                self.mensaje.text = "Formato inválido. Usa: pos, nuevo"
                return
            posicion, nuevo_valor =  datos.split(",", 1)
            pos = int(posicion)

            if 0<=pos < len(self.lista):
                self.lista[pos] = nuevo_valor
                self.mensaje.text = f"Posición {pos} modificada"
                self.input.text = ""
                self.actualizar()
            else:
                self.mensaje.text = "Posición fuera de rango"
        except ValueError:
            self.mensaje.text = "La posicion debe ser un número"



if __name__ == "__main__":
    ListaApp().run()