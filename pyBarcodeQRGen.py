import barcode
from barcode.writer import ImageWriter
from PIL import Image

# Genera el código de barras
def generate_barcode(data, bar_color=(0, 0, 0), bg_color=(255, 255, 255), output_file='barcode.png'):
    # Asegurarse de que el archivo no tenga la extensión duplicada
    if output_file.endswith('.png'):
        output_file = output_file[:-4]  # Quitar la extensión .png si ya está en el nombre

    # Crea el código de barras Code128 con el writer de imagen, sin el texto debajo
    code128 = barcode.get('code128', data, writer=ImageWriter())

    # Configura que no muestre el texto debajo del código de barras
    options = {
        'write_text': False  # Desactiva el texto plano debajo del código de barras
    }

    # Genera el código de barras y lo guarda como imagen (python-barcode agrega .png)
    code128.save(output_file, options)

    # Abre la imagen generada
    img = Image.open(f"{output_file}.png")

    # Modifica los colores de fondo y de las barras
    img = img.convert('RGBA')
    datas = img.getdata()

    new_data = []
    for item in datas:
        # Cambia el color de las barras (negro por defecto)
        if item[:3] == (0, 0, 0):  # color original de las barras (negro)
            new_data.append((*bar_color, 255))  # nuevo color de barras
        else:
            new_data.append((*bg_color, 255))  # nuevo color de fondo

    img.putdata(new_data)
    img.save(f"{output_file}.png")