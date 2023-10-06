import requests
from bs4 import BeautifulSoup

# URL de la página de alquileres de casas en Clasificados La Voz
html_text_casas = requests.get('https://clasificados.lavoz.com.ar/inmuebles/casas?operacion=alquileres').text
# print(html_text)

# Extraer el contenido HTML de la página web
soup = BeautifulSoup(html_text_casas, 'lxml')
# print(soup)

print('Provincias:')

# Extraer lista de alquileres por provincias
def extraer_alquileres_provincias(soup):
    div_provincias = soup.find_all('div', id='provincias')
    alquileres_provincias = []

    for i, div in enumerate(div_provincias):
        provincias = div.find('a')
        if provincias:
            cant_provincias = provincias.text.strip()
            alquileres_provincias.append(cant_provincias)
            print(f'{i}: {cant_provincias}')
        else:
            print(f'No se encontró la etiqueta <a> dentro del div {i}.')

    return alquileres_provincias

def filtrar_alquileres_provincias(alquileres_provincias, indice):
    if 0 <= indice < len(alquileres_provincias):
        provincia_seleccionada = alquileres_provincias[indice]
        return [provincia_seleccionada]
    else:
        print(f'El índice {indice} está fuera del rango de la lista de alquileres por provincias.')
        return []

# Llamas a la función para obtener la lista de alquileres por provincias
alquileres_provincias = extraer_alquileres_provincias(soup)

# Capturas el índice de la provincia que el usuario desea seleccionar
indice_provincia = input('\nIngrese el índice de la provincia que desea seleccionar: ')

# Verifica si la entrada del usuario es un número entero
if indice_provincia.isdigit():
    indice_provincia = int(indice_provincia)
    if 0 <= indice_provincia < len(alquileres_provincias):
        provincia_seleccionada = filtrar_alquileres_provincias(alquileres_provincias, indice_provincia)
        print('Provincia seleccionada:')
        print(provincia_seleccionada)
    else:
        print('El índice está fuera del rango de la lista de alquileres por provincias.')
else:
    print('Por favor, ingrese un valor numérico válido para el índice.')

# Lista de provincias
provincias = [
    "Córdoba",
    "Mendoza",
    "GBA-Zona-Norte",
    "Buenos-Aires",
    "GBA-Zona-Oeste",
    "GBA-Zona-Sur",
    "Buenos-Aires-Costa-Atlantica",
    "Salta",
    "Capital-Federal",
    "Neuquén",
    "Entre-Rios",
    "Santa-Fe",
    "Chaco",
    "Misiones",
    "Rio-Negro",
    "San-Juan"
]

int_indice_provincia = int(indice_provincia)
provincia = provincias[int_indice_provincia]

# Convierte el nombre de la provincia a minúsculas y elimina los espacios
t_provincia = provincia.lower().replace(" ", "")

# Construye la URL con la variable t_provincia
url = f'https://clasificados.lavoz.com.ar/inmuebles/casas?list=true&operacion=alquileres&provincia={t_provincia}'

# URL de la página de alquileres de casas por ciudades en Clasificados La Voz
html_text_ciudades = requests.get(url).text

# Extraer el contenido HTML de la página web
soup = BeautifulSoup(html_text_ciudades, 'lxml')

print('\nCiudades:')

# Extraer lista de alquileres de ciudades
def extraer_alquileres_ciudades(soup):
    div_ciudades = soup.find_all('div', id='ciudades')
    alquileres_ciudades = []

    for i, div in enumerate(div_ciudades):
        ciudades = div.find('a')
        if ciudades:
            cant_ciudades = ciudades.text.strip()
            alquileres_ciudades.append(cant_ciudades)
            print(f'{i}: {cant_ciudades}')
        else:
            print(f'No se encontró la etiqueta <a> dentro del div {i}.')

    return alquileres_ciudades

# Llamas a la función para obtener la lista de alquileres por ciudades
alquileres_ciudades = extraer_alquileres_ciudades(soup)
