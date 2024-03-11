from flask import Flask, render_template, request, flash, redirect
import json


app = Flask(__name__)
app.secret_key = 'Kobata'

logado = False

@app.route("/")
def Homeland():
    global logado
    logado = False

    return render_template("Index.html")

@app.route("/Home", methods=["GET","POST"])
def home():
    
    global logado

    username = request.form.get("lgin")
    pwd = request.form.get("senha")

    with open('usuarios.json') as usuariosTemp:
        usuarios = json.load(usuariosTemp)
        
        cont = 0
   
    if username == "ADM" and pwd == "1234":
        logado = True

        return redirect("/adm")
    
    for usuario in usuarios:
        cont += 1
        if usuario['nome'] == username and usuario['senha'] == pwd:
            return render_template("home.html")
        
        if cont >= len(usuarios):
            flash("NÃO AUTORIZADO")
            return redirect("/")

@app.route("/adm")
def adm():
    if logado == True:
         return render_template("administrador.html")
    if logado == False:        
        return redirect("/")

@app.route("/matnr")
def matnr():
    if logado == True:
         return render_template("home.html")
    if logado == False:        
        return redirect("/")


@app.route("/CadUser", methods=["GET","POST"])
def Caduser():
        user = []
        Login = request.form.get("LoginAdm")
        Passw = request.form.get("Password")
        user = [
            {
                "nome": Login,
                "senha": Passw
            }
        ]

        with open('usuarios.json') as usuariosTemp:
            usuarios = json.load(usuariosTemp)

        usuarioNovo = usuarios + user
        
        with open('usuarios.json','w') as gravarTemp:
            json.dump(usuarioNovo, gravarTemp, indent=4)
       
            flash("USUÁRIO CADASTRADO")
        return redirect("/adm")

@app.route("/Cadmatnr", methods=["GET","POST"])
def cadMatnr():
    matnrList = []
    matnrName = request.form.get("matNome")
    matnrList = [
        {
        "material": matnrName
    }
    ]

    with open('matnr.json') as matTemp:
        matnr = json.load(matTemp)

        newMatnr = matnr + matnrList

        with open('matnr.json', 'w') as gravarMatnr:
            json.dump(newMatnr, gravarMatnr, indent=1)

        with open('matnr.json') as matCarga:
           matnrCarga = json.load(matCarga)

           
           flash("Cadastro Realizado")

           return render_template("home.html",matnrCarga=matnrCarga)

@app.route("/service", methods=["GET","POST"])
def service():
    return render_template("services.html")

@app.route("/orcamento",methods=["GET","POST"])
def orcamento():
    return render_template("orcamento.html")


if __name__ == "__main__":
    app.run(debug=True)
