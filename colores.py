from PIL import Image, ImageDraw, ImageFont

# Definimos los colores en HEX y sus nombres
colors = {
    "Original": "#00B4E6",
    "Azul claro suave": "#66CBEF",
    "Azul grisáceo": "#99D6EB",
    "Azul pastel": "#B3E4F2",
    "Azul medio apagado": "#33A9D1"
}

# Crear una imagen en blanco
width = 600
height = 60 * len(colors)
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Dibujar bloques de colores con etiquetas
for i, (name, hex_color) in enumerate(colors.items()):
    y = i * 60
    draw.rectangle([0, y, 100, y + 60], fill=hex_color)
    draw.text((110, y + 20), f"{name} - {hex_color}", fill="black")

# Mostrar imagen
image.show()

# Guardar para mostrar en ChatGPT
image_path = "/mnt/data/colores_azules_suaves.png"
image.save(image_path)

image_path
