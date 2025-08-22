class Categorias:
    def __init__(self, id_categoria, nombre):
        self.id_categoria = id_categoria
        self.nombre = nombre

    def __str__(self):
        return f'Codigo: {self.id_categoria}  |  Nombre: {self.nombre}'


class Productos:
    def __init__(self, id_producto, nombre, categoria: Categorias, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.categoria = categoria.nombre
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
        return (f'Código |\t\tNombre |\t\tCategoría |\t\tPrecio de venta \t\tCompras Totales \t\tVentas Totales \t\tStock'
                f'\n{self.id_producto} |\t\t{self.nombre} |\t\t{self.categoria} |\t\tQ.{self.precio}'
                f'|\t\t{self.total_compras} |\t\t{self.total_ventas} |\t\t{self.stock}')


class Proveedores:
    def __init__(self, id_proveedor, nombre, empresa, telefono, direccion, correo, categoria: Categorias):
        self.id_proveedor = id_proveedor
        self.nombre = nombre
        self.empresa = empresa
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo
        self.categoria = categoria.nombre

    def __str__(self):
        return (f'ID |\t\tNombre |\t\tEmpresa |\t\tTeléfono \t\tDirección \t\tCorreo \t\tCategoría'
                f'\n{self.id_proveedor} |\t\t{self.nombre} |\t\t{self.empresa} |\t\tQ.{self.telefono}'
                f'|\t\t{self.direccion} |\t\t{self.correo} |\t\t{self.categoria}')


class Clientes:
    def __init__(self, nit, nombre, telefono, direccion, correo):
        self.nit = nit
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo

    def __str__(self):
        return (f'NIT |\t\tNombre |\t\tTeléfono \t\tDirección \t\tCorreo'
                f'\n{self.nit} |\t\t{self.nombre} |\t\tQ.{self.telefono} |\t\t{self.direccion} |\t\t{self.correo}')


class Empleados:
    def __init__(self, id_empleado, nombre, telefono, direccion, correo):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo

    def __str__(self):
        return (f'ID |\t\tNombre |\t\tTeléfono \t\tDirección \t\tCorreo'
                f'\n{self.id} |\t\t{self.nombre} |\t\tQ.{self.telefono} |\t\t{self.direccion} |\t\t{self.correo}')


from datetime import datetime  # para obtener fecha y hora


class Ventas:
    def __init__(self, id_venta, cliente: Clientes, empleado: Empleados):
        self.id_venta = id_venta
        self.fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.cliente = cliente.nombre
        self.empleado = empleado.nombre


class DetalleVentas:
    def __init__(self, id_detalle, num_venta: Ventas, cantidad, producto: Productos):
        self.id_detalle = id_detalle
        self.num_venta = num_venta.id_venta
        self.cantidad = cantidad
        self.producto = producto.id_producto
        self.precio = producto.precio
        self.sub_total = producto.precio * cantidad


class Compras:
    def __init__(self, id_compra, proveedor: Proveedores, empleado: Empleados):
        self.id_compra = id_compra
        self.fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.proveedor = proveedor.nombre
        self.empleado = empleado.nombre


class DellateCompras:
    def __init__(self, id_dellate, num_compra: Compras, cantidad, producto: Productos, precio_compra, fecha_caducidad):
        self.id_dellate = id_dellate
        self.num_compra = num_compra.id_compra
        self.cantidad = cantidad
        self.producto = producto.nombre
        self.precio_compra = precio_compra
        self.sub_total = precio_compra * cantidad
        self.fecha_caducidad = fecha_caducidad