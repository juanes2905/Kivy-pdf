import logging
import requests
from kivymd.toast import toast


def inserUsers(self):
    email = self.users.ids.InsertEmail.text
    user = self.users.ids.InsertUsername.text
    password = self.users.ids.InsertPassword.text

    if email and user and password :
        try:
            url = 'http://localhost:8000/CreateUsers'
            data = {'email': email, 'user': user, 'password': password}
            logging.info(f"RESPONSE: Insercion a la base de datos correcta : {data}")
            response = requests.post(url, data=data)

            if response.status_code == 200:
                json_response = response.json()
                if json_response.get('success'):
                    self.screen_manager.current = "newview"
                    self.principal.ids.top_app_bar.right_action_items=[["logout", lambda x: self.confirm_logout()]]
                    logging.info("VIEW: SALIENDO DE LA VISTA PARA RECARGAR DESPUES DE LA CREACION DEL USUARIOS NUEVO")
                    logging.info("-----------------------------------------------------")
                else:
                    toast("Diligenciar todos los campos")
                    logging.warning("RESPONSE: No se llenaron los datos correctamente")
            else:
                toast("Datos correctamente diligenciados")
                logging.info("RESPONSE: Datos correctamente diligenciados")
        except Exception as error:
            logging.error(f"Error de conexión: {error}")
            toast("Error de conexión al servidor")
    else:
        toast("Debe ingresar correo electrónico y contraseña")
        logging.warning("RESPONSE: Debe diligenciar los campos correctamente")