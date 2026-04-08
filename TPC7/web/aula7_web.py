from flask import Flask, render_template
import json

app=Flask(__name__)

fd_b=open("../../Aula_3/dicionario_medico.json", "r", encoding="utf-8")
db=json.load(fd_b)


@app.get("/")  #rota para humanos
def homepage():
    return render_template("home.html")
@app.get("/api/conceitos")  #rota para máquina
def conceitos_api():
    return db

@app.get("/conceitos")  
def conceitos():
    return render_template("conceitos.html", conceitos=db.keys())


@app.get("/conceitos/<designacao>")  #link variável
def conceito(designacao):
    if designacao in db:
        descricao = db[designacao]
        return render_template("conceito.html", designacao=designacao, descricao=descricao)
    else:
        return render_template("erro.html", error="O conceito introduzido não existe.")

app.run(host="localhost", port=4002, debug=True)