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
