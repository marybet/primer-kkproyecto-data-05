from fastapi import FastAPI
import pandas as pd 
from limpieza import df_filme
from starlette.responses import RedirectResponse



proyecto01 = FastAPI(title="Proyecto Data Engineer")

 
@proyecto01.get("/")
async def raiz():
    return RedirectResponse(url="/docs/")   

@proyecto01.get("/get_max_duracion/")
async def get_max_duracion(anio:int,plataforma:str,um:str):

 
     df_consul_1= df_filme[["plataforma","release_year","um","duration_3"]]
     df_consul_1=df_consul_1[(df_consul_1["um"]==um)&(df_consul_1["release_year"]==anio)&(df_consul_1["plataform"]==plataforma)].groupby("release_year").max()
     return df_consul_1



@proyecto01.get("/get_count_platform/{plataforma}")
async def get_count_platform(plataforma:str):

     df_consul_2=df_filme[["plataforma","title"]]
     df_consul_2=df_consul_2.groupby(["plataforma"]).count()
     return df_consul_2   

@proyecto01.get("/get_listedin/{genero}")
async def get_listedin(genero:str):
     df_consul_3= df_filme[["plataforma","listed_in"]]
     df_consul_3=df_consul_3[df_consul_3["listed_in"].str.contains("TV Shows", regex=False)].groupby("plataforma").count()
     list= set(df_consul_3["listed_in"].tolist())
     return df_consul_3

@proyecto01.get("/get_actor/{actor}{anio}")
async def get_actor(actor:str, anio:float):    
     df_consul_4=df_filme[["plataforma","cast","release_year"]]
     df_consul_4= df_consul_4.dropna(axis=0, how="all", subset=["cast"])
     df_consul_4=df_consul_4[df_consul_4["cast"].str.contains("Nell Carter", regex=False)].groupby(["release_year","plataforma"]).count()
     list= set(df_consul_4["cast"].tolist())
     return df_consul_4
