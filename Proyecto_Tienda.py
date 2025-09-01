class Categorias:
    def __init__(self, id_categoria, nombre):
        self.id_categoria = id_categoria
        self.nombre = nombre

    def __str__(self):
        return f'Codigo: {self.id_categoria} \t|\t  Nombre: {self.nombre}'


class CrearCategoria:
    def __init__(self):
        self.categorias = {}
        self.cargar_categorias()

    def cargar_categorias(self):
        try:
            with open('categorias.txt', 'r', encoding="utf-8") as file:
                for linea in file:
                    linea = linea.strip()
                    if linea:
                        id_categoria, nombre = linea.split(':')
                        categoria = Categorias(id_categoria, nombre)
                        self.categorias[id_categoria] = categoria
                print("Categorias cargadas exitosamente")
        except FileNotFoundError:
            print("No existe el archivo categorias.txt, se creará uno al guardar")

    def guardar_categorias(self):
        with open('categorias.txt', 'w', encoding="utf-8") as file:
            for id_categoria, categoria in self.categorias.items():
                file.write(f'{id_categoria}:{categoria.nombre}\n')

    def crear_categoria(self, categoria: Categorias):
        if categoria.id_categoria not in self.categorias.keys():
            self.categorias[categoria.id_categoria] = categoria
            self.guardar_categorias()
            print(f"Categoría registrada correctamente")
        else:
            raise ValueError("Ya se ha registrado una categoría con el mismo id")

    def buscar_categoria(self, id_categoria):
        if id_categoria in self.categorias.keys():
            return self.categorias[id_categoria]
        else:
            return None


class Productos:
    def __init__(self, id_producto, nombre, id_categoria, precio, total_compras, total_ventas, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.categoria = id_categoria
        self.__precio = precio
        self.total_compras = total_compras
        self.total_ventas = total_ventas
        self.stock = stock

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
            return producto.id_producto
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
            if clave == "codigo" and producto.id_producto == valor:
                resultados.append(producto)
            elif clave == "nombre" and valor.lower() in producto.nombre.lower():
                resultados.append(producto)
            elif clave == "categoria" and valor.lower() in producto.categoria.lower():
                resultados.append(producto)
        return resultados


class Inventario:
    def __init__(self):
        self.inventario = {}
        self.cargar_productos()

    def cargar_productos(self):
        try:
            with open('productos.txt', 'r', encoding="utf-8") as file:
                for linea in file:
                    linea = linea.strip()
                    if linea:
                        id_producto, nombre, id_categoria, precio, total_compras, total_ventas, stock = linea.split(':')
                        producto = Productos(id_producto, nombre, id_categoria, float(precio), int(total_compras),
                                             int(total_ventas), int(stock))
                        self.inventario[id_producto] = producto
                print("Productos importados correctamente")
        except FileNotFoundError:
            print("No existe el archivo productos.txt, se creará uno al guardar")

    def guardar_productos(self):
        with open('productos.txt', 'w', encoding="utf-8") as file:
            for id_producto, producto in self.inventario.items():
                file.write(f'{id_producto}:{producto.nombre}:{producto.categoria}:{producto.precio}:'
                           f'{producto.total_compras}:{producto.total_ventas}:{producto.stock}\n')

    def agregar_producto(self, producto: Productos):
        if producto.id_producto in self.inventario:
            raise ValueError('Ya existe un producto con el mismo código')
        self.inventario[producto.id_producto] = producto
        self.guardar_productos()
        print("Productos agregados correctamente")

    def listar_productos(self, clave):
        lista = list(self.inventario.values())
        return Ordenador.quick_sort(lista, clave) if lista else []

    def buscar_producto(self, clave, valor):
        lista = list(self.inventario.values())
        return Buscador.buscar(lista, clave, valor)

    def actualizar_precio(self, codigo, nuevo_precio):
        if codigo in self.inventario:
            self.inventario[codigo].precio = nuevo_precio
            print("Precio actualizado correctamente")
        else:
            raise ValueError("Producto no encontrado")

    def actualizar_stock(self, codigo, cantidad, motivo):
        if motivo == "compra":
            self.inventario[codigo].total_compras += cantidad
            self.inventario[codigo].stock += cantidad

        else:
            if cantidad > self.inventario[codigo].stock:
                raise ValueError("No hay stock suficiente")
            self.inventario[codigo].total_ventas += cantidad
            self.inventario[codigo].stock -= cantidad
        self.guardar_productos()  # 🔹 Guardar automáticamente


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
        self.cargar_proveedores()

    def cargar_proveedores(self):
        try:
            with open('proveedores.txt', 'r', encoding="utf-8") as file:
                for linea in file:
                    linea = linea.strip()
                    if linea:
                        id_proveedor, nombre, empresa, telefono, direccion, correo, categoria = linea.split(':')
                        proveedor = Proveedores(id_proveedor, nombre, empresa, telefono, direccion, correo, categoria)
                        self.proveedores[id_proveedor] = proveedor
                print("Proveedores  importados correctamente")
        except FileNotFoundError:
            print("No existe el archivo productos.txt, se creará uno al guardar")

    def guardar_proveedores(self):
        with open('proveedores.txt', 'w', encoding="utf-8") as file:
            for id_proveedor, proveedor in self.proveedores.items():
                file.write(
                    f'{id_proveedor}:{proveedor.nombre}:{proveedor.empresa}:{proveedor.telefono}:{proveedor.direccion}:'
                    f'{proveedor.correo}:{proveedor.categoria}\n')

    def agregar_proveedor(self, proveedor: Proveedores):
        if proveedor.id_proveedor not in self.proveedores:
            self.proveedores[proveedor.id_proveedor] = proveedor
            self.guardar_proveedores()
            print("Proveedor agregado correctamente")
        else:
            raise ValueError("Ya existe un provedor con el mismo ID")

    def buscar(self, id_proveedor):
        if id_proveedor in self.proveedores:
            return self.proveedores[id_proveedor]
        return None


class Clientes:
    def __init__(self, nit, nombre, direccion, telefono, correo):
        self.nit = nit
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo

    def __str__(self):
        return (f'NIT: {self.nit} \t|\t Nombre: {self.nombre} \t|\t Teléfono{self.telefono} '
                f'\t|\t Dirección: {self.direccion} \t|\t Correo: {self.correo}')


class GestionCliente:
    def __init__(self):
        self.clientes = {}
        self.cargar_clientes()

    def cargar_clientes(self):
        try:
            with open("clientes.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        nit, nombre, direccion, telefono, correo = linea.split(":")
                        cliente = Clientes(nit, nombre, direccion, telefono, correo)
                        self.clientes[nit] = cliente
            print("Clientes importados desde clientes.txt")
        except FileNotFoundError:
            print("No existe el archivo clientes.txt, se creará uno nuevo al guardar.")

    def guardar_clientes(self):
        with open("clientes.txt", "w", encoding="utf-8") as archivo:
            for nit, datos in self.clientes.items():
                archivo.write(f"{nit}:{datos.nombre}:{datos.direccion}:{datos.telefono}:{datos.correo}\n")

    def agregar_cliente(self, nit, cliente):
        if nit not in self.clientes:
            self.clientes[nit] = cliente
            self.guardar_clientes()
            print("Cliente registrado correctamente")
        else:
            raise ValueError("Ya existe un cliente con el mismo NIT")

    def buscar_cliente(self, nit):
        if nit in self.clientes:
            return self.clientes[nit]
        return None


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
        self.cargar_empleado()

    def cargar_empleado(self):
        try:
            with open("empleados.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        id_empleado, nombre, departamento, telefono, direccion, correo = linea.split(":")
                        empleado = Empleados(id_empleado, nombre, departamento, telefono, direccion, correo)
                        self.empleados[id_empleado] = empleado
                print("Empleados importados correctamente")
        except FileNotFoundError:
            print("No existe el archivo empleados.txt, se creará uno al guardar")

    def guardar_empleado(self):
        with open("empleados.txt", "w", encoding="utf-8") as archivo:
            for id_empleado, empleado in self.empleados.items():
                archivo.write(f"{id_empleado}:{empleado.nombre}:{empleado.departamento}:{empleado.telefono}:"
                              f"{empleado.direccion}:{empleado.correo}\n")

    def agregar_empleado(self, empleado: Empleados):
        if empleado.id_empleado not in self.empleados:
            self.empleados[empleado.id_empleado] = empleado
            self.guardar_empleado()
            print("Empleado registrado correctamente")
        else:
            raise ValueError("Ya existe un empleado con el mismo ID")

    def buscar_empleado(self, id_empleado):
        if id_empleado in self.empleados.keys():
            return self.empleados[id_empleado]
        return None

    def mostrar(self):
        if not self.empleados:
            print("No hay empleados registrados")
        else:
            for empleado in self.empleados.values():
                print(empleado)

    def despedir_empleado(self, id_empleado):
        if id_empleado in self.empleados:
            confirmacion = input("Ingrese contraseña de administrador: ")
            if confirmacion == "Administrador1215":
                print("Se despidió a ", self.empleados[id_empleado].nombre)
                del self.empleados[id_empleado]
            else:
                print("Contraseña no válida, no se despidió al empleado")
        else:
            print("No se encontró al empleado")


from datetime import datetime


class Ventas:
    def __init__(self, id_venta, fecha_hora=None, nit_cliente="", empleado=""):
        self.id_venta = id_venta
        self.fecha_hora = fecha_hora if fecha_hora else datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.nit_cliente = nit_cliente
        self.empleado = empleado
        self.detalles = []
        self.total = 0.0

    def agregar_detalle(self, detalle):
        self.detalles.append(detalle)
        self.total += detalle.subtotal

    def __str__(self):
        return (f"Venta No. {self.id_venta} | Fecha: {self.fecha_hora} | "
                f"NIT cliente: {self.nit_cliente} | Empleado: {self.empleado}")


class DetalleVenta:
    def __init__(self, id_detalle, id_venta, id_producto, precio, cantidad):
        self.id_detalle = id_detalle
        self.id_venta = id_venta
        self.id_producto = id_producto
        self.precio = precio
        self.cantidad = cantidad
        self.subtotal = precio * cantidad

    def __str__(self):
        return (f"Detalle {self.id_detalle} \nProducto: {self.id_producto}"
                f"\nCantidad: {self.cantidad} | Precio: Q{self.precio:.2f} \nSubtotal: Q{self.subtotal:.2f}")


class ControlVentas:
    def __init__(self):
        self.ventas = {}
        self.ultimo_id_venta = 0
        self.ultimo_id_detalle = 0
        self.cargar_ventas()

    def cargar_ventas(self):
        try:
            # Cargar ventas
            with open("ventas.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    id_venta, fecha_hora, nit_cliente, empleado = linea.strip().split(";")
                    venta = Ventas(id_venta, fecha_hora, nit_cliente, empleado)
                    self.ventas[id_venta] = venta

                    # Actualizar último ID
                    if id_venta.startswith("V"):
                        num = int(id_venta[1:])
                        self.ultimo_id_venta = max(self.ultimo_id_venta, num)

            # Cargar detalles
            with open("detalles_ventas.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    id_detalle, id_venta, id_producto, precio, cantidad = linea.strip().split(";")
                    detalle = DetalleVenta(id_detalle, id_venta, id_producto, float(precio), int(cantidad))
                    if id_venta in self.ventas:
                        self.ventas[id_venta].agregar_detalle(detalle)

                    # Actualizar último ID detalle
                    if id_detalle.startswith("DV"):
                        num = int(id_detalle[2:])
                        self.ultimo_id_detalle = max(self.ultimo_id_detalle, num)

        except FileNotFoundError:
            print("No existen archivos de ventas, se crearán al guardar")

    def guardar_ventas(self):
        with open("ventas.txt", "w", encoding="utf-8") as archivo:
            for venta in self.ventas.values():
                archivo.write(f"{venta.id_venta};{venta.fecha_hora};{venta.nit_cliente};{venta.empleado}\n")

        with open("detalles_ventas.txt", "w", encoding="utf-8") as archivo:
            for venta in self.ventas.values():
                for detalle in venta.detalles:
                    archivo.write(
                        f"{detalle.id_detalle};{detalle.id_venta};{detalle.id_producto};{detalle.precio};{detalle.cantidad}\n")

    def mostrar_resumen(self, num_venta):
        print("\n", self.ventas[num_venta])
        print("Detalles de venta:")
        for i in self.ventas[num_venta].detalles:
            print(i)
        print("Total: ", self.ventas[num_venta].total)

    def mostrar_historial(self):
        for venta in self.ventas.values():
            self.mostrar_resumen(venta.id_venta)

    def generar_id_venta(self):
        self.ultimo_id_venta += 1
        return f"V{self.ultimo_id_venta:03d}"

    def generar_id_detalle(self):
        self.ultimo_id_detalle += 1
        return f"DV{self.ultimo_id_detalle:03d}"


class DetalleCompra:
    def __init__(self, id_detalle, id_compra, id_producto, precio, cantidad):
        self.id_detalle = id_detalle
        self.id_compra = id_compra
        self.id_producto = id_producto
        self.precio = float(precio)
        self.cantidad = int(cantidad)

    def subtotal(self):
        return self.precio * self.cantidad

    def __str__(self):
        return (f"Detalle {self.id_detalle} \nProducto: {self.id_producto}"
                f"\nCantidad: {self.cantidad} | Precio de compra: Q{self.precio:.2f} \nSubtotal: Q{self.subtotal()}")


class Compra:
    def __init__(self, id_compra, fecha_hora=None, proveedor=None, empleado=None):
        self.id_compra = id_compra
        # Si no viene fecha, se asigna fecha actual
        self.fecha_hora = fecha_hora or datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.proveedor = proveedor
        self.empleado = empleado
        self.detalles = []

    def __str__(self):
        return (f"Venta No. {self.id_compra} | Fecha: {self.fecha_hora} | "
                f"ID proveedor: {self.proveedor} | Empleado: {self.empleado}")

    def agregar_detalle(self, detalle: DetalleCompra):
        self.detalles.append(detalle)

    def total(self):
        return sum(d.subtotal() for d in self.detalles)


class ControlCompras:
    def __init__(self):
        self.compras = {}
        self.ultimo_id_compra = 0
        self.ultimo_id_detalle = 0
        self.cargar_compras()

    def guardar_compras(self):
        with open("compras.txt", "w", encoding="utf-8") as archivo:
            for compra in self.compras.values():
                archivo.write(f"{compra.id_compra};{compra.fecha_hora};{compra.proveedor};{compra.empleado}\n")

        with open("detalles_compras.txt", "w", encoding="utf-8") as archivo:
            for compra in self.compras.values():
                for detalle in compra.detalles:
                    archivo.write(
                        f"{detalle.id_detalle};{detalle.id_compra};{detalle.id_producto};{detalle.precio};{detalle.cantidad}\n")

    def cargar_compras(self):
        try:
            # Cargar compras
            with open("compras.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    if linea.strip():
                        id_compra, fecha_hora, proveedor, empleado = linea.strip().split(";")
                        compra = Compra(id_compra, fecha_hora, proveedor, empleado)
                        self.compras[id_compra] = compra
                        # Actualizar último ID
                        if id_compra.startswith("C"):
                            num = int(id_compra[1:])
                            self.ultimo_id_compra = max(self.ultimo_id_compra, num)
        except FileNotFoundError:
            print("No existe compras.txt, se creará uno al guardar.")

        try:
            # Cargar detalles
            with open("detalles_compras.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    if linea.strip():
                        id_detalle, id_compra, id_producto, precio, cantidad = linea.strip().split(";")
                        detalle = DetalleCompra(id_detalle, id_compra, id_producto, precio, cantidad)
                        if id_compra in self.compras:
                            self.compras[id_compra].agregar_detalle(detalle)
                            # Actualizar último id_detalle
                            if id_detalle.startswith("DC"):  # si son tipo D001
                                num = int(id_detalle[2:])  # quitar la D y convertir a número
                                self.ultimo_id_detalle = max(self.ultimo_id_detalle, num)

        except FileNotFoundError:
            print("No existe detalles_compras.txt, se creará uno al guardar.")

    def mostrar_resumen(self, num_compra):
        print("\n", self.compras[num_compra])
        print("Detalles de venta:")
        for i in self.compras[num_compra].detalles:
            print(i)
        print("TOTAL: ", self.compras[num_compra].total())

    def mostrar_historial(self):
        for compra in self.compras.values():
            self.mostrar_resumen(compra.id_compra)

    def generar_id_compra(self):
        self.ultimo_id_compra += 1
        return f"C{self.ultimo_id_compra:03d}"

    def generar_id_detalle(self):
        self.ultimo_id_detalle += 1
        return f"DC{self.ultimo_id_detalle:03d}"


# MENÚ Principal

# import getpass

clientes = GestionCliente()
empleados = GestionEmpleado()
gestor_categorias = CrearCategoria()
proveedores = GestionProveedores()
inventario = Inventario()
ventas = ControlVentas()
compras = ControlCompras()

while True:
    print("---SISTEMA TIENDA---")
    print("1.Gestión de Empleados")
    print("2.Gestión de bodega")
    print("3.Ventas (cajero)")
    print("4.Mostrar historial")
    print("5.Salir")
    opcion = input("\nSeleccione una opcion: ")
    if opcion == "1":
        pin = input("Ingrese el PIN de acceso: ")
        if pin != "Admin123":
            print("❗Acceso no permitido, pin no válido")
            continue
        while True:
            print("--MENÚ Gestión de empleados--")
            print("1.Contratar empleado")
            print("2.Mostrar empleados")
            print("3.Despedir empleado")
            print("4.Salir")
            opcion = input("\nSeleccione una opcion: ")
            if opcion == "1":
                while True:
                    print("Contratar Empleado: ")
                    id_empleado = input("ID de emplead@: ")
                    if id_empleado in empleados.empleados.keys():
                        print("Ya existe un empleado con el id.")
                        continue
                    nombre = input("\tNombre: ")
                    while True:
                        departamento = input("\tDepartamento: ")
                        if departamento not in ["Coordinador de bodega", "Recursos Humanos", "Gerente", "Ventas"]:
                            print("Departamento no disponible")
                            continue
                        break
                    while True:
                        try:
                            telefono = int(input("\tTeléfono: "))
                            if telefono < 0:
                                print("Teléfono no válido")
                                continue
                            break
                        except ValueError as e:
                            print("Ha ocurrido un error", e)
                    direccion = input("\tDireccion: ")
                    correo = input("\tCorreo: ")
                    agregar_empleado = Empleados(id_empleado, nombre, departamento, telefono, direccion, correo)
                    empleados.agregar_empleado(agregar_empleado)
                    break
            elif opcion == "2":
                print("Empleados Registrados: ")
                empleados.mostrar()
            elif opcion == "3":
                id_empleado = input("Ingrese el ID del empleado que desea despedir: ")
                empleados.despedir_empleado(id_empleado)
            elif opcion == "4":
                print("Regresando al menú principal...")
                opcion = 0
                break
            else:
                print("Opción no disponible")


    elif opcion == "2":
        if not empleados.empleados:
            print("No hay personal registrado")
            continue
        encargado = empleados.buscar_empleado(input("Ingrese su ID de empleado: "))
        if encargado is None:
            print("El ID ingresado no existe")
            continue
        elif encargado.departamento != "Coordinador de bodega":
            print("El empleado no pertenece al departamento de cordinador de bodega, no puede ingresar a esta área")
            continue
        pin = input("Ingrese la contraseña de acceso: ")
        if pin != "CoBodega123":
            print("❗Acceso no permitido, contraseña no válida")
            continue
        while True:
            print("--MENÚ gestión de bodega--")
            print("1.Buscar/agregar proveedor")
            print("2.Comprar productos (actualizar stock)")
            print("3.Ver todos los productos")
            print("4.Modificar precios")
            print("5.Salir")
            opcion = input("\nSeleccione una opción: ")
            if opcion == "1":
                id_proveedor = input("Ingrese el ID del proveedor: ")
                buscar = proveedores.buscar(id_proveedor)
                if buscar is None:
                    confirmar = input("No existe el proveedor, ¿desea registrarlo? (S/N): ")
                    if confirmar.lower() == "s":
                        nombre = input("\tNombre: ")
                        empresa = input("\tEmpresa: ")
                        while True:
                            try:
                                telefono = int(input("\tTeléfono: "))
                                if telefono < 10000000:
                                    print("Número de telefono no válido")
                                    continue
                                break
                            except ValueError as e:
                                print("Ha ocurrido un error: ", e)
                        direccion = input("\tDireccion: ")
                        correo = input("\tCorreo: ")
                        id_categoria = input("\tId Categoría: ")
                        agregar_proveedor = Proveedores(id_proveedor, nombre, empresa, telefono, direccion, correo,
                                                        id_categoria)
                        proveedores.agregar_proveedor(agregar_proveedor)
                    elif confirmar.lower() == "n":
                        print("Regresando al menú...")
                        continue
                    else:
                        print("Confirmación no válida, regresando al menú...")
                        continue
                else:
                    print(buscar)
            elif opcion == "2":
                if not proveedores.proveedores:
                    print("Aún no hay proveedores, registre al menos uno en la opción 1")
                    continue
                num_compra = compras.generar_id_compra()
                id_proveedor = input("\tIngrese el Id del proveedor: ")
                if proveedores.buscar(id_proveedor) is None:
                    print("No se encontró al proveedor")
                    continue

                compra = Compra(num_compra, proveedor=id_proveedor, empleado=encargado.id_empleado)

                print("Realizar compras (ingrese 0 para finalizar):")
                while True:
                    id_detalle_compra = compras.generar_id_detalle()
                    codigo = input("Ingrese el código de producto: ")
                    if codigo == "0":
                        break

                    producto = inventario.buscar_producto("codigo", codigo)
                    if not producto:
                        confirmar = input("El producto no existe, ¿desea registrarlo? (S/N): ")
                        if confirmar.lower() == "s":
                            nombre_producto = input("\tNombre del producto: ")
                            while True:
                                id_categoria = input("\tId de categoria: ")
                                if gestor_categorias.buscar_categoria(id_categoria) is None:
                                    confirmar = input("La categoría no existe, ¿Desea registrarla? (S/N): ")
                                    if confirmar.lower() == "s":
                                        nombre_cat = input("\tNombre de la categoría: ")
                                        nueva_categoria = Categorias(id_categoria, nombre_cat)
                                        gestor_categorias.crear_categoria(nueva_categoria)
                                        break
                                    elif confirmar.lower() == "n":
                                        continue
                                else:
                                    break

                            while True:
                                try:
                                    precio = float(input("\tPrecio de venta: Q."))
                                    if precio <= 0:
                                        print("El precio debe ser mayor a 0")
                                        continue
                                    break
                                except ValueError:
                                    print("ERROR: Precio ingresado no válido")

                            producto = Productos(codigo, nombre_producto, id_categoria, precio, 0, 0, 0)
                            inventario.agregar_producto(producto)
                        else:
                            continue  # vuelve al menú

                    # aquí ya hay producto en inventario
                    while True:
                        try:
                            cantidad = int(input(f"\tCantidad a comprar: "))
                            if cantidad <= 0:
                                raise ValueError("La cantidad debe ser mayor a 0")

                            precio_compra = float(input("\tPrecio de compra: Q."))
                            if precio_compra <= 0:
                                raise ValueError("El precio debe ser mayor a 0")

                            detalle = DetalleCompra(id_detalle_compra, num_compra, codigo, precio_compra, cantidad)
                            compra.agregar_detalle(detalle)

                            # actualizar stock en inventario
                            inventario.actualizar_stock(codigo, cantidad, "compra")
                            inventario.guardar_productos()

                            break
                        except ValueError as e:
                            print("Ha ocurrido un error:", e)
                compras.compras[num_compra] = compra
                compras.guardar_compras()
                compras.mostrar_resumen(num_compra)
                print("Compras realizadas correctamente")

            elif opcion == "3":
                clave = input("Ordenar por (codigo, nombre, categoria): ").lower()
                if clave not in ["nombre", "precio", "categoria"]:
                    print("Orden no valido, se ordenará por nombre")
                    clave = "nombre"
                productos = inventario.listar_productos(clave)
                if productos:
                    for p in productos:
                        print(p)
                else:
                    print("No se encontraron productos")
            elif opcion == "4":
                if not inventario.inventario:
                    print("No hay productos registrados")
                    continue

                while True:
                    try:
                        codigo = input("Ingrese el código del producto: ")
                        nuevo_precio = float(input("Ingrese el nuevo precio: Q."))
                        inventario.actualizar_precio(codigo, nuevo_precio)
                        break
                    except ValueError as e:
                        print("Ha ocurrido un error: ", e)
            elif opcion == "5":
                print("Regresando al menú principal")
                opcion = 0
                break


    elif opcion == "3":
        if not inventario.inventario:
            print("No se ha realizado ninguna compra de productos")
            continue
        encargado = input("Ingrese su ID de empleado: ")
        buscar = empleados.buscar_empleado(encargado)
        if buscar is None or buscar.departamento.lower() != "ventas":
            print("No existe el ID ingresado o no pertenece al departamento de ventas")
            continue
        pin = input("Ingrese el contraseña de acceso: ")
        if pin != "Ventas123":
            print("❗Acceso no permitido, contraseña incorrecta")
            continue
        while True:
            print("--MENÚ Ventas (Cajero)--")
            print("1.Cobrar")
            print("2.Buscar producto")
            print("3.Salir")
            opcion = input("\nSeleccione una opción: ")
            if opcion == "1":
                num_venta = ventas.generar_id_venta()
                nit = input("Ingrese NIT del cliente: ")
                if nit.lower() != "cf":
                    cliente = clientes.buscar_cliente(nit)
                    if cliente is None:
                        confirmar = input("El NIT ingresado no está registrado, ¿desea registrarlo? (S/N): ").lower()
                        if confirmar == "s":
                            nombre = input("\tNombre: ")
                            while True:
                                try:
                                    telefono = int(input("\tTeléfono: "))
                                    if telefono < 10000000:
                                        raise ValueError("Número de teléfono no válido")
                                    direccion = input("\tDirección: ")
                                    correo = input("\tCorreo: ")
                                    cliente = Clientes(nit, nombre, direccion, telefono, correo)
                                    clientes.agregar_cliente(nit, cliente)
                                    break
                                except ValueError as e:
                                    print("Ha ocurrido un error: ", e)
                        elif confirmar == "n":
                            continue
                        else:
                            print("Confirmación no válida")
                            continue
                venta = Ventas(num_venta, datetime.now().strftime("%d/%m/%Y %H:%M:%S"), nit, encargado)

                print("Ingrese los productos (ingrese 0 para finalizar):")
                while True:
                    id_detalle_venta = ventas.generar_id_detalle()
                    codigo = input("Código del producto: ")
                    if codigo == "0":
                        break
                    producto = inventario.buscar_producto("codigo", codigo)
                    if producto is None:
                        print("No existe ningún producto código ingresado")
                        continue
                    while True:
                        try:
                            cantidad = int(input("\tCantidad: "))
                            if cantidad < 0:
                                raise ValueError("La cantidad debe ser mayo a 0")
                            crear_detalle = DetalleVenta(id_detalle_venta, num_venta,
                                                         inventario.inventario[codigo].id_producto,
                                                         inventario.inventario[codigo].precio,
                                                         cantidad)
                            venta.agregar_detalle(crear_detalle)
                            inventario.actualizar_stock(codigo, cantidad, "venta")
                            break
                        except ValueError as e:
                            print("Ha ocurrido un error: ", e)
                ventas.ventas[num_venta] = venta
                ventas.guardar_ventas()
                ventas.mostrar_resumen(num_venta)

            elif opcion == "2":
                print("--BUSCAR PRODUCTO--")
                clave = input("Buscar por (codigo, nombre, categoria): ").lower()
                valor = input(f"Ingrese el/la {clave} del producto: ")
                resultados = inventario.buscar_producto(clave, valor)
                if resultados:
                    for p in resultados:
                        print(p)
                else:
                    print("No se encontró ningún producto")
            elif opcion == "3":
                print("Regresando al menú principal")
                break
            else:
                print("Opción no disponible")

    elif opcion == "4":
        while True:
            print("--MENÚ HISTORIAL--")
            print("1.Historial de compras")
            print("2.Historial de ventas")
            print("3.Salir")
            opcion = input("\nSeleccione una opción: ")
            if opcion == "1":
                compras.mostrar_historial()
            elif opcion == "2":
                ventas.mostrar_historial()
            elif opcion == "3":
                break
            else:
                print("Opción no válida")

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
