### Programa de Validación de iP ###

# importamos el módulo ipaddress
import ipaddress

# creamos una función para tomar la dirección IP como parámetro y tratar de crear un objeto de dirección IP
def validar_ip(direccion_ip):
    try:
        ip = ipaddress.ip_address(direccion_ip)
        if ip.is_private:
            print(f"{direccion_ip} es una IP privada válida ({ip.version}).")
        else:
            print(f"{direccion_ip} es una IP pública válida ({ip.version}).")
    except ValueError:
        print(f"{direccion_ip} no es una IP válida.")

# añadimos otra función que recibe una subred en CIDR
# intenta crear un objeto de red, si no es válido lanza excepción   
def validar_subred(direccion_subred):
    try:
        red = ipaddress.ip_network(direccion_subred, strict=False) # permite validar tanto redes completas como direcciones específicas dentro de esas redes
        print(f"{direccion_subred} es una subred válida.")
    except ValueError:
        print(f"{direccion_subred} no es una subred válida.")

# se añade un menu para que el programa sea fácil de usar
def menu():
    while True:
        print("\nMenú de opciones:")
        print(" 1. Validar dirección IP")
        print(" 2. Validar subred (CIDR)")
        print(" 3. Salir")

        opcion = input ("Qué quieres hacer: ")

        if opcion == "1":
            direccion_ip = input("Introduce la dirección IP: ")
            validar_ip(direccion_ip)
        elif opcion == "2":
            direccion_subred = input("Introduce la subred en formato CIDR (ej: 192.168.1.0/24): ")
            validar_subred(direccion_subred)
        elif opcion == "3":
            print("¡Hasta la próxima!")
            break
        else:
            print("Opción no válida, inserta el número de la acción que quieres realizar.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
    