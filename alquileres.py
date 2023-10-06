import requests
from bs4 import BeautifulSoup

# URL de la página de alquileres en Clasificados La Voz
html_text = requests.get('https://clasificados.lavoz.com.ar/inmuebles/todo?operacion=alquileres').text
# print(html_text)

# Extraer el contenido HTML de la página web
soup = BeautifulSoup(html_text, 'lxml')
# print(soup)

# Extraer la cantidad de alquileres
def extraer_alquileres(soup):
    div_alquileres = soup.find_all('div', class_='mx1 px2 py05')
    alquileres_lista = []

    for i, div in enumerate(div_alquileres):
        alquileres = div.find('a')
        if alquileres:
            cant_alquileres = alquileres.text.strip()
            alquileres_lista.append(cant_alquileres)
            # print(f"{i}: {cant_alquileres}")
        else:
            print(f"No se encontró la etiqueta <a> dentro del div {i}.")

    return alquileres_lista

# Llamas a la función para obtener la lista de alquileres
alquileres_lista = extraer_alquileres(soup)

# Índices de los alquileres que deseas seleccionar
tipos = [2, 4]

# Creas una lista para almacenar los alquileres seleccionados por índice
alquileres_seleccionados = []

# Recorres la lista de índices deseados
def filtrar_alquileres(alquileres_lista, tipos):
    alquileres_seleccionados = []

    for indice in tipos:
        # Verifica si el índice está dentro del rango de la lista
        if 0 <= indice < len(alquileres_lista):
            alquiler_seleccionado = alquileres_lista[indice]
            alquileres_seleccionados.append(alquiler_seleccionado)
        else:
            print(f"El índice {indice} está fuera del rango de la lista de alquileres.")

    return alquileres_seleccionados

# Llamas a la función para seleccionar alquileres por índices
tipos_alquileres = filtrar_alquileres(alquileres_lista, tipos)

# Imprimes la lista de alquileres seleccionados
print("Tipos de alquileres:")
print(tipos_alquileres)
