import logging
import requests
import shutil
from kivymd.toast import toast
from kivymd.uix.button import MDRaisedButton
import json
import os
from fpdf import FPDF
from kivy.network.urlrequest import UrlRequest

def buscarUsuario(self):
    def on_success(req, response):
        logging.info(f"success {req} - {response}")
        if response.get('success', False):
            usuario = response
            self.Data.ids.usuario.text = usuario.get('UserName', '')
            self.Data.ids.busEmail.text = usuario.get('email', '')
            self.Data.ids.busPassword.text = usuario.get('password', '')
            self.screen_manager.current = "data"
            self.Data.ids.Spin.active = False
        else:
            self.Data.ids.usuario.text = "Usuario no encontrado"
            self.Data.ids.busEmail.text = ""
            self.Data.ids.busPassword.text = ""
            self.Data.ids.Spin.active = False 
    

    def on_failure(req, result):
        logging.info(f"failure {req} - {result}")
        toast("Usuario no encontrado")
        logging.error("Usuario no encontrado")
        self.Data.ids.usuario.text = ""
        self.Data.ids.busEmail.text = ""
        self.Data.ids.busPassword.text = ""
        self.Data.ids.Spin.active = False 

    def on_error(req, result):
        logging.info(f"error {req} - {result}")
        toast("Usuario no encontrado")
        logging.error("Usuario no encontrado")

    buscar = self.Data.ids.busUsers.text

    if buscar:
        self.Data.ids.Spin.active = True
        try:
            url = 'http://localhost:8000/buscarUsuarios'
            data = json.dumps({'busUsers': buscar})
            logging.info(f"REQUEST: {data}")
            headers = {'Content-type': 'application/json'}
            UrlRequest(url=url, on_success=on_success, on_failure=on_failure, on_error=on_error, timeout=3, req_headers=headers, req_body=data)
        except Exception as error:
            logging.error(f"Error de conexión: {error}")
            toast("Error de conexión al servidor")
    else:
        toast("Usuario no encontrado")
        logging.warning("RESPONSE: Usuario no encontrado")



def descargarUsuarioPDF(self):
    try:
        usuario = self.Data.ids.usuario.text 
        email = self.Data.ids.busEmail.text 
        password = self.Data.ids.busPassword.text 
        if usuario and email and password:
            filename = f"{usuario}.pdf"  
            folder_path = "C:/Users/sopor/Downloads/Usuarios/"
            filepath = os.path.join(folder_path, filename)
            
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                logging.info(f"Carpeta {folder_path} creada.")
                toast("Espere un momento...")
                
            # Si el archivo existe, eliminarlo para reemplazarlo
            if os.path.exists(filepath):
                os.remove(filepath)
                logging.info(f"RESPONSE: El archivo {filename} ya existe. Se sobrescribirá con nuevos datos.")
            
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt=f"Usuario: {usuario}", ln=True)
            pdf.cell(200, 10, txt=f"Correo: {email}", ln=True)
            pdf.cell(200, 10, txt=f"Contraseña: {password}", ln=True)
            
            logging.info(f"Valores descargados: Usuario={usuario}, Correo={email}, Contraseña={password}")
            
            pdf.output(filename)
            shutil.move(filename, filepath)
            toast("Usuario Descargado exitosamente")
        else:
            toast("El usuario no pudo ser descargado")
            logging.warning("RESPONSE: El usuario no pudo ser descargado")
    except Exception as e:
        logging.error(f"RESPONSE ERROR: {e}")