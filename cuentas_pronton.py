from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import csv
import random
import time
import pyperclip
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Ruta completa al ChromeDriver descargado
chrome_driver_path = r"C:\Users\34670\Desktop\python\amazon\cuentas_google\chromedriver.exe"

# Configuración del servicio de ChromeDriver
service = Service(executable_path=chrome_driver_path)

# Inicializar el navegador con el servicio de ChromeDriver
browser = webdriver.Chrome(service=service)

# Abrir la página de registro de ProtonMail
browser.get("https://account.proton.me/signup")

# Maximizar la ventana del navegador
browser.maximize_window()

# Esperar a que la página cargue
wait = WebDriverWait(browser, 30)

# Listado de nombres
nombres = [
    "Alfredo", "Juan Francisco", "Elias", "Sofia", "Elena", "Marta", "Carolina", "Carol", "Ruben", "Diego",
    "Lucia", "Maria", "Laura", "Ana", "Daniel", "Pablo", "Javier", "Carlos", "Miguel", "Antonio",
    "Jose", "Fernando", "Raul", "Sara", "Patricia", "Nuria", "Rosa", "Cristina", "Beatriz", "Angela",
    "Ivan", "Hector", "Alberto", "Sergio", "Gabriel", "Andres", "Luis", "Francisco", "Manuel", "Pedro",
    "Alejandro", "Adrian", "Oscar", "Victor", "Jorge", "Raquel", "Carmen", "Isabel", "Pilar", "Ricardo"
]

# Listado de primeros apellidos
primeros_apellidos = [
    "Garcia", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Perez", "Sanchez", "Ramirez", "Torres",
    "Flores", "Rivera", "Gomez", "Diaz", "Cruz", "Reyes", "Morales", "Ortiz", "Gutierrez", "Chavez",
    "Ramos", "Vargas", "Castro", "Romero", "Mendoza", "Ruiz", "Herrera", "Aguilar", "Medina", "Castillo",
    "Vega", "Soto", "Marquez", "Guerrero", "Silva", "Delgado", "Pena", "Rojas", "Blanco", "Molina",
    "Navarro", "Gil", "Cabrera", "Jimenez", "Santos", "Mendez", "Paredes", "Rivas", "Salazar", "Rojas"
]

# Listado de segundos apellidos
segundos_apellidos = [
    "Fernandez", "Jimenez", "Suarez", "Castro", "Ortiz", "Rubio", "Mendez", "Navarro", "Ramos", "Reyes",
    "Guzman", "Paredes", "Rivas", "Espinoza", "Cabrera", "Salazar", "Aguirre", "Luna", "Benitez", "Santos",
    "Gil", "Cabrera", "Santos", "Mendez", "Paredes", "Rivas", "Salazar", "Rojas", "Blanco", "Molina",
    "Garcia", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Perez", "Sanchez", "Ramirez", "Torres",
    "Flores", "Rivera", "Gomez", "Diaz", "Cruz", "Reyes", "Morales", "Ortiz", "Gutierrez", "Chavez"
]

# Función para generar una combinación aleatoria de nombre, primer apellido y segundo apellido
def generar_nombre_completo():
    nombre = random.choice(nombres)
    primer_apellido = random.choice(primeros_apellidos)
    segundo_apellido = random.choice(segundos_apellidos)
    return nombre, primer_apellido, segundo_apellido

# Función para generar una dirección de ProtonMail basada en el nombre, apellido, día y año de nacimiento
def generar_direccion_protonmail(nombre, primer_apellido, dia, anio):
    nombre_sanitizado = nombre.replace(" ", "").lower()
    apellido_sanitizado = primer_apellido.replace(" ", "").lower()
    direccion_protonmail = f"{nombre_sanitizado}{anio}{apellido_sanitizado}{dia}"
    return direccion_protonmail

# Función para generar una contraseña aleatoria
def generar_contraseña_aleatoria(longitud):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789$@&/"
    while True:
        contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
        if (any(c.islower() for c in contraseña) and any(c.isupper() for c in contraseña) and any(c.isdigit() for c in contraseña) and any(c in '$@&/' for c in contraseña)):
            return contraseña

# Función para guardar los datos en un archivo CSV
def guardar_datos_csv(filename, data):
    file_exists = os.path.isfile(filename)
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Nombre", "Primer Apellido", "Segundo Apellido", "Dia", "Mes", "Anio", "Sexo", "Correo Electronico", "Contraseña"])
        writer.writerow(data)

# Generar una fecha de nacimiento aleatoria
dia = random.randint(1, 30)
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
mes = random.choice(meses)
anio = random.randint(1970, 2001)

# Generar un nombre completo aleatorio
nombre, primer_apellido, segundo_apellido = generar_nombre_completo()
sexo = "Prefiero no decirlo"
direccion_protonmail = generar_direccion_protonmail(nombre, primer_apellido, dia, anio)
contraseña = generar_contraseña_aleatoria(random.randint(10, 15))

# Guardar los datos en un archivo CSV
guardar_datos_csv('datos_protonmail.csv', [nombre, primer_apellido, segundo_apellido, dia, mes, anio, sexo, direccion_protonmail, contraseña])

print(f"Llenando el formulario con: Nombre de Usuario: {direccion_protonmail}")

# Esperar hasta que el campo de nombre de usuario sea visible
try:
    username_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#email")))
except TimeoutException:
    print("No se pudo encontrar el campo de nombre de usuario por CSS_SELECTOR. Intentando con XPATH.")
    username_field = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='email']")))

time.sleep(random.uniform(1, 10))

# Intentar hacer clic en el campo de nombre de usuario utilizando JavaScript
browser.execute_script("arguments[0].click();", username_field)
username_field.send_keys(direccion_protonmail)

# Rellenar el campo de contraseña
password_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#password")))
time.sleep(random.uniform(1, 10))
password_field.send_keys(contraseña)

# Rellenar el campo de confirmar contraseña
confirm_password_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#repeat-password")))
time.sleep(random.uniform(1, 10))
confirm_password_field.send_keys(contraseña)

# Hacer clic en el botón "Crear cuenta"
create_account_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Crear cuenta')]")))
time.sleep(random.uniform(1, 10))
create_account_button.click()

# Esperar unos segundos para ver el resultado
time.sleep(10)

# A partir de aquí, lo siguiente es introducir el teléfono. Esto ya lo he desarrollado de forma privada porque exige
# conexiones para validar por móvil