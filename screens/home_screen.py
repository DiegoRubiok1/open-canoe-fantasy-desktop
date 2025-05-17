from kivy.uix.screenmanager import Screen
from requests import post
from config import BASE_URL_DEVELOPMENT

class HomeScreen(Screen):
    def login(self):
        password = self.ids.password.text
        email = self.ids.email.text

        data = {
            'email': email,
            'password': password
        }

        try:
            response = post(f'{BASE_URL_DEVELOPMENT}/login', json=data)
            if response.status_code == 200:
                # Aquí puedes manejar la respuesta del servidor
                print("Login exitoso")
            else:
                print("Error en el login")
        except Exception as e:
            print(f"Error al conectar con el servidor: {e}")
