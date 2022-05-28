from uberx import UberX
from uberpool import UberPool
from uberblack import UberBlack
from ubervan import UberVan
from user import User
from driver import Driver
from trip import Trip

import random

if __name__ == "__main__":

    program_activated = 0
    payment_process = 0
    aux = True

    # Inicio: Menu UBER

    while program_activated != 4:
        print("---- Menu principal de UBER ----\n")
        program_activated = int(input("1. Agregar usuario\n2. Agregar conductor\n3. Solicitar servicio\n4. Salir\nOpcion: "))

        if program_activated == 1:

            # Entrada de datos

            name_aux = input("Ingrese nombre del usuario: ")
            document_aux = input("Ingrese numero de identificacion: ")
            email_aux = input("Ingrese email: ")
            password_aux = input("Ingrese una contrasena: ")

            # Instanciando usuario (Solo 1 vez)

            User1 = User(1, name_aux, document_aux, email_aux, password_aux)
            print(f'\nBienvenido {User1.get_name()}\n')

        elif program_activated == 2:

            # Entrada de datos

            name_aux = input("Ingrese nombre del usuario: ")
            document_aux = input("Ingrese numero de identificacion: ")
            email_aux = input("Ingrese email: ")
            password_aux = input("Ingrese una contrasena: ")
            brand_car = input("Ingrese la marca del vehiculo: ")
            model_car = input("Ingrese modelo del vehiculo: ")
            license_aux = input("Ingrese codigo de la licencia: ")

            while aux == True:
                tipo_uber = int(input("Ingrese el tipo de Uber\n1. UberX\n2. UberPool\nOpcion: "))
            
                # Instanciando conductor y vehiculo UBER (Solo 1 vez) (UberX o UberPool)

                if tipo_uber == 1:
                    Driver1 = UberX(1, license_aux, Driver(1, name_aux, document_aux, email_aux, password_aux), 4, brand_car, model_car)
                    aux = False
                elif tipo_uber == 2:
                    Driver1 = UberPool(1, license_aux, Driver(1, name_aux, document_aux, email_aux, password_aux), 4, brand_car, model_car)
                    aux = False
                else:
                    print("\nIngrese una opcion valida\n")

            print(f'Conductor {Driver1.driver.get_name()} registrado con exito!\n')
            aux = True

        elif program_activated == 3:
            route_start = input("Ingrese ubicacion de origen: ")
            route_end = input("Ingrese ubicacion de destino: ")

            while payment_process != 4:
                payment_process = int(input("\n--- Metodo de pago ---\n1. Efectivo\n2. Tarjeta\n3. PayPal\n4. Cancelar servicio\nOpcion: "))
                if payment_process == 1:
                    pass
                elif payment_process == 2:
                    pass
                elif payment_process == 3:
                    pass
                else:
                    print("\nIngrese una opcion valida\n")

                
    
    """
    Car1 = UberX(1, "AMS321", Driver(1, "Carlos Silva", "V25643915", "Caensi95@gmail.com", 1234), 4, "Chery", "Arauca")
    print(f'{Car1.driver.get_driver()} El vehiculo Uber es un {Car1.brand} {Car1.model} ')

    Car2 = UberVan(2, "FTS123", Driver(2, "Luz Mar", "V5348227", "ramluzmar25@gmail.com", 5678), 6, "Daihatsu", "Terios")
    print(vars(Car2))"""