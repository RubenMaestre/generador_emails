from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import csv
import random
import time
import string

# Ruta completa al ChromeDriver descargado
chrome_driver_path = r"C:\Users\34670\Desktop\python\amazon\cuentas_google\chromedriver.exe"

# Configuración del servicio de ChromeDriver
service = Service(executable_path=chrome_driver_path)

# Inicializar el navegador con el servicio de ChromeDriver
browser = webdriver.Chrome(service=service)

# Abrir la página de registro de Yahoo Mail
browser.get("https://login.yahoo.com/account/create")

# Maximizar la ventana del navegador
browser.maximize_window()

# Esperar a que la página cargue
wait = WebDriverWait(browser, 10)

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

# Función para generar una dirección de Yahoo basada en el nombre y apellido
def generar_direccion_yahoo(nombre, primer_apellido, dia, anio):
    nombre_sanitizado = nombre.replace(" ", "").lower()
    apellido_sanitizado = primer_apellido.replace(" ", "").lower()
    direccion_yahoo = f"{nombre_sanitizado}{anio}{apellido_sanitizado}{dia}@yahoo.com"
    return direccion_yahoo

# Función para generar una contraseña aleatoria
def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + "$@&/"
    while True:
        contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
        if (any(c.islower() for c in contrasena)
            and any(c.isupper() for c in contrasena)
            and any(c.isdigit() for c in contrasena)
            and any(c in "$@&/" for c in contrasena)):
            break
    return contrasena

# Función para guardar los datos en un archivo CSV
def guardar_datos_csv(filename, data):
    file_exists = os.path.isfile(filename)
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Nombre", "Primer Apellido", "Segundo Apellido", "Dia", "Mes", "Anio", "Sexo", "Correo Electronico", "Password"])
        writer.writerow(data)

# Generar una fecha de nacimiento aleatoria
dia = random.randint(1, 30)
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
mes = random.choice(meses)
anio = random.randint(1970, 2001)

# Generar un nombre completo aleatorio
nombre, primer_apellido, segundo_apellido = generar_nombre_completo()
sexo = "Prefiero no decirlo"
direccion_yahoo = generar_direccion_yahoo(nombre, primer_apellido, dia, anio)

# Generar una contraseña aleatoria
password = generar_contrasena(random.randint(10, 15))

# Guardar los datos en un archivo CSV
guardar_datos_csv('datos_yahoo.csv', [nombre, primer_apellido, segundo_apellido, dia, mes, anio, sexo, direccion_yahoo, password])

print(f"Llenando el formulario con: {nombre} {primer_apellido} {segundo_apellido}")

# Rellenar el campo de nombre
first_name_field = wait.until(EC.presence_of_element_located((By.ID, "usernamereg-firstName")))
time.sleep(random.uniform(1, 10))
first_name_field.send_keys(nombre)

# Rellenar el campo de apellidos (combinando ambos apellidos)
last_name_field = wait.until(EC.presence_of_element_located((By.ID, "usernamereg-lastName")))
time.sleep(random.uniform(1, 10))
last_name_field.send_keys(f"{primer_apellido} {segundo_apellido}")

# Seleccionar el mes de nacimiento
month_dropdown = wait.until(EC.presence_of_element_located((By.ID, "usernamereg-month")))
time.sleep(random.uniform(1, 10))
month_dropdown.click()
month_option = wait.until(EC.presence_of_element_located((By.XPATH, f"//option[text()='{mes}']")))
time.sleep(random.uniform(1, 10))
month_option.click()

# Rellenar el día de nacimiento
day_field = wait.until(EC.presence_of_element_located((By.ID, "usernamereg-day")))
time.sleep(random.uniform(1, 10))
day_field.send_keys(str(dia))

# Rellenar el año de nacimiento
year_field = wait.until(EC.presence_of_element_located((By.ID, "usernamereg-year")))
time.sleep(random.uniform(1, 10))
year_field.send_keys(str(anio))

# Generar una dirección de Yahoo basada en el nombre, apellido, día y año de nacimiento
direccion_yahoo = generar_direccion_yahoo(nombre, primer_apellido, dia, anio)

# Rellenar el campo de dirección de correo electrónico
email_field = wait.until(EC.presence_of_element_located((By.ID, "usernamereg-userId")))
time.sleep(random.uniform(1, 10))
email_field.send_keys(direccion_yahoo.split('@')[0])

# Rellenar el campo de contraseña
password_field = wait.until(EC.presence_of_element_located((By.ID, "usernamereg-password")))
time.sleep(random.uniform(1, 10))
password_field.send_keys(password)

# Hacer clic en el botón "Siguiente"
submit_button = wait.until(EC.element_to_be_clickable((By.ID, "reg-submit-button")))
time.sleep(random.uniform(1, 10))
submit_button.click()

# Esperar unos segundos para ver el resultado
time.sleep(5)

# A partir de aquí, lo siguiente es introducir el teléfono. Esto ya lo he desarrollado de forma privada, hay varias empresas
# que ofrecen números de teléfonos virtuales (que son de pago) que nos valdría para introducir el teléfono en Yahoo, 
# enviará un mensaje, que conectaremos a un servidor mediante Flask y recibiríamos el código de autorización de Yahoo. 
# Con eso ya lo tendríamos y podríamos tener la cuenta operativa.