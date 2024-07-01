FROM python:3.10
EXPOSE 5000
# crear directorio de trabajo
WORKDIR /Servidor3 
# copiar el archivo .py al directorio de trabajo
COPY servidor3.py .
#instalar las dependencias
RUN pip install flask
# ejecutar la aplicación
CMD ["python","servidor3.py"]