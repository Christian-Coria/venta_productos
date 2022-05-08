
from diseño_clases import Producto


class Orden:
    contador_orden = 0 #inicializamos el contador en 0

    def __init__(self,productos):
        Orden.contador_orden +=1 #por cada objeto creado se uma 1 al contador
        self._id_orden = Orden.contador_orden
        self._productos = list(productos) # nos aseguramos que sea una lista donde se almacenen los productos
        
    def agregar_productos(self,producto): #agregmos el argumento de producto
        self._productos.append(producto) #agregamos producto a la lista

    def calcular_total(self):
        #es necesario definir una variable temporal
        total = 0
        for producto in self._productos:
            total += producto._precio
        return total

    def __str__(self): #metodo para convertir todo a un string
        productos_str = " "
        for producto in self._productos:
            productos_str += producto.__str__() + "---"

        return f"orden {self._id_orden}, Productos: {productos_str}"

if __name__ == "__main__":
    producto1 = Producto("camisa", 100.00)
    producto2 = Producto("pantalon" , 200.00)
    productos1 = [producto1,producto2]
    orden1 = Orden(productos1)
    
    print(orden1)
