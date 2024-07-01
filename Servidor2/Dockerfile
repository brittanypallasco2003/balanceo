FROM python:3.10
EXPOSE 5000
# crear directorio de trabajo
WORKDIR /Servidor2 
# copiar el archivo .py al directorio de trabajo
COPY servidor2.py .
#instalar las dependencias
RUN pip install flask
# ejecutar la aplicación
CMD ["python","servidor2.py"]