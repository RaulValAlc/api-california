# Proyecto: Despliegue de Modelo California Housing

Este documento detalla los pasos seguidos para desplegar una API predictiva del valor de las viviendas en California usando un modelo de Machine Learning.

## Pasos para el despliegue

1. **Creación de la cuenta en la plataforma:** 
   Se creó una cuenta gratuita en la plataforma en la nube Render (render.com), vinculándola directamente con la cuenta de GitHub para agilizar el proceso.

2. **Configuración del repositorio:** 
   Se creó un repositorio público en GitHub donde se subió el código fuente. Los archivos principales incluyen `app.py` (API con Flask), `modelo_california.pkl` (el modelo ya entrenado) y `requirements.txt` (las dependencias).

3. **Configuración del servicio en la nube:** 
   En Render, se creó un nuevo "Web Service" enlazado a la rama `main` del repositorio de GitHub, seleccionando Python 3 como entorno.

4. **Comandos de despliegue:** 
   Para la configuración del servicio se establecieron los siguientes comandos:
   - **Build Command:** `pip install -r requirements.txt` (para instalar las librerías necesarias).
   - **Start Command:** `gunicorn app:app` (para levantar el servidor de producción).

5. **URL final:** 
   La aplicación está desplegada y accesible públicamente a través de la siguiente URL:
   **https://api-california.onrender.com**