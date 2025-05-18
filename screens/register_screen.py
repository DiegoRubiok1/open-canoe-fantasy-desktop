from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from requests import post
from config import BASE_URL, TOKEN

class RegisterScreen(Screen):
    def register(self):
        # Aquí iría la lógica para registrar al usuario
        # Por ejemplo, enviar una solicitud POST al servidor con los datos del formulario
        pass