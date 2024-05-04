import logging
from kivy import platform
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.bottomsheet import MDGridBottomSheet
from kivymd.uix.card import MDCardSwipe
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.toast import toast
from kivy.properties import StringProperty
from screens.py.login import login
from screens.py.users import inserUsers
from screens.py.buscarUsuarios import buscarUsuario, descargarUsuarioPDF
from kivy.uix.label import Label
from kivymd.uix.spinner import MDSpinner
from kivy.metrics import dp
from kivy.clock import Clock

if platform == "win":
    Window.minimum_width = 520
    Window.minimum_height = 550
Window.size = (520, 550)

class SwipeToDeleteItem(MDCardSwipe):
    text = StringProperty()

class Tarea(MDApp):
    logging.info("PRUEBA DE COMMIT")
    logging.info("SI SUBI EL COMMIT")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dialog = None
        self.name_input = None
        self.password_input = None

    def build(self, **kwargs):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Orange"

    
        self.screen_manager = ScreenManager()

        self.Login = Builder.load_file("screens/kv/Login.kv")
        self.screen_manager.add_widget(self.Login)
        self.principal = Builder.load_file("screens/kv/principal.kv")
        self.principal.ids.contenedor.add_widget(self.screen_manager)
        
        self.newStyle = Builder.load_file("screens/kv/newstyle.kv")
        self.screen_manager.add_widget(self.newStyle)
        self.desplegar = Builder.load_file("screens/kv/desplegar.kv")
        self.screen_manager.add_widget(self.desplegar)
        self.Navegacion = Builder.load_file("screens/kv/navigation.kv")
        self.screen_manager.add_widget(self.Navegacion)
        self.users = Builder.load_file("screens/kv/usuarios.kv")
        self.screen_manager.add_widget(self.users)
        self.Data = Builder.load_file("screens/kv/data.kv")
        self.screen_manager.add_widget(self.Data)
        self.Lista = Builder.load_file("screens/kv/listUsers.kv")
        self.screen_manager.add_widget(self.Lista)

        self.name_input = self.Login.ids.validaInp
        self.password_input = self.Login.ids.inpPass

        return self.principal

    def on_start(self):
        self.newStyle.ids.md_list.add_widget(SwipeToDeleteItem(text="Aplicaciones"))
        self.newStyle.ids.md_list.add_widget(SwipeToDeleteItem(text="Navegacion"))
        self.newStyle.ids.md_list.add_widget(SwipeToDeleteItem(text="Datos"))
        self.newStyle.ids.md_list.add_widget(SwipeToDeleteItem(text="Buscar"))
        self.newStyle.ids.md_list.add_widget(SwipeToDeleteItem(text="Lista"))

    def remove_item(self, instance):
        self.newStyle.ids.md_list.remove_widget(instance)

    def listaView(self, item_text):
        Comunicado = "LOAD: CARGANDO LA VISTA"
        line = "-----------------------------------------------------"
        if item_text == "Aplicaciones":
            self.screen_manager.current = "desplegable"
            logging.info(Comunicado)
            logging.info(line)
            self.principal.ids.top_app_bar.right_action_items=[["arrow-left", lambda x: self.volver_a_newview()]]
        elif item_text == "Navegacion":
            self.screen_manager.current = "navegacionApp"
            logging.info(Comunicado)
            logging.info(line)
            self.principal.ids.top_app_bar.right_action_items=[["arrow-left", lambda x: self.volver_a_newview()]]
        elif item_text == "Datos":
            self.screen_manager.current = "InsertU"
            logging.info(Comunicado)
            logging.info(line)
            self.principal.ids.top_app_bar.right_action_items=[["arrow-left", lambda x: self.volver_a_newview()]]
        elif item_text == "Buscar":
            self.screen_manager.current = "data"
            logging.info(Comunicado)
            logging.info(line)
            self.principal.ids.top_app_bar.right_action_items=[["arrow-left", lambda x: self.volver_a_newview()]]
        elif item_text == "Lista":
            self.screen_manager.current = "Lista"
            logging.info(Comunicado)
            logging.info(line)
            self.principal.ids.top_app_bar.right_action_items=[["arrow-left", lambda x: self.volver_a_newview()]]

    def callback_for_menu_items(self, *args):
        toast(args[0])

    def show_example_grid_bottom_sheet(self):
        bottom_sheet_menu = MDGridBottomSheet()
        data = {
            "Facebook": "facebook",
            "YouTube": "youtube",
            "Twitter": "twitter",
            "Messenger": "facebook-messenger",
            "Camera": "camera",
        }
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0]: self.callback_for_menu_items(y),
                icon_src=item[1],
            )
        bottom_sheet_menu.elevation = 0
        bottom_sheet_menu.open()

    def logout(self, instance):
        if self.dialog:
            self.screen_manager.current = "login"
            self.dialog.dismiss()
            self.Login.ids.validaInp.text = ""
            self.Login.ids.inpPass.text = ""

    def confirm_logout(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="¿Está seguro de que desea cerrar sesión?",
                elevation=0,
                buttons=[
                    MDFlatButton(
                        text="Cancelar",
                        on_release=self.closeDialog
                    ),
                    MDFlatButton(
                        text="Aceptar",
                        on_release=self.logout
                    ),
                ],
            )
        self.dialog.open()

    def closeDialog(self, *args):
        if self.dialog:
            self.dialog.dismiss()

    def salir(self):
        match self.screen_manager.current:
            case "newview":
                if self.screen_manager.current == "newview":
                    self.screen_manager.current = "login"
                    logging.info("Cargando pantalla de inicio...")
                    self.principal.ids.top_app_bar.right_action_items=[]
                else:
                    self.screen_manager.current = "login"
                    self.principal.ids.top_app_bar.right_action_items=[]
                    logging.error("VIEW: Es imposible realizar esta acción")

    def ingresar(self):
        login(self)

    def InsersPruebas(self):
        inserUsers(self)

    def buscarUsuarios(self):
        buscarUsuario(self)
        
    def descargarUsuarioPDF(self):
        descargarUsuarioPDF(self)


    def volver_a_newview(self):
        self.screen_manager.current = "newview"
        logging.info("LOAD: Retornado a la vista INICIO")
        logging.info("-----------------------------------------------------")
        self.principal.ids.top_app_bar.right_action_items=[["logout", lambda x: self.confirm_logout()]]

if __name__ == "__main__":
    Tarea().run()