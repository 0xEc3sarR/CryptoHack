from PIL import Image

# abrir las dos imagenes
ima1 = Image.open("flag_7ae18c704272532658c10b5faad06d74.png").convert("RGB")
ima2 = Image.open("lemur_ed66878c338e662d3473f0d98eedbd0d.png").convert("RGB")

# asegurar que tienen el mismo size
if ima1.size != ima2.size:
    raise ValueError("Las imagenes deben tener el mismo size")

# obtener los pixeles como listas de tuplas (R, G, B)
pixels1 = list(ima1.getdata())
pixels2 = list(ima2.getdata())

# aplicar XOR a cada componente de cada pixel
pixels_xor = [
    (r1 ^ r2, g1 ^ g2, b1 ^ b2) for (r1, g1, b1), (r2, g2, b2) in zip(pixels1, pixels2)
]

# crear una nueva imagen con los pixeles resultados
img_xor = Image.new("RGB", ima1.size)
img_xor.putdata(pixels_xor)

# guardar o mostrar la imagen
img_xor.save("xor.png")
img_xor.show()
