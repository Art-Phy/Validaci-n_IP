"""
===============================
     IP VALIDATOR (v1.1.0)
===============================

Validador de direcciones IP y subredes (CIDR) con soporte para
ejecución interactiva (menú) o mediamte argumento CLI

Autor: Art-Phy
Versión: 1.1.0

Dependencias:
    - coloroma (para colorear la salida, opcional)
        pip install colorama
"""

from __future__ import annotations
import ipaddress
import argparse
import sys
from typing import Optional
from colorama import Fore, Style, init

# Inicializa colorama (para Windows y UNIX)
init(autoreset=True)


def validar_ip(direc_ip: str) -> bool:
    """
    Valida si una dirección IP es válida y muestra su tipo.
    
    Args:
        direc_ip: Dirección IP como string.

    Returns:
        bool: True si es válida, False si no.
    """
    try:
        ip = ipaddress.ip_address(direc_ip)
        tipo = "privada" if ip.is_private else "pública"
        print(f"{Fore.GREEN}✅ {direc_ip} es una IP {tipo} válida ({ip.version}).{Style.RESET_ALL}")
        return True
    except ValueError:
        print(f"{Fore.RED}❌ {direc_ip} no es una IP válida.{Style.RESET_ALL}")
        return False
    

def validar_subred(direc_subred: str) -> bool:
    """
    Valida si una subred (CIDR) es válida.

    Args:
        direc_subred: Subred en formato CIDR (ejm: '192.168.1.0/24).

    Return:
        bool: True si es válida, False si no.
    """
    try:
        red = ipaddress.ip_network(direc_subred, strict=False)
        print(f"{Fore.GREEN}✅ {direc_subred} es una subred válida ({red.version}). {Style.RESET_ALL}")
        return True
    except ValueError:
        print(f"{Fore.RED}❌ {direc_subred} no es una subred válida.{Style.RESET_ALL}")
        return False
    

def menu() -> None:
    """
    Muestra un menú interactivo para validar IPs o subredes.
    """
    while True:
        print("\nMenú de opciones:")
        print(" 1. Validar dirección IP")
        print(" 2. Validar subred (CIDR)")
        print(" 3. Salir")

        option = input("Elige una opción (1-3): ").strip()

        if option == "1":
            direc_ip = input("Introduce la dirección IP: ").strip()
            validar_ip(direc_ip)
        elif option == "2":
            direc_subred = input("Introduce la subred (CIDR, ej: 192.168.1.0/24): ").strip()
            validar_subred(direc_subred)
        elif option == 3:
            print("👋 ¡Hasta la próxima!")
            break
        else:
            print(f"{Fore.YELLOW}⚠️ Opción no válida. Intenta de nuevo.{Style.RESET_ALL}")


def parse_args() -> argparse.Namespace:
    """
    Analiza los argumentos de línea de comandos.

    Returns:
        argparse.Namespace con los parámetros parseados.
    """

