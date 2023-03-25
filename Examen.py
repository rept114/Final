def obtener_categoria_pelicula():
    categorias = {
        1: {"nombre": "Acción", "precio": 5},
        2: {"nombre": "Aventura", "precio": 4},
        3: {"nombre": "Comedia", "precio": 3},
        4: {"nombre": "Drama", "precio": 4.5},
        5: {"nombre": "Romance", "precio": 3.5},
        6: {"nombre": "Terror", "precio": 5.5},
        7: {"nombre": "Ciencia Ficción", "precio": 6},
        8: {"nombre": "Fantasía", "precio": 4.5},
        9: {"nombre": "Musical", "precio": 5},
        10: {"nombre": "Documental", "precio": 2.5}
    }

    print("Categorías de películas disponibles:")
    for codigo, categoria in categorias.items():
        print(f"{codigo} - {categoria['nombre']} (${categoria['precio']} por día)")

    codigo = int(input("Ingrese el código de la categoría de la película que desea: "))
    return categorias[codigo]


def calcular_precio_alquiler(categoria, dias):
    return categoria["precio"] * dias


def main():
    categoria = obtener_categoria_pelicula()
    dias = int(input("Ingrese el número de días que desea alquilar la película: "))
    precio_total = calcular_precio_alquiler(categoria, dias)

    print(f"El precio total a pagar por el alquiler de la película es: ${precio_total}")


if __name__ == '__main__':
    main()