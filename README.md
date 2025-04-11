# 🧪 Automatización de Pruebas con Selenium - SauceDemo

Este proyecto muestra una prueba automatizada utilizando **Python + Selenium WebDriver**, sobre la página de pruebas [SauceDemo](https://www.saucedemo.com/).  
Incluye capturas de evidencia, reporte HTML, y un video demostrativo.

---

# Historias de Usuario – Proyecto de Prueba Automatizada con Selenium

## Historia 1: Iniciar sesión correctamente

**Como** usuario,  
**quiero** poder iniciar sesión con credenciales válidas  
**para** acceder a mis productos.\*\*

### ✅ Criterios de Aceptación

- El sistema permite el acceso si el usuario y contraseña son correctos.
- La página de productos se muestra tras iniciar sesión.

### ❌ Criterios de Rechazo

- Si los campos están vacíos o incorrectos, se muestra un mensaje de error.
- El usuario no puede acceder a la siguiente página sin credenciales válidas.

---

## Historia 2: Ver el detalle de un producto

**Como** comprador,  
**quiero** ver la información detallada de un producto  
**para** decidir si lo compro.

### ✅ Criterios de Aceptación

- Se puede hacer clic en el nombre de cualquier producto.
- Se muestra una nueva página con descripción, imagen y precio del producto.

### ❌ Criterios de Rechazo

- Si el producto no carga correctamente, debe mostrarse un mensaje de error.
- El botón de regreso a la tienda debe estar visible y funcional.

---

## Historia 3: Agregar un producto al carrito

**Como** usuario registrado,  
**quiero** agregar productos al carrito  
**para** comprarlos más adelante.

### ✅ Criterios de Aceptación

- El botón “Add to cart” funciona correctamente.
- El ícono del carrito se actualiza con la cantidad de productos añadidos.

### ❌ Criterios de Rechazo

- Si no hay stock, debe avisar que no se puede agregar.
- No se puede agregar el mismo producto varias veces desde la misma vista.

---

## Historia 4: Ver el carrito de compras

**Como** comprador,  
**quiero** ver el contenido del carrito  
**para** revisar lo que he seleccionado.

### ✅ Criterios de Aceptación

- El carrito muestra todos los productos añadidos.
- El botón para continuar al checkout debe estar disponible.

### ❌ Criterios de Rechazo

- Si el carrito está vacío, debe indicarse con un mensaje claro.
- No se debe permitir proceder sin productos seleccionados.

---

## Historia 5: Cerrar sesión

**Como** usuario,  
**quiero** cerrar sesión desde el menú  
**para** proteger mi cuenta en equipos compartidos.

### ✅ Criterios de Aceptación

- El botón de logout está accesible desde el menú lateral.
- Al hacer clic en logout, se redirige correctamente a la página de login.

### ❌ Criterios de Rechazo

- Si hay un error al cerrar sesión, debe notificarse al usuario.
- El usuario no debe permanecer logueado tras hacer logout.

---

## ⚙️ Tecnologías usadas

- Python 3.x
- Selenium
- ChromeDriver
- pytest + pytest-html (para reportes)
- OBS (para video demo)

---

## 📂 Estructura del Proyecto

```
📁 PruebaSelenium/
├── prueba_selenium.py
├── evidencias/
│   ├── 01_login_page.png
│   ├── 02_logged_in.png
│   └── ...
├── reporte.html
├── video_demo.mp4 (opcional, si lo subiste)
└── README.md
```

---

## ▶️ Ejecución de la prueba

1. Clona el repositorio
2. Instala los requerimientos:
   ```
   pip install selenium pytest pytest-html
   ```
3. Asegúrate de tener `chromedriver.exe` en la raíz del proyecto
4. Ejecuta el script:
   ```
   python prueba_selenium.py
   ```

---

## 📷 Evidencias

Se generan capturas automáticamente en la carpeta `evidencias/`.

---

## 📊 Reporte HTML

El reporte de la ejecución de pruebas se encuentra en el archivo `reporte.html`.

---

## 🎥 Video Demostrativo

Puedes ver la ejecución completa en el video `video_demo.mp4`.

---

## 🧑‍💻 Autor

**Luis Elian Pérez (2021-0119)**  
Proyecto para evaluación académica - Automatización de Pruebas
