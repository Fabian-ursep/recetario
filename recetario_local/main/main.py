from functions import  *

ruta_recetario = Path(__file__).resolve().parent.parent / 'recetas'

lista_recetas = listado_recetas(ruta_recetario)
lista_categorias = listado_categorias(ruta_recetario)
cantidad_recetas =  len(lista_recetas)
print(lista_recetas)
print(f'Bienvenido a su recetario personal \nLa ruta de acceso a sus recetas es: {ruta_recetario} \nLa cantidad de recetas que posee actualmente es : {cantidad_recetas}' )

while True:
    opcion = mostrar_funciones()
    if opcion == '6':
        break
    else:
        elegir_tarea(opcion, ruta_recetario, lista_categorias)