# 🧪 Automatización de Pruebas con Selenium - SauceDemo

Este proyecto muestra una prueba automatizada utilizando **Python + Selenium WebDriver**, sobre la página de pruebas [SauceDemo](https://www.saucedemo.com/).  
Incluye capturas de evidencia, reporte HTML, y un video demostrativo.

---

## 📋 Historias de Usuario

### Historia de Usuario 1

**Como** usuario del sistema  
**Quiero** iniciar sesión correctamente  
**Para** acceder a los productos disponibles

**Criterios de aceptación:**

- Ingresar usuario y contraseña válidos
- Redirigir al inventario
- Mostrar productos

---

### Historia de Usuario 2

**Como** usuario del sistema  
**Quiero** poder ver el detalle de un producto  
**Para** conocer más información antes de comprar

**Criterios de aceptación:**

- Click sobre el nombre del producto
- Redirige a la vista de detalle
- Mostrar botón para agregar al carrito

---

### Historia de Usuario 3

**Como** usuario del sistema  
**Quiero** agregar productos al carrito y verlos  
**Para** confirmar mi selección antes de pagar

**Criterios de aceptación:**

- Botón de agregar debe funcionar
- Click en el ícono del carrito lleva al resumen
- Producto seleccionado debe estar listado

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
