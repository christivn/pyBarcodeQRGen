import pyBarcodeQRGen

# Barcode Generation Example
if __name__ == "__main__":
    data = 'MiStringAlfanumerico'  # Cualquier string que quieras almacenar
    bar_color = (0, 0, 255)  # Color de las barras: azul
    bg_color = (255, 255, 0)  # Color de fondo: amarillo
    output_file = "barcode-example.png" # output filename

    pyBarcodeQRGen.generate_barcode(data, bar_color, bg_color, output_file)
    print(f"Código de barras guardado en {output_file}")