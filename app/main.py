from flask import Flask, send_file
import pandas as pd
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

@app.route("/hello")
def hello():
    return {"message": "🚀 API funziona correttamente!"}

@app.route("/plot")
def plot():
    # Creiamo dati fittizi
    df = pd.DataFrame({"x": [1, 2, 3, 4, 5], "y": [1, 4, 9, 16, 25]})

    # Creiamo il grafico
    plt.figure()
    plt.plot(df["x"], df["y"], marker="o")
    plt.title("Grafico fittizio")
    plt.xlabel("X")
    plt.ylabel("Y")

    # Salviamo in memoria
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)

    # Restituiamo l’immagine al browser
    return send_file(buf, mimetype="image/png")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
