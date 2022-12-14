import pandas as pd
from sqlalchemy import create_engine


#importamos el dataframe 
df_amazon= pd.read_csv(r"C:\Users\mariana\Downloads\PI01_DATA05-main\Datasets\amazon_prime_titles.csv") 
df_disney= pd.read_csv(r"C:\Users\mariana\Downloads\PI01_DATA05-main\Datasets\disney_plus_titles.csv")   
df_hulu= pd.read_csv(r"C:\Users\mariana\Downloads\PI01_DATA05-main\Datasets\hulu_titles.csv")
df_netflix= pd.read_json(r"C:\Users\mariana\Downloads\PI01_DATA05-main\Datasets\netflix_titles.json")


#creamos una nueva columna para cadaa data frame
df_amazon['plataforma'] = 'Amazon'
df_disney['plataforma'] = 'disney'
df_hulu['plataforma'] = 'hulu'
df_netflix['plataforma'] = 'netflix'


#concatenamos los data frame
df_filme = pd.concat([df_amazon,df_disney,df_hulu,df_netflix])


#eliminamos las columnas 'country', 'date_added','description'
df_filme = df_amazon.drop(['country', 'date_added','description'], axis=1)

#rellenamos los datos vacios NaN, por un string sin datos
df_filme.fillna('Sin Dato',inplace=True)

#Separamos la columna de duration por su valor y su unidad de medida
df_filme[["duration_3","um"]]=df_filme.duration.str.split(expand =True)

#Convertimos la columna de duration a integer
df_filme["duration_3"]=pd.to_numeric(df_filme["duration_3"], downcast="integer")


#Nos aseguramos que la columna um tenga los datos limpios
df_filme["um"]=df_filme["um"].str.replace("Seasons","Season")

#CONSULTA 1
#Máxima duración según tipo de film (película/serie), por plataforma y por año. 
# El request debe ser: get_max_duration (año, plataforma, [min o season])
df_consul_1= df_filme[["plataforma","release_year","um","duration_3"]]
df_consul_1=df_consul_1[df_consul_1["um"]=="min"].max()
df_consul_1

#CONSULTA 2
#Cantidad de películas y series (separado) por plataforma. 
# El request debe ser: get_count_plataform(plataforma)
df_consul_2=df_filme[["plataforma","title"]]
df_consul_2=df_consul_2.groupby(["plataforma"]).count()
df_consul_2

#CONSULTA 3
#Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo.
#  El request debe ser: get_listedin('genero').
df_consul_3= df_filme[["plataforma","listed_in"]]
df_consul_3=df_consul_3[df_consul_3["listed_in"].str.contains("TV Shows", regex=False)].groupby("plataforma").count()
list= set(df_consul_3["listed_in"].tolist())
df_consul_3

#CONSULTA 4
#Actor que más se repite según plataforma y año. 
# El request debe ser: get_actor(plataforma, año)
df_consul_4=df_filme[["plataforma","cast","release_year"]]
df_consul_4= df_consul_4.dropna(axis=0, how="all", subset=["cast"])
df_consul_4=df_consul_4[df_consul_4["cast"].str.contains("Nell Carter", regex=False)].groupby(["release_year","plataforma"]).count()
list= set(df_consul_4["cast"].tolist())
df_consul_4