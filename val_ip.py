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
        red = ipaddress.ip_network(direccion_subred, strict=False)
        print(f"{direccion_subred} es una subred válida.")
    except ValueError:
        print(f"{direccion_subred} no es una subred válida.")
