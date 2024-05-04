import logging
import requests
import json
from kivymd.toast import toast

from kivy.network.urlrequest import UrlRequest

def login(self):
    def on_success(req, result):
        logging.info(f"success {req} - {result}")
        self.screen_manager.current = "newview"
        self.principal.ids.top_app_bar.right_action_items=[["logout", lambda x: self.confirm_logout()]]
        logging.info("VIEW: INGRESANDO A LA VISTA")
        logging.info("-----------------------------------------------------")
        

    def on_failure(req, result):
        logging.info(f"failure {req} - {result}")
        toast("Usuario y contraseña incorrectos")

    def on_error(req, result):
        logging.info(f"error {req} - {result}")
        toast("Usuario y contraseña incorrectos")

    email = self.Login.ids.validaInp.text
    password = self.Login.ids.inpPass.text

    if email != "" and password != "":
        self.Login.ids.spin.active = True
        try:
            url = 'http://localhost:8000/login'
            data = json.dumps({'email': email, 'password': password})
            logging.info(f"RESPONSE: {data}")
            headers = {'Content-type': 'application/json'}
            response = UrlRequest(url=url,on_success=on_success,on_failure=on_failure,on_error=on_error,timeout=3,req_headers=headers, req_body = data)
            # response = requests.post(url, data=data)
                
        #     if response.status_code == 200:
        #         json_response = response.json()                
        #         if json_response.get('success'):
        #             self.screen_manager.current = "newview"
        #             self.principal.ids.top_app_bar.right_action_items=[["logout", lambda x: self.confirm_logout()]]
        #             logging.info("VIEW: INGRESANDO A LA VISTA")
        #             logging.info("-----------------------------------------------------")
        #         else:
        #             toast("Correo electrónico o contraseña incorrectos")
        #     else:
        #         toast("Correo electrónico o contraseña incorrectos")
        except Exception as e:
            logging.error(f"Error de conexión: {e}")
            toast("Error de conexión al servidor")
    else:
        toast("Debe ingresar usario y contraseña")

