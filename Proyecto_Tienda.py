class Categorias:
    def __init__(self, id_categoria, nombre):
        self.id_categoria = id_categoria
        self.nombre = nombre

    def __str__(self):
        return f'Codigo: {self.id_categoria} \t|\t  Nombre: {self.nombre}'


class CrearCategoria:
    def __init__(self):
        self.categorias = {}

    def crear_categoria(self, categoria: Categorias):
        if id_categoria not in self.categorias.keys():
            self.categorias[categoria.id_categoria] = categoria
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

    def actualizar_stock(self, codigo):
        pass


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

    def buscar(self, id_proveedor):
        if id_proveedor in self.proveedores:
            return self.proveedores[id_proveedor]
        return None


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
    def __init__(self, id_empleado, nombre, departamento, telefono, direccion, correo):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.departamento = departamento
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

    def buscar_empleado(self, id_empleado):
        if id_empleado in self.empleados.keys():
            return self.empleados[id_empleado]
        return None


from datetime import datetime  # para obtener fecha y hora


class Ventas:
    def __init__(self, id_venta, nit_cliente, empleado: Empleados):
        self.id_venta = id_venta
        self.fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.cliente = nit_cliente
        self.empleado = empleado.nombre
        self.detalles = []
        self.total = 0

    def __str__(self):
        return (f'Venta No. {self.id_venta} \t|\tFecha: {self.fecha_hora} \t|\tNIT de cliente: {self.cliente} '
                f'\t|\tEncargado de venta: {self.empleado}')


class AgregarVentas:
    def __init__(self):
        self.ventas = {}

    def crear_venta(self, id_venta, venta: Ventas):
        self.ventas[id_venta] = venta

    def agregar_detalle(self, id_venta, detalle):
        self.ventas[id_venta].detalles.append(detalle)


class DetalleVentas:
    def __init__(self, id_detalle, num_venta: Ventas, producto: Productos, cantidad):
        self.id_detalle = id_detalle
        self.num_venta = num_venta.id_venta
        self.producto = producto.nombre
        self.cantidad = cantidad
        self.precio = producto.precio
        self.sub_total = producto.precio * self.cantidad

    def __str__(self):
        return f'{self.num_venta} \t|\t{self.producto} \t|\t{self.cantidad} \t|\t{self.precio} \nSubtotal: {self.sub_total}'


class GestionDetallesVenta:
    def __init__(self):
        self.detalle_ventas = {}

    def agregar_detalles(self, id_detalle, detalle_ventas: DetalleVentas):
        self.detalle_ventas[id_detalle] = detalle_ventas

    def aumentar_cantidad(self, id_detalle, cantidad):
        self.detalle_ventas[id_detalle].cantidad += cantidad


class Compras:
    def __init__(self, id_compra, proveedor: Proveedores, empleado: Empleados):
        self.id_compra = id_compra
        self.fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.proveedor = proveedor.nombre
        self.empleado = empleado.nombre
        self.detalles = []
        self.total = 0

    def __str__(self):
        return (f'Código de compra: {self.id_compra} \t|\tFecha y hora de la compra: {self.fecha_hora}'
                f'\t|\tProveedor: {self.proveedor} \t|\tEncargado de compra: {self.empleado}')


class GestionCompras:
    def __init__(self):
        self.compras = {}

    def agregar_compra(self, id_compra, compra):
        self.compras[id_compra] = compra

    def agregar_detalle(self, id_compra, detalle):
        self.compras[id_compra].detalles.append(detalle)


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


class CrearDetalleCompra:
    def __init__(self):
        self.detalle_compra = {}

    def agregar_detalle_compra(self, id_detalle, detalle_compra):
        self.detalle_compra[id_detalle] = detalle_compra

    def aumentar_cantidad(self, id_detalle, cantidad):
        self.detalle_compra[id_detalle].cantidad += cantidad


# MENÚ Principal
import getpass

num_ventas = 0
empleados = GestionEmpleado()
categoria = CrearCategoria()
proveedores = GestionProveedores()
inventario = Inventario()
while True:
    print("---SISTEMA TIENDA---")
    print("1.Gestión de Empleados")
    print("2.Gestión de bodega")
    print("3.Ventas (cajero)")
    print("4.Salir")
    opcion = input("\nSeleccione una opcion: ")
    if opcion == "1":
        pin = input("Ingrese el PIN de acceso")
        if pin != "Admin123":
            print("❗Acceso no permitido, pin no válido")
            continue
    elif opcion == "2":
        if not empleados.empleados:
            print("No hay empleados en el sistema")
        buscar = empleados.buscar_empleado(input("Ingrese su ID de empleado: "))
        if buscar is None:
            print("El ID ingresado no existe")
            continue
        elif buscar.departamento != "Cordinador de bodega":
            print("El empleado no pertenece al departamento de cordinador de bodega, no puede ingresar a esta área")
            continue
        pin = input("Ingrese la contraseña de acceso: ")
        if pin != "CoBodega123":
            print("❗Acceso no permitido, contraseña no válida")
            continue
        while True:
            print("--MENÚ gestión de bodega--")
            print("1.Gestión de proveedores")
            print("2.Comprar productos (actualizar stock)")
            print("3.Ver todos los productos")
            print("4.Modificar precios")
            print("5.Salir")
            opcion = input("\nSeleccione una opción: ")
            if opcion == "1":
                if not proveedores.proveedores:
                    confirmar = input("No hay proveedores registrados, ¿desea registrar alguno? (S/N): ")
                    if confirmar.lower() == "s":
                        id_proveedor = input("Ingrese el ID del proveedor: ")
                    elif confirmar.lower() == "n":
                        print("Regresando al menú...")
                        continue
                    else:
                        print("Confirmación no válida, regresando al menú...")
                        continue
            elif opcion == "2":
                print("Ralizar compras (ingrese 0 para finalizar):")
                while True:
                    codigo = input("Ingrese el código de producto: ")
                    if codigo == "0":
                        break
                    buscar = inventario.buscar_producto("codigo", codigo)
                    if buscar is None:
                        confirmar = input("El producto no existe, ¿desea registrarlo? S/N: ")
                        if confirmar.lower() == "s":
                            nombre = input("\tNombre: ")
                            while True:
                                id_categoria = input("\tId de categoria: ")
                                if categoria.buscar_categoria(id_categoria) is None:
                                    confirmar = input("La categoría no existe, ¿Desea registrarlo? S/N: ")
                                    if confirmar.lower() == "s":
                                        nombre = input("\tNombre: ")
                                        agregar_categoria = Categorias(id_categoria, nombre)
                                        categoria.crear_categoria(agregar_categoria)
                                        break
                                    elif confirmar.lower() == "n":
                                        pass
                                    else:
                                        print("Confirmación no válida")
                            while True:
                                try:
                                    precio = float(input("\tPrecio: Q."))
                                    if precio < 0:
                                        print("El precio debe ser mayor a 0")
                                    break
                                except ValueError:
                                    print("ERROR: Precio ingresado no válido")
                            producto = Productos(codigo, nombre, categoria, precio)
                            inventario.agregar_producto(producto)
                            break
                        elif confirmar.lower() == "n":
                            pass
                        else:
                            print("Confirmación no válida")
                    while True:
                        try:
                            cantidad = int(input(f"\tCantidad de {buscar} que desea comprar: "))
                            if cantidad < 0:
                                raise ValueError("El cantidad debe ser mayor a 0")
                            break
                        except ValueError as e:
                            print("Ha ocurrido un error: ", e)
                    id_proveedor = input("\tIngrese el Id del proveedor: ")
                    if GestionProveedores.buscar(id_proveedor) is None:
                        print("No se encontre a ningún proveedor")
                        continue
            elif opcion == "5":
                print("Regresando al menú principal")
                break
    elif opcion == "3":
        if inventario:
            print("No se ha realizado ninguna compra de los productos")
            continue
    elif opcion == "5":
        confirmar = input("¿Está seguro que desea salir del programa? S/N: ")
        if confirmar.lower() == "n":
            print("Regresando al menú...")
        elif confirmar.lower() == "s":
            print("Saliendo del programa, tenga buen día...")
            break
        else:
            print("Confirmación no válida, regresando al menú...")
    else:
        print("Opción no disponible")