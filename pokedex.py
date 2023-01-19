from flask.globals import request
from models.pokemon import Pokemon
from flask import Flask, render_template
import requests
import json


app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/buscar", methods = ["GET","POST"])


def buscar():
    pokemon = Pokemon(request.form["nome"].lower(),"","","",)
    try:
        res = json.loads(requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon.nome}").text)
        result = res['sprites']['front_default']
        sprite_shiny = res['sprites']['front_shiny']
        name = res['forms'][0]['name']

        pokemon.foto = result
        pokemon.shiny = sprite_shiny
        pokemon.nome = name
       
        if len (res["types"])==1:
            pokemon.tipo = res["types"][0]["type"]["name"]
        else:
            pokemon.tipo = res["types"][0]["type"]["name"]

    except:
        return "Pokemon Não encontrado"

    return render_template("index.html",
    nome = pokemon.nome,
    foto = pokemon.foto,
    tipo = pokemon.tipo.upper(),
    shiny = pokemon.shiny,

    )

if __name__ == '__main__':
    app.run(debug= True)