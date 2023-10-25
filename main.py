import requests
from bs4 import BeautifulSoup
from unidecode import unidecode
import re
import lxml.html as html

# Extraer inmuebles
def extraer_inmuebles():
    url = 'https://clasificados.lavoz.com.ar/inmuebles/todo?'
    tipos = [1,2,3,4,6,7,8,9]

    html_text_inmuebles = requests.get(url).text
    soup = BeautifulSoup(html_text_inmuebles, 'lxml')

    inmuebles = soup.find_all('div', class_='mx1 px2 py05')
    inmuebles_seleccionados = []

    for i, inmueble in enumerate(inmuebles):
        tipo_inmueble = inmueble.find('a')
        if tipo_inmueble:
            inmueble_texto = tipo_inmueble.text.strip()
            inmuebles_seleccionados.append(inmueble_texto)
        else:
            print(f'No se encontró la etiqueta <a> dentro del div {i}.')

    inmuebles_filtrados = [inmuebles_seleccionados[indice] for indice in tipos if indice < len(inmuebles_seleccionados)]
    return inmuebles_filtrados

print('Inmuebles:')
print(extraer_inmuebles())
inmuebles_filtro = extraer_inmuebles()

def convertir_lista(lista):
    lista_nueva = []
    for string in lista:
        string_modificado = unidecode(string.lower().replace(' ', '-'))
        string_modificado = re.sub(r'\([^)]*\)', '', string_modificado)
        string_modificado = string_modificado.rstrip('-')
        lista_nueva.append(string_modificado)
    return lista_nueva

lista_tipos_inmuebles = extraer_inmuebles()
lista_inmuebles = convertir_lista(lista_tipos_inmuebles)

def seleccionar(lista, indice):
    if indice.isdigit():
        indice = int(indice)
        if 0 <= indice < len(lista):
            seleccionado = lista[indice]
            return seleccionado
        else:
            return 'El índice está fuera del rango de la lista.'
    else:
        return 'Ingrese un valor numérico válido para el índice.'

seleccionar_inmueble = input('\nSeleccione subrubro: ')
print(inmuebles_filtro[int(seleccionar_inmueble)])
subrubro = seleccionar(lista_inmuebles, seleccionar_inmueble)

def construir_url_subrubro(subrubro):
    url = f'https://clasificados.lavoz.com.ar/inmuebles/{subrubro}'
    return url

url_subrubro = construir_url_subrubro(subrubro)

# Extraer operaciones
def extraer_operaciones(url, palabras_clave):
    html_text_operaciones = requests.get(url).text
    soup = BeautifulSoup(html_text_operaciones, 'lxml')

    operaciones = soup.find_all('div', class_='mx1 px2 py05')
    operaciones_seleccionados = []

    for i, operacion in enumerate(operaciones):
        tipo_operacion = operacion.find('a')
        if tipo_operacion:
            operacion_texto = tipo_operacion.text.strip()
            for palabra_clave in palabras_clave:
                if palabra_clave in operacion_texto:
                    operaciones_seleccionados.append(operacion_texto)
                    break
        else:
            print(f'No se encontró la etiqueta <a> dentro del div {i}.')

    return operaciones_seleccionados

palabras_clave = ['Alquileres', 'Venta', 'Compra']
operaciones_filtradas = extraer_operaciones(url_subrubro, palabras_clave)

print('\nOperaciones:')
print(extraer_operaciones(url_subrubro, palabras_clave))
operacion_filtro = extraer_operaciones(url_subrubro, palabras_clave)

lista_alquileres_operaciones = extraer_operaciones(url_subrubro, palabras_clave)
lista_operaciones = convertir_lista(lista_alquileres_operaciones)

seleccionar_operacion = input('\nSeleccione la operación: ')
print(operacion_filtro[int(seleccionar_operacion)])
operacion = seleccionar(lista_operaciones, seleccionar_operacion)

def construir_url_operacion(subrubro,operacion):
    url = f'https://clasificados.lavoz.com.ar/inmuebles/{subrubro}?operacion={operacion}'
    return url

url_operacion = construir_url_operacion(subrubro,operacion)

# Extraer provincias
def extraer_provincias(url):

    html_text_provincias = requests.get(url).text
    soup = BeautifulSoup(html_text_provincias, 'lxml')

    div_provincias = soup.find_all('div', id='provincias')
    alquileres_provincias = []

    for i, div in enumerate(div_provincias):
        provincias = div.find('a')
        if provincias:
            cant_provincias = provincias.text.strip()
            alquileres_provincias.append(cant_provincias)
        else:
            print(f'No se encontró la etiqueta <a> dentro del div {i}.')

    return alquileres_provincias

print('\nProvincias:')
print(extraer_provincias(url_operacion))
provincia_filtro = extraer_provincias(url_subrubro)

lista_alquileres_provincias = extraer_provincias(url_subrubro)
lista_provincias = convertir_lista(lista_alquileres_provincias)

seleccionar_provincia = input('\nSeleccione la provincia: ')
print(provincia_filtro[int(seleccionar_provincia)])
provincia = seleccionar(lista_provincias, seleccionar_provincia)

def construir_url_provincia(subrubro,operacion,provincia):
    url = f'https://clasificados.lavoz.com.ar/inmuebles/{subrubro}?operacion={operacion}&provincia={provincia}'
    return url

url_provincia = construir_url_provincia(subrubro,operacion,provincia)

# Extraer Ciudades
def extraer_ciudades(url):

        html_text_ciudades = requests.get(url).text
        soup = BeautifulSoup(html_text_ciudades, 'lxml')

        div_ciudades = soup.find_all('div', id='ciudades')
        alquileres_ciudades = []

        for i, div in enumerate(div_ciudades):
            ciudades = div.find('a')
            if ciudades:
                cant_ciudades = ciudades.text.strip()
                alquileres_ciudades.append(cant_ciudades)
            else:
                print(f'No se encontró la etiqueta <a> dentro del div {i}.')

        return alquileres_ciudades

print('\nCiudades:')
print(extraer_ciudades(url_provincia))
ciudad_filtro = extraer_ciudades(url_provincia)

lista_alquileres_ciudades = extraer_ciudades(url_provincia)
lista_ciudades = convertir_lista(lista_alquileres_ciudades)

seleccionar_ciudad = input('\nSeleccione la ciudad: ')
print(ciudad_filtro[int(seleccionar_ciudad)])
ciudad = seleccionar(lista_ciudades, seleccionar_ciudad)

def construir_url_ciudad(subrubro,operacion,provincia,ciudad):
    url = f'https://clasificados.lavoz.com.ar/inmuebles/{subrubro}?operacion={operacion}&provincia={provincia}&ciudad={ciudad}'
    return url

url_alquileres = construir_url_ciudad(subrubro,operacion,provincia,ciudad)

# Extraer alquileres
def parser_func(url):
    req = requests.get(url)
    home = req.content.decode('utf-8')

    parser = html.fromstring(home)
    return parser

def buscarInfo(urls_inmueble):
    for i in urls_inmueble:
        title = '//div[@class="bg-darken-1 px3 py2"]/h1/text()'
        price = '//div[@class="bg-darken-1 px3 py2"]//div[@class="h2 mt0 main bolder"]/text()'
        tipo_ope_dor = '//div[@class="inline-flex align-baseline2 col-10"]/a/text()'
        zona = '//div[@class="col col-12 md-pt2"]/p[@class="mt0 h4"]/text()'
        date = '//div[@class="bg-darken-1 px3 py2"]//div[@class="h5 center"]/text()'

        parser = parser_func(i)

        precio = parser.xpath(price)
        data_list = parser.xpath(tipo_ope_dor)
        barrio = parser.xpath(zona)
        titulo = parser.xpath(title)
        aux_fecha = parser.xpath(date)

        aux_fecha = aux_fecha[0].lstrip('Fecha de actualización: ')

        if (len(barrio) != 1):
            barrio.append("null")

        if (len(data_list) == 1):
            data_list.insert(0, "Comercio")
            data_list.append("N/A")
        elif (len(data_list) < 1):
            data_list.append("null")
            data_list.append("null")
            data_list.append("null")

        data_list.append(precio[0])
        data_list.append(barrio[0])
        data_list.append(aux_fecha)
        data_list.append(titulo[0])

        print(f"*{data_list}*\n")
        # guardar


url_ppal = url_alquileres

paginacion = '//a[@class="page-link h4"]/text()'
links_inmuebles = '//div[@class="col col-12 mx1 md-mx0 md-mr1 bg-white mb2 line-height-3 card relative safari-card "]/a[@class="text-decoration-none"]/@href'

parser = parser_func(url_ppal)

cantidad_de_paginas = parser.xpath(paginacion)

maximo = int(cantidad_de_paginas[-1])

for i in range(1, maximo):

    pagina = f"{url_ppal}&page={i}"
    parser = parser_func(pagina)
    links = parser.xpath(links_inmuebles)

    print(f"**********{pagina}**********\n")

    buscarInfo(links)

    if (i == 2):
        break
