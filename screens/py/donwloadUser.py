import logging
import requests
import shutil
from kivymd.toast import toast
from kivymd.uix.button import MDRaisedButton
import json
import os
from fpdf import FPDF
from kivy.network.urlrequest import UrlRequest

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
                logging.info(f"FOLDER : {folder_path} SUCCESSFULLY CREATED.")
                # toast("Espere un momento...")
                
            # Si el archivo existe, eliminarlo para reemplazarlo
            if os.path.exists(filepath):
                os.remove(filepath)
                logging.info(f"RESPONSE: El archivo {filename} ya existe. Se sobrescribirá con nuevos datos.")
            
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            
            ruta_imagen = "img/Iconci24.png"  # Ajusta la ruta de la imagen
            pdf.image(ruta_imagen, x=10, y=10, w=70)
            # Ajusta las coordenadas y dimensiones de la imagen
            
            
            pdf.cell(200, 10, txt="DATOS USUARIO", ln=True, align="C")
            
                       
            # Define las coordenadas para cada elemento
            pos_x_usuario = 80
            pos_y_usuario = 30

            pos_x_correo = 80
            pos_y_correo = 45

            pos_x_contraseña = 80
            pos_y_contraseña = 60
            
            # Dibuja los elementos en las coordenadas especificadas
            pdf.text(pos_x_usuario, pos_y_usuario, f"Usuario: {usuario}")
            pdf.text(pos_x_correo, pos_y_correo, f"Correo: {email}")
            pdf.text(pos_x_contraseña, pos_y_contraseña, f"Contraseña: {password}")
            
            logging.info(f"Valores descargados: Usuario={usuario}, Correo={email}, Contraseña={password}")
            
            pdf.output(filename)
            shutil.move(filename, filepath)
            toast("Usuario Descargado exitosamente")
        else:
            toast("El usuario no pudo ser descargado")
            logging.warning("RESPONSE: El usuario no pudo ser descargado")
    except Exception as e:
        logging.error(f"RESPONSE ERROR: {e}")
