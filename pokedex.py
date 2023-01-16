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
    pokemon = Pokemon(request.form["nome"].lower(),"","",)
    try:
        res = json.loads(requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon.nome}").text)
        result = res['sprites']
        result = result['front_shiny']
        pokemon.foto = result

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

    )

if __name__ == '__main__':
    app.run()