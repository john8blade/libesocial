from flask import Flask
import routes


app = Flask(__name__)
app.secret_key = 'minha_chave_secreta_aqui'


routes.add_routes(app)

if __name__ == '__main__':
    app.run(debug=False, port=2525)