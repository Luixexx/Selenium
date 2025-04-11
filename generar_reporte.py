import os

# Datos de pasos
pasos = [
    "01_login_page.png - Página de inicio cargada correctamente",
    "02_logged_in.png - Login exitoso y productos visibles",
    "03_product_detail.png - Detalle de producto desplegado",
    "04_added_to_cart.png - Producto agregado al carrito",
    "05_cart.png - Producto visible en el carrito"
]

# Crear HTML
html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Reporte de Pruebas - Selenium</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        h1 { color: #333; }
        .paso { margin-bottom: 40px; }
        .paso img { width: 500px; border: 1px solid #ccc; }
        .estado { color: green; font-weight: bold; }
    </style>
</head>
<body>
    <h1>Reporte de Evidencias - Prueba Automatizada</h1>
"""

for paso in pasos:
    archivo, descripcion = paso.split(" - ", 1)
    ruta = os.path.join("evidencias", archivo)
    if os.path.exists(ruta):
        html += f"""
        <div class="paso">
            <h2>{descripcion}</h2>
            <img src="{ruta}" alt="{descripcion}">
            <p class="estado">✅ Paso ejecutado correctamente</p>
        </div>
        """
    else:
        html += f"""
        <div class="paso">
            <h2>{descripcion}</h2>
            <p class="estado" style="color:red;">❌ No se encontró la evidencia: {archivo}</p>
        </div>
        """

html += """
</body>
</html>
"""

# Guardar el archivo
with open("reporte.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Reporte generado como 'reporte.html'")
