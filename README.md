# Proyecto de automatización de creación de cuentas de email con Selenium

## Descripción

Bienvenidos a mi proyecto de automatización de la creación de cuentas de email en diferentes plataformas utilizando Selenium. Este proyecto tiene como objetivo simplificar y automatizar el proceso de registro en servicios populares de correo electrónico como Google, Yahoo y ProtonMail.

### Primera parte: Creación de cuentas de email

En esta primera fase, me he centrado en la implementación de scripts de Python utilizando Selenium para crear cuentas de correo electrónico de manera automática. Los scripts están diseñados para interactuar con los formularios de registro de cada plataforma, rellenar los datos necesarios y finalizar el proceso de registro.

Los scripts incluidos son:

- **Google**: Automatización del registro de cuentas en Gmail.
- **Yahoo**: Automatización del registro de cuentas en Yahoo Mail.
- **ProtonMail**: Automatización del registro de cuentas en ProtonMail.

Cada script sigue una estructura similar:

1. **Inicialización del navegador**: Utiliza Selenium WebDriver para abrir un navegador y acceder a la página de registro.
2. **Generación de datos aleatorios**: Genera nombres, apellidos, fechas de nacimiento y contraseñas aleatorias para cada cuenta.
3. **Relleno de formularios**: Utiliza Selenium para rellenar los campos del formulario de registro con los datos generados.
4. **Envío del formulario**: Finaliza el proceso de registro enviando el formulario.

### Segunda parte: Verificación con números de teléfono virtuales

Aunque esta parte no está incluida en el repositorio, mencionaré que el proyecto también contempla la conexión con números de teléfono virtuales para completar la verificación de las cuentas creadas. Esta funcionalidad permite recibir códigos de verificación enviados por las plataformas de correo electrónico para confirmar la autenticidad del número de teléfono proporcionado.

**Nota**: No he incluido esta segunda parte en GitHub debido a preocupaciones legales y éticas que aún estoy investigando.

## Requisitos

- Python 3.8 o superior
- Selenium
- Un navegador web compatible (Chrome, Firefox, etc.)
- WebDriver para el navegador utilizado (ChromeDriver, GeckoDriver, etc.)

## Instalación

1. Clona el repositorio en tu máquina local.
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
