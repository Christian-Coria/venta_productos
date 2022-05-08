class Producto:
    contador_producto = 0

    def __init__(self,nombre,precio):
        Producto.contador_producto +=1
        self._id_producto = Producto.contador_producto
        self._nombre = nombre
        self._precio = precio

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self,precio):
        self._precio = precio
    def __str__(self):
        return f"id: {self._id_producto} , nombre: {self._nombre} , precio: {self._precio}"

    #VERIFICAMOS QUE EL CODIGO SOLO SE EJECUTA SI ESTA EN EL MISMO MODULO Y ARCHIVO
    #asi hacemos pruebas privadas 
if __name__ == "__main__":
   producto1 = Producto("camisa", 100.00)
   print(producto1)
   producto2 = Producto("pantalon" , 200.00)
   print(producto2)



        