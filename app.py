from flask import Flask, render_template
import datetime

# Skapa en Flask-app
app = Flask(__name__)

# Ange vad som händer när man går in på startsidan '/'
@app.route('/')
def home():
    return 'Hello world'

@app.route('/date')
def date():
    return str(datetime.date.today())

@app.route('/hej/<name>')
def hej(name):
    name = name.upper()
    return render_template("main.html", greeting_name=name)


# Starta webbappen när man kör python-filen
if __name__ == "__main__":
    app.run(debug=True)