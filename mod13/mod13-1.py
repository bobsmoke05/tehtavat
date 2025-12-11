from flask import Flask, jsonify

app = Flask(__name__)

def onko_alkuluku(luku):
    if luku < 2:
        return False
    if luku == 2:
        return True
    if luku % 2 == 0:
        return False
    i = 3
    while i * i <= luku:
        if luku % i == 0:
            return False
        i += 2
    return True

@app.route('/alkuluku/<int:luku>', methods=['GET'])
def tarkista_alkuluku(luku):
    vastaus = {
        "Number": luku,
        "isPrime": onko_alkuluku(luku)
    }
    return jsonify(vastaus)

if __name__ == '__main__':
    app.run(port=3000)