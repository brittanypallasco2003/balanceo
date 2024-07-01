FROM python:3.10
EXPOSE 5000
# crear directorio de trabajo
WORKDIR /Servidor1 
# copiar el archivo .py al directorio de trabajo
COPY servidor1.py .
#instalar las dependencias
RUN pip install flask
# ejecutar la aplicación
CMD ["python","servidor1.py"]