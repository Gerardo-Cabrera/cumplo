# Instrucciones para ejecutar la aplicación

- Se sugiere crear un entorno virtual para instalar allí las dependencias del archivo requirements.txt. Una vez instaladas las dependencias que se encuentran en el mismo, proceder a crear un proyecto con el framework Django.

- También se sugiere que el proyecto tenga por nombre "cumplo" y se cree la app "udis_dolar" (así los denominé yo respectivamente). Una vez creados, reemplazar todos los archivos descargando los de este repositorio.

- Se agregó una carpeta conf, la cual contiene el archivo "config.cfg" en el se incluyeron datos importantes para el funcionamiento de la aplicación. Los mismos pueden ser modificados si el usuario así lo desea.

- Una vez que se ha terminado de realizar la configuración acceder a la ubicación del proyecto a través de la consola (de windows, linux o mac según sea el caso) y colocarse en el nivel donde se encuentre el archivo "manage.py" para ejecutar el siguiente comando: "python manage.py runserver", el cual levantará la aplicación en la siguiente dirección: "http://127.0.0.1:8000" o "http://localhost:8000/", agregar udis-dolar/index para que quede de la siguiente manera: "http://127.0.0.1:8000/udis-dolar/index" o http://localhost:8000/udis-dolar/index y poder utilizar la aplicación.
