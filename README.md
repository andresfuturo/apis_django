
 API de Automóviles - Proyecto Django

Descripción
Este proyecto es una API REST desarrollada con Django y Django Rest Framework para gestionar automóviles. Permite realizar las siguientes acciones sobre los automóviles: registrar, consultar, actualizar y eliminar, todo desde una base de datos.

 Tecnologías utilizadas
- **Python 3.11**
- **Django 5.2**
- **Django Rest Framework**

 Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/ANDRES-FLORIAN-SALAZAR/PUNTOEXTRA.git
   cd gestion-automoviles
   ```

2. **Crear y activar un entorno virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate     # Para Windows
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar la base de datos**
   Ejecuta las migraciones para configurar la base de datos:
   ```bash
   python manage.py migrate
   ```

5. **Ejecutar el servidor**
   ```bash
   python manage.py runserver
   ```

La API estará disponible en: `http://127.0.0.1:8000/api/`

---

 Modelos

### Modelo `Automovil`
El modelo `Automovil` representa los automóviles registrados en el sistema.

Atributos:
- nombre Nombre comercial del automóvil.
- marca Marca del fabricante (ej. Toyota, Ford).
- modelo Año o versión del automóvil.
- diseño Tipo de diseño (Sedán, SUV, Hatchback, etc).
- cilindrajeCilindraje del motor en centímetros cúbicos (cc).

### Modelo `Cliente`
Este modelo define a un cliente con los siguientes atributos:

- nombre: Nombre del cliente.
- email: Correo electrónico del cliente.
- telefono: Teléfono de contacto del cliente (opcional).
- direccion: Dirección del cliente (opcional).

### Modelo `Venta`
Este modelo define una venta con los siguientes atributos:

- cliente: Referencia al cliente que realiza la compra.
- automovil: Referencia al automóvil comprado.
- fecha_venta: Fecha de la venta, generada automáticamente.
- precio_final: Precio final de la venta.





---

## 🔥 Funcionamiento de la API REST

Base URL de la API:
```
http://127.0.0.1:8000/api/
```

---

## 📍 Endpoints disponibles

### 1. Obtener lista de automóviles
- **Método:** `GET`
- **URL:** `/api/automoviles/`
- **Descripción:** Retorna una lista de todos los automóviles registrados en la base de datos.

**Ejemplo de respuesta:**
```json
[
    {
        "id": 2,
        "nombre": "txt2",
        "marca": "toyoyra",
        "modelo": 2000,
        "diseño": "2000",
        "cilindraje": 2000
    },
    {
        "id": 3,
        "nombre": "cccc",
        "marca": "mazda",
        "modelo": 20,
        "diseño": "20",
        "cilindraje": 20
    }
]
```

---

### 2. Crear un nuevo automóvil
- **Método:** `POST`
- **URL:** `/api/automoviles/`
- **Descripción:** Crea un nuevo automóvil en la base de datos.

**Ejemplo de cuerpo de solicitud:**
```json
{
    "nombre": "Nuevo Automóvil",
    "marca": "Honda",
    "modelo": 2022,
    "diseño": "Sedán",
    "cilindraje": 1500
}
```

---

### 3. Obtener un automóvil específico
- **Método:** `GET`
- **URL:** `/api/automoviles/{id}/`
- **Descripción:** Devuelve los detalles de un automóvil utilizando su ID.

**Ejemplo de solicitud:**
```
GET http://127.0.0.1:8000/api/automoviles/3/
```

**Ejemplo de respuesta:**
```json
{
    "id": 3,
    "nombre": "cccc",
    "marca": "mazda",
    "modelo": 20,
    "diseño": "20",
    "cilindraje": 20
}
```

---

### 4. Actualizar un automóvil
- **Método:** `PUT`
- **URL:** `/api/automoviles/{id}/`
- **Descripción:** Actualiza los detalles de un automóvil utilizando su ID.

**Ejemplo de cuerpo de solicitud:**
```json
{
    "nombre": "Nuevo nombre",
    "marca": "Nueva marca",
    "modelo": 2023,
    "diseño": "SUV",
    "cilindraje": 1800
}
```

---

### 5. Eliminar un automóvil
- **Método:** `DELETE`
- **URL:** `/api/automoviles/{id}/`
- **Descripción:** Elimina un automóvil utilizando su ID.

**Ejemplo de solicitud:**
```
DELETE http://127.0.0.1:8000/api/automoviles/3/
```

---

## 📂 Estructura del proyecto

```
edgar/
├── patinoApp/           # Gestión de automóviles
│   ├── static/         
│   ├── templates/      
│   ├── models.py        # Modelos de datos
│   └── views.py         # Lógica de la aplicación
├── ventasApp/           # Gestión de ventas
│   ├── static/         
│   ├── templates/      
│   ├── models.py        # Modelos de datos
│   └── views.py         # Lógica de la aplicación
├── clienteApp/          # Gestión de clientes
│   ├── static/         
│   ├── templates/      
│   ├── models.py        # Modelos de datos
│   └── views.py         # Lógica de la aplicación
├── manage.py            # Script de gestión de Django
└── requirements.txt     # Dependencias del proyecto
```

---


