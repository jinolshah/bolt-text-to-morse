from flask import Flask, render_template, url_for, flash, redirect
from forms import DataInput
from textmorse import converter, hitter
from boltiot import Bolt
import webbrowser


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hyf56gcxz9m11qa0'

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def base():
    form = DataInput()
    if form.validate_on_submit():
        print("Valid")
        codeout = converter(form)
        opchoice = str(form.choice.data)
        api_key = str(form.boltapikey.data)
        device_id = str(form.deviceID.data)
        mybolt = Bolt(api_key, device_id)
        if codeout != "invalid":
            hitter(codeout, opchoice, mybolt)

    return render_template("home.html", form = form)

webbrowser.open_new("http://localhost:5000/")

if __name__ == "__main__":
    app.run()