class Categorias:
    def __init__(self, id_categoria, nombre):
        self.id_categoria = id_categoria
        self.nombre = nombre

    def __str__(self):
        return f'Codigo: {self.id_categoria} \t|\t  Nombre: {self.nombre}'


class CrearCategoria:
    def __init__(self):
        self.categorias = {}

    def crear_categoria(self, id_categoria, nombre):
        if id_categoria not in self.categorias.keys():
            self.categorias[id_categoria] = {'nombre': nombre}
            print("Categoría registrada correctamente")
        else:
            raise ValueError("Ya se ha registrado una categoría con el mismo id")

    def buscar_categoria(self, id_categoria):
        if id_categoria in self.categorias.keys():
            return self.categorias[id_categoria]
        else:
            return None


class Productos:
    def __init__(self, id_producto, nombre, id_categoria, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.categoria = id_categoria
        self.__precio = precio
        self.total_compras = 0
        self.total_ventas = 0
        self.stock = 0

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, precio):
        if precio > 0:
            self.__precio = precio
        else:
            raise ValueError("El precio debe ser mayor a 0")

    def __str__(self):
        return (f'Código: {self.id_producto} \t|\t {self.nombre} \t|\t Categoría: {self.categoria} '
                f'\t|\t Precio de venta: Q.{self.precio} \t|\t Compras totales: {self.total_compras} '
                f'\t|\t Ventas totales: {self.total_ventas} \t|\t Stock disponible: {self.stock}')


class Ordenador:
    @staticmethod
    def obtener_valor(producto, clave):
        if clave == "codigo":
            return producto.codigo
        elif clave == "nombre":
            return producto.nombre
        elif clave == "categoria":
            return producto.categoria
        elif clave == "precio":
            return producto.precio
        elif clave == "stock":
            return producto.stock
        return producto.nombre  # pro defecto se va a ordenar por nombre

    @staticmethod
    def quick_sort(lista, clave):
        if len(lista) <= 1:
            return lista
        pivote = Ordenador.obtener_valor(lista[0], clave)
        menores = [x for x in lista[1:] if Ordenador.obtener_valor(x, clave) < pivote]
        iguales = [x for x in lista if Ordenador.obtener_valor(x, clave) == pivote]
        mayores = [x for x in lista[1:] if Ordenador.obtener_valor(x, clave) > pivote]
        return Ordenador.quick_sort(menores, clave) + iguales + Ordenador.quick_sort(mayores, clave)


class Buscador:
    @staticmethod
    def buscar(lista, clave, valor):
        resultados = []
        for producto in lista:
            if clave == "codigo" and producto.codigo == valor:
                resultados.append(producto)
            elif clave == "nombre" and valor.lower() in producto.nombre.lower():
                resultados.append(producto)
            elif clave == "categoria" and valor.lower() in producto.categoria.lower():
                resultados.append(producto)
        return resultados


class Inventario:
    def __init__(self):
        self.inventario = {}

    def agregar_producto(self, producto: Productos):
        if producto.id_producto in self.inventario:
            raise ValueError('Ya existe un producto con el mismo código')
        self.inventario[producto.id_producto] = producto

    def listar_productos(self, clave):
        lista = list(self.inventario.values())
        return Ordenador.quick_sort(lista, clave) if lista else []

    def buscar_producto(self, clave, valor):
        lista = list(self.inventario.values())
        return Buscador.buscar(lista, clave, valor)

    def actualizar_precio(self, codigo, nuevo_precio):
        if codigo in self.inventario:
            self.inventario[codigo].precio = nuevo_precio
        else:
            raise ValueError("Producto no encontrado")

    def actualizar_stock(self):
        pass

    def eliminar_producto(self, codigo):
        if codigo in self.inventario:
            del self.inventario[codigo]
        else:
            raise ValueError("Producto no encontrado")


class Proveedores:
    def __init__(self, id_proveedor, nombre, empresa, telefono, direccion, correo, categoria):
        self.id_proveedor = id_proveedor
        self.nombre = nombre
        self.empresa = empresa
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo
        self.categoria = categoria

    def __str__(self):
        return (f'ID: {self.id_proveedor} \t|\t Nombre: {self.nombre} \t|\t Empresa: {self.empresa} '
                f'\t|\t Teléfono: {self.telefono} \t|\t Dirección: {self.direccion} \t|\t Correo: {self.correo} '
                f'\t|\t Categoría: {self.categoria}')


class GestionProveedores:
    def __init__(self):
        self.proveedores = {}

    def agregar_proveedor(self, id_proveedor, proveedor: Proveedores):
        if id_proveedor not in self.proveedores:
            self.proveedores[id_proveedor] = proveedor
        else:
            raise ValueError("Ya existe un provedor con el mismo ID")


class Clientes:
    def __init__(self, nit, nombre, telefono, direccion, correo):
        self.nit = nit
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo

    def __str__(self):
        return (f'NIT: {self.nit} \t|\t Nombre: {self.nombre} \t|\t Teléfono{self.telefono} '
                f'\t|\t Dirección: {self.direccion} \t|\t Correo: {self.correo}')


class GestionCliente:
    def __init__(self):
        self.clientes = {}

    def agregar_cliente(self, nit, cliente):
        if nit not in self.clientes:
            self.clientes[nit] = cliente
        else:
            raise ValueError("Ya existe un cliente con el mismo NIT")


class Empleados:
    def __init__(self, id_empleado, nombre, rol, telefono, direccion, correo):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.rol = rol
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo

    def __str__(self):
        return (f'ID: {self.id_empleado} \t|\t Nombe: {self.nombre} \t|\t Teléfono: {self.telefono} '
                f'\t|\t Dirección: {self.direccion} \t|\t Correo: {self.correo}')


class GestionEmpleado:
    def __init__(self):
        self.empleados = {}

    def agregar_empleado(self, id_empleado, empleado):
        if id_empleado not in self.empleados:
            self.empleados[id_empleado] = empleado
            print("Empleado registrado correctamente")
        else:
            raise ValueError("Ya existe un empleado con el mismo ID")


from datetime import datetime  # para obtener fecha y hora


class Ventas:
    def __init__(self, id_venta, nit_cliente, empleado: Empleados):
        self.id_venta = id_venta
        self.fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.cliente = nit_cliente
        self.empleado = empleado.nombre
        self.total = 0

    def __str__(self):
        return (f'Venta No. {self.id_venta} \t|\tFecha: {self.fecha_hora} \t|\tNIT de cliente: {self.cliente} '
                f'\t|\tEncargado de venta: {self.empleado}')


class AgregarVentas:
    def __init__(self):
        self.ventas = {}

    def crear_venta(self, id_venta, venta: Ventas):
        self.ventas[id_venta] = venta


class DetalleVentas:
    def __init__(self, id_detalle, num_venta: Ventas, producto: Productos, cantidad):
        self.id_detalle = id_detalle
        self.num_venta = num_venta.id_venta
        self.producto = producto.nombre
        self.cantidad = cantidad
        self.precio = producto.precio
        self.sub_total = producto.precio * cantidad

    def __str__(self):
        return f'{self.num_venta} \t|\t{self.producto} \t|\t{self.cantidad} \t|\t{self.precio} \nSubtotal: {self.sub_total}'


class GestionDetallesVenta:
    def __init__(self):
        self.detalle_ventas = {}

    def agregar_detalles(self, id_detalle, detalle_ventas:DetalleVentas):
        self.detalle_ventas[id_detalle] = detalle_ventas

class Compras:
    def __init__(self, id_compra, proveedor: Proveedores, empleado: Empleados):
        self.id_compra = id_compra
        self.fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.proveedor = proveedor.nombre
        self.empleado = empleado.nombre
        self.total = 0

    def __str__(self):
        return (f'Código de compra: {self.id_compra} \t|\tFecha y hora de la compra: {self.fecha_hora}'
                f'\t|\tProveedor: {self.proveedor} \t|\tEncargado de compra: {self.empleado}')


class DellateCompras:
    def __init__(self, id_dellate, num_compra: Compras, producto: Productos, precio_compra, cantidad, fecha_caducidad):
        self.id_dellate = id_dellate
        self.num_compra = num_compra.id_compra
        self.producto = producto.nombre
        self.precio_compra = precio_compra
        self.cantidad = cantidad
        self.fecha_caducidad = fecha_caducidad
        self.sub_total = precio_compra * cantidad

    def __str__(self):
        return (
            f'Compra No. {self.num_compra} \t|\t Nombre del producto: {self.producto} \t|\t Precio de compra: {self.precio_compra}'
            f'\t|\tCantidad comprada: {self.cantidad} \t|\t fecha de caducidad: {self.fecha_caducidad} \nSubtotal: {self.sub_total}')


class Menu:
    def mostrar_menu(self):
        pass


class MenuProductos(Menu):
    @staticmethod
    def mostrar_menu_productos():
        while True:
            print("--MENÚ gestión de productos--")
            print("1.Registrar productos")
            print("2.Comprar productos (actualizar stock)")
            print("3.Ver todos los productos")
            print("4.Modificar precios")
            print("5.Salir")
            opcion = input("\nSeleccione una opción: ")
            if opcion == "1":
                print("Ingrese los códigos de los productos, ingrese '0' para finalizar: ")
                while True:
                    codigo = input("Codigo del producto: ")
                    if codigo == "0":
                        break
                    nombre = input("\tNombre: ")
                    precio = input("\tPrecio: ")
                    categoria = input("\tId de categoria: ")
                    if CrearCategoria.buscar_categoria(categoria) is None:
                        print("No se encontró una categoría con el id ingresado, intente de nuevo")
            elif opcion == "5":
                print("Regresando al menú principal")
                break


class MenuCaja(Menu):
    def mostrar_menu(self):
        while True:
            print("---MENÚ Cajero---")
            print("1.Cobrar")
            print("2.Salir")
            opcion = input("\nSeleccione una opción: ")
            if opcion == "1":
                print("Ingrese los códigos de productos ('0' para finalizar): ")
                while True:
                    codigo = input("Código de producto:")
                    if codigo == "0":
                        break
            elif opcion == "2":
                print("Regresando al menú principal...")
                break
