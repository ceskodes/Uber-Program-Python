from card import Card
from cash import Cash
from paypal import Paypal
from uberx import UberX
from uberpool import UberPool
from uberblack import UberBlack
from ubervan import UberVan
from user import User
from driver import Driver
from trip import Trip
from route import Route

import random

if __name__ == "__main__":

    program_activated = 0
    payment_process = 0
    driver_exist = False
    user_exist = False
    aux = True

    # Inicio: Menu UBER

    while program_activated != 4:
        print("---- Menu principal de UBER ----\n")
        program_activated = int(input("1. Agregar usuario\n2. Agregar conductor\n3. Solicitar servicio\n4. Salir\nOpcion: "))

        if program_activated == 1:

            # Entrada de datos

            name_aux = input("\nIngrese nombre del usuario: ")
            document_aux = input("Ingrese numero de identificacion: ")
            email_aux = input("Ingrese email: ")
            password_aux = input("Ingrese una contrasena: ")

            # Instanciando usuario (Solo 1 vez)

            User1 = User(1, name_aux, document_aux, email_aux, password_aux)
            user_exist = True
            print(f'\nBienvenido {User1.get_name()}\n')

        elif program_activated == 2:

            # Entrada de datos

            name_aux = input("\nIngrese nombre del conductor: ")
            document_aux = input("Ingrese numero de identificacion: ")
            email_aux = input("Ingrese email: ")
            password_aux = input("Ingrese una contrasena: ")
            brand_car = input("Ingrese la marca del vehiculo: ")
            model_car = input("Ingrese modelo del vehiculo: ")
            license_aux = input("Ingrese codigo de la licencia: ")

            while aux == True:
                tipo_uber = int(input("\nIngrese el tipo de Uber\n1. UberX\n2. UberPool\nOpcion: "))
            
                # Instanciando conductor y vehiculo UBER (Solo 1 vez) (UberX o UberPool)

                if tipo_uber == 1:
                    Driver1 = UberX(1, license_aux, Driver(1, name_aux, document_aux, email_aux, password_aux), 4, brand_car, model_car)
                    aux = False
                    driver_exist = True
                elif tipo_uber == 2:
                    Driver1 = UberPool(1, license_aux, Driver(1, name_aux, document_aux, email_aux, password_aux), 4, brand_car, model_car)
                    aux = False
                    driver_exist = True
                else:
                    print("\nIngrese una opcion valida\n")

            print(f'\nConductor {Driver1.driver.get_name()} registrado con exito!\n')
            aux = True

        elif program_activated == 3:
            if driver_exist == True and user_exist == True:
                # Route: Punto de origen y destino
                route_start = input("\nIngrese ubicacion de origen: ")
                route_end = input("Ingrese ubicacion de destino: ")

                # Costo del servicio
                cost_aux = random.randint(5, 20)
                print(f'\nEl costo del servicio es de ${cost_aux}.')

                # Metodo de pago
                while payment_process != 4:
                    payment_process = int(input("\n--- Metodo de pago ---\n1. Efectivo\n2. Tarjeta\n3. PayPal\n4. Cancelar servicio\nOpcion: "))
                    
                    # Efectivo
                    if payment_process == 1:
                        # Asignando trip al usuario
                        User1.set_trip(Trip(Driver1, Route(1, route_start, route_end), Cash(1, cost_aux)))
                        print(f'\nEl UBER asignado {Driver1.driver.get_name()} esta en camino a buscarlo en el punto: {route_start} y llegara en aproximadamente {random.randint(5, 8)} minutos.\n')
                        break

                    # Tarjeta
                    elif payment_process == 2:

                        # Entrada de datos para el pago
                        card_number = int(input("\nIngrese el numero de la tarjeta: "))
                        cvv_number = int(input("Ingrese el codigo CVV: "))
                        exp_date = input("Ingrese fecha de vencimiento (Formato MM/AAAA): ")
                        bank_card = input("Ingrese el banco asociado a la tarjeta: ")

                        # Asignando trip al usuario
                        User1.set_trip(Trip(Driver1, Route(1, route_start, route_end), Card(2, cost_aux, card_number, cvv_number, exp_date, bank_card)))
                        print(f'\nSu pago fue realizado exitosamente, el UBER asignado {Driver1.driver.get_name()} esta en camino a buscarlo en el punto: {route_start} y llegara en aproximadamente {random.randint(5, 8)} minutos..\n')
                        break

                    # PayPal
                    elif payment_process == 3:

                        # Entrada de datos para el pago
                        email_aux = input("\nIngrese su correo electronico de PayPal: ")

                        # Asignando trip al usuario
                        User1.set_trip(Trip(Driver1, Route(1, route_start, route_end), Paypal(1, cost_aux, email_aux)))
                        print(f'\nSu pago fue realizado exitosamente, el UBER asignado {Driver1.driver.get_name()} esta en camino a buscarlo en el punto: {route_start} y llegara en aproximadamente {random.randint(5, 8)} minutos..\n')
                        break

                    # Opcion invalida
                    elif payment_process == 4:
                        print("\nCancelando servicio.\n")
                    else:
                        print("\nIngrese una opcion valida\n")

                payment_process = 0
            else:
                print("\nDebes agregar un conductor o usuario primero.\n")