from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.home_screen import HomeScreen
from kivy.lang import Builder
import os

class OpenCanoeFantasyApp(App):
    def build(self):
        # Obtener la ruta del directorio actual
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Construir la ruta completa al archivo kv
        kv_path = os.path.join(current_dir, 'ui', 'home_screen.kv')
        
        # Cargar el archivo kv
        Builder.load_file(kv_path)
        
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        return sm

if __name__ == '__main__':
    OpenCanoeFantasyApp().run()