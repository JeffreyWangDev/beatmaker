from flask import Flask, render_template

app = Flask(__name__,
            static_folder='static')

@app.route("/snare.mp3")
def snare():
    return app.send_static_file("snare.mp3")

@app.route("/bass.mp3")
def kick():
    return app.send_static_file("bass.mp3")

@app.route("/hihat.mp3")
def hihat():
    return app.send_static_file("hihat.mp3")

@app.route("/tom.mp3")
def tom():
    return app.send_static_file("tom.mp3")

@app.route("/cowbell.mp3")
def cowbell():
    return app.send_static_file("cowbell.mp3")

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)