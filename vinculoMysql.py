import mysql.connector

try:
   conexion = mysql.connector.connect(
      host = "localhost",
      port = 3306,
      user = 'root',
      password = "root",
      db = "disqueria"
   )
   if conexion.is_connected():
      print("La conexion es exitosa.")



except:
     print("No se conecto.") 

finally:
   if conexion.is_connected():
      conexion.close()
      print("La conexión se cerró.")   