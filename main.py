from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.home_screen import HomeScreen
from screens.register_screen import RegisterScreen
from utils.ui_loader import load_kv_files
from kivy.core.text import LabelBase
from kivy.core.window import Window
from config import WINDOW_CONFIG
from kivy.utils import platform

class OpenCanoeFantasyApp(App):
    def build(self):
        if platform == 'android' or platform == 'ios':
            # En móviles, usar el tamaño del sistema
            Window.size = Window.system_size
        else:
            # En desktop, usar el tamaño configurado
            Window.size = (WINDOW_CONFIG['width'], WINDOW_CONFIG['height'])
            Window.minimum_width = WINDOW_CONFIG['minimum_width']
            Window.minimum_height = WINDOW_CONFIG['minimum_height']
            Window.resizable = WINDOW_CONFIG['resizable']
        
        # Registrar fuentes
        self.register_fonts()
        
        # Cargar todos los archivos .kv
        load_kv_files()
        
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(RegisterScreen(name='register'))
        return sm
    
    def register_fonts(self):
        LabelBase.register(name='goli',
                         fn_regular='assets/fonts/Goli-Regular.ttf',
                         fn_bold='assets/fonts/Goli-Bold.ttf')

if __name__ == '__main__':
    OpenCanoeFantasyApp().run()