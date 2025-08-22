class Categorias:
    def __init__(self, id_categoria, nombre):
        self.id_categoria = id_categoria
        self.nombre = nombre

    def __str__(self):
        return f'Codigo: {self.id_categoria} \t|\t  Nombre: {self.nombre}'


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


class Empleados:
    def __init__(self, id_empleado, nombre, telefono, direccion, correo):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo

    def __str__(self):
        return (f'ID: {self.id_empleado} \t|\t Nombe: {self.nombre} \t|\t Teléfono: {self.telefono} '
                f'\t|\t Dirección: {self.direccion} \t|\t Correo: {self.correo}')


from datetime import datetime  # para obtener fecha y hora


class Ventas:
    def __init__(self, id_venta, nit_cliente, empleado: Empleados):
        self.id_venta = id_venta
        self.fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.cliente = nit_cliente
        self.empleado = empleado.nombre

    def __str__(self):
        return (f'Venta No. {self.id_venta} \t|\tFecha: {self.fecha_hora} \t|\tNIT de cliente: {self.cliente} '
                f'\t|\tEncargado de venta: {self.empleado}')


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


class Compras:
    def __init__(self, id_compra, proveedor: Proveedores, empleado: Empleados):
        self.id_compra = id_compra
        self.fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.proveedor = proveedor.nombre
        self.empleado = empleado.nombre

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
        return (f'Compra No. {self.num_compra} \t|\t Nombre del producto: {self.producto} \t|\t Precio de compra: {self.precio_compra}'
                f'\t|\tCantidad comprada: {self.cantidad} \t|\t fecha de caducidad: {self.fecha_caducidad} \nSubtotal: {self.sub_total}')
