from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Servidor en Ejecución"

# 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