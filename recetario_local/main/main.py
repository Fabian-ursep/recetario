from pathlib import Path

ruta_recetario = Path(__file__).resolve().parent.parent / 'recetas'
lista_recetas = list(Path(ruta_recetario).glob('**/*.txt'))
cantidad_recetas = 1


print(lista_recetas)
print(f'Bienvenido a su recetario personal \nLa ruta de acceso a sus recetas es: {ruta_recetario} \nLa cantidad de recetas que posee actualmente es : {cantidad_recetas}' )
