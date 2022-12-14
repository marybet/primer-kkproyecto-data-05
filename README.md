# primer-kkproyecto-data-05
¡Bienvenidos a mi primer proyecto individual Data Engineer

El proyecto consiste en realizar una ingesta de datos desde diversas fuentes, posteriormente aplicar las transformaciones que consideren pertinentes, y luego disponibilizar los datos limpios para su consulta a través de una API. Esta API deberán construirla en un entorno virtual dockerizado.

Las consultas realizadas son:

+ Máxima duración según tipo de film (película/serie), por plataforma y por año:
    Request : get_max_duration(año, plataforma, [min o season])

+ Cantidad de películas y series (separado) por plataforma
    Request: get_count_plataform(plataforma)  
  
+ Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo.
   Request debe ser: get_listedin('genero')
