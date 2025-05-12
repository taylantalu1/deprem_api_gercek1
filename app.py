import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"mesaj": "Deprem API'ye hoş geldiniz. /api/deprem adresini kullanın."})

@app.route("/api/deprem")
def get_deprem_data():
    try:
        url = "https://www.koeri.boun.edu.tr/scripts/lst9.asp"
        response = requests.get(url, timeout=10)
        response.encoding = "utf-8"
        text = response.text

        pre_data = text.split("<pre>")[1].split("</pre>")[0].strip()
        lines = pre_data.split("\n")[6:]

        earthquakes = []
        for line in lines:
            parts = line.split()
            if len(parts) < 6:
                continue
            try:
                eq = {
                    "tarih": parts[0],
                    "saat": parts[1],
                    "enlem": parts[2],
                    "boylam": parts[3],
                    "derinlik_km": parts[4],
                    "buyukluk": parts[5],
                    "yer": " ".join(parts[6:])
                }
                earthquakes.append(eq)
            except:
                continue

        return jsonify(earthquakes)

    except Exception as e:
        return jsonify({"hata": str(e)}), 500
