import barcode
import qrcode
from barcode.writer import ImageWriter
from PIL import Image

# Genera el código de barras
def generate_barcode(data, bar_color=(0, 0, 0), bg_color=(255, 255, 255), output_file="barcode.png"):
    """
    Genera un código de barras con colores personalizados.
    
    :param data: String de datos a codificar en el código de barras.
    :param bar_color: Color de las barras en formato (R, G, B).
    :param bg_color: Color de fondo en formato (R, G, B).
    :param output_file: Nombre del archivo de salida.
    """
    # Asegurarse de que el archivo no tenga la extensión duplicada
    if output_file.endswith(".png"):
        output_file = output_file[:-4]  # Quitar la extensión .png si ya está en el nombre

    # Crea el código de barras Code128 con el writer de imagen, sin el texto debajo
    code128 = barcode.get("code128", data, writer=ImageWriter())

    # Configura que no muestre el texto debajo del código de barras
    options = {
        "write_text": False  # Desactiva el texto plano debajo del código de barras
    }

    # Genera el código de barras y lo guarda como imagen (python-barcode agrega .png)
    code128.save(output_file, options)

    # Abre la imagen generada
    img = Image.open(f"{output_file}.png")

    # Modifica los colores de fondo y de las barras
    img = img.convert("RGBA")
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


def generate_qr_code(data, bar_color=(0, 0, 0), bg_color=(255, 255, 255), output_file="qr_code.png"):
    """
    Genera un código QR con colores personalizados.
    
    :param data: String de datos a codificar en el código QR.
    :param bar_color: Color de las barras en formato (R, G, B).
    :param bg_color: Color de fondo en formato (R, G, B).
    :param output_file: Nombre del archivo de salida.
    """
    # Crear el código QR
    qr = qrcode.QRCode(
        version=1,  # Version 1: 21x21 matrix (puede cambiar según tamaño del dato)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nivel de corrección de errores
        box_size=10,  # Tamaño de cada caja
        border=1,  # Tamaño del borde
    )
    qr.add_data(data)  # Añadir los datos al QR
    qr.make(fit=True)

    # Crear imagen QR con colores personalizados
    img = qr.make_image(fill_color=bar_color, back_color=bg_color).convert("RGBA")

    # Guardar la imagen del código QR
    img.save(output_file)