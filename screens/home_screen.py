from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from requests import post
from config import BASE_URL
from config import TOKEN

class HomeScreen(Screen):
    error_message = StringProperty('')  # Propiedad para el mensaje de error

    def login(self):
        password = self.ids.password.text
        email = self.ids.email.text

        data = {
            'email': str(email),
            'password': str(password)
        }

        try:
            response = post(f'{BASE_URL}/auth/login', json=data)
            response_data = response.json()  # Convierte la respuesta JSON a diccionario
            
            if response.status_code == 200:
                self.error_message = ''  # Limpiar mensaje de error

                TOKEN = response_data.get('token')
                username = response_data.get('user').get('username')


                
                print('username:', username)

            else:
                self.error_message = response_data.get('error', 'Error desconocido')

        except Exception as e:
            self.error_message = f"Error al conectar con el servidor: {e}"
    
    def register(self):
        self.manager.current = 'register'
