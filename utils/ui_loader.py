import os
from kivy.lang import Builder

def load_kv_files():
    """Carga todos los archivos .kv de la carpeta ui"""
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ui_dir = os.path.join(current_dir, 'ui')
    
    # Cargar primero el archivo de estilos
    styles_path = os.path.join(ui_dir, 'styles.kv')
    if os.path.exists(styles_path):
        Builder.load_file(styles_path)
    
    # Cargar el resto de archivos .kv
    for file in os.listdir(ui_dir):
        if file.endswith('.kv') and file != 'styles.kv':
            kv_path = os.path.join(ui_dir, file)
            Builder.load_file(kv_path)