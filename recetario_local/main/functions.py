import os
from pathlib import Path


def mostrar_funciones():
    print('''Por favor, seleccione una de las siguientes opciones:
    1. Leer receta almacenada
    2. Crear nueva receta
    3. Crear nueva categoría
    4. Eliminar receta
    5. Eliminar categoría
    6. Salir''')
    while True:
        seleccion_lista = ['1','2','3','4','5','6']
        seleccion = input('>: ')
        if seleccion in seleccion_lista:
            return seleccion
        else:
            print('Por favor seleccione una opción correcta')

def elegir_tarea(opcion, ruta, lista):
    if opcion == '1':
        leer_receta(lista)
    elif opcion == '2':
        crear_receta(lista)
    elif opcion == '3':
        crear_categoría()
    elif opcion == '4':
        eliminar_receta()
    elif opcion == '5':
        eliminar_categoría()
    else:
        salir()


def leer_receta(lista):
    while True:
        lista_categorías = lista
        for i in lista_categorías:
            print(i)
        categoria = input('Por favor seleccione una de las categorias mencionadas \n>: ').capitalize()
        if categoria in lista:
            ruta_leer = Path(__file__).resolve().parent.parent / 'recetas' / categoria
            rutas_categorias = list(p for p in ruta_leer.glob('*'))
            lista_recetas = [p.stem.capitalize() for p in rutas_categorias]
            while True:
                lista = lista_recetas
                for i in lista:
                    print(i)
                receta_a_leer = input('Por favor seleccione una de las recetas mencionadas \n>: ').capitalize()
                ruta_receta_leer = str(receta_a_leer + '.txt')
                if receta_a_leer in lista:
                    ruta_abrir = Path(__file__).resolve().parent.parent / 'recetas' / categoria
                    receta = open(ruta_abrir / ruta_receta_leer, 'r')
                    print(receta.read())
                    receta.close()
                    break
            break
        else:
            print('Por favor seleccione una categoría válida:')
    confirmacion_lectura = input('Presione enter para volver al menú principal')

def crear_receta(lista):
    while True:
        lista_categorías = lista
        for i in lista_categorías:
            print(i)
        categoria = input('Por favor seleccione una de las categorias mencionadas \n>: ').capitalize()
        if categoria in lista:
            ruta_crear = Path(__file__).resolve().parent.parent / 'recetas' / categoria
            receta_a_crear = input('Por favor escriba un nombre para su nueva receta \n>: ').capitalize()
            ruta_receta_crear = str(receta_a_crear + '.txt')
            receta = open(ruta_crear / ruta_receta_crear, 'x')
            receta.close()
            receta = open(ruta_crear / ruta_receta_crear, 'w')
            nueva_receta = input('Por favor a continuación escriba su receta\n>: ').capitalize()
            receta.write(nueva_receta)
            break
        else:
            print('Por favor seleccione una categoría válida:')
    confirmacion_lectura = input('Presione enter para volver al menú principal')

def crear_categoría():
    print('crear categoria')
def eliminar_receta():
    print('eliminar receta')
def eliminar_categoría():
    print('eliminar categoria')
def salir():
    print('salir')

def listado_recetas(ruta):
    ruta_recetas = list(p for p in ruta.glob('**/*.txt'))
    lista_recetas = [p.stem.capitalize() for p in ruta_recetas]
    return lista_recetas

def listado_categorias(ruta):
    rutas_categorias = list(p for p in ruta.glob('*') if p.is_dir())
    lista_recetas = [p.stem.capitalize() for p in rutas_categorias]
    return lista_recetas


'''
2. En la opción 2 también se le va a hacer elegir una categoría, pero luego le va a pedir que
escriba el nombre y el contenido de la nueva receta que quiere crear, y el programa va
a crear ese archivo en el lugar correcto.
3. La opción 3 le va a preguntar el nombre de la categoría que quiere crear y va a generar
una carpeta nueva con ese nombre.
4. La opción 4, hará todo lo mismo que la opción uno, pero en vez de leer la receta, la va
a eliminar
5. La opción 5, le va a preguntar qué categoría quiere eliminar
6. Finalmente, la opción 6 simplemente va a finalizar la ejecución del código.'''