from flask import Flask, render_template, request, jsonify
from transfunction import transliteration

app = Flask(__name__)
# To return transliterated text as string format w/o it will be ascii_unicode characters
app.config["JSON_AS_ASCII"] = False


@app.route("/")
def index():
    return render_template("Homepage.html", is_available=True)


@app.route("/trans")
def trans():

    return render_template(
        "transliterate.html",
        our_text=transliteration(text="English to tamil typing", language="tamil"),
    )


@app.route("/addRegion", methods=["POST"])
def addRegion():
    value = request.form["projectFilePath"]
    chosen_lang = request.form["language"]

    """To return as webpage"""
    return render_template(
        "Homepage.html",
        prediction=transliteration(text=value, language=chosen_lang),
        is_available=True,
    )
    """To return as json format"""
    # data = transliteration(
    #     text=value, language=chosen_lang)
    # return jsonify(final=data)


@app.route("/final/<message>/<lang>", methods=["GET"])
def final(message, lang):

    result = transliteration(text=message, language=lang)
    # print((message, result))
    # return jsonify(input=message, answer=result)
    return render_template(
        "transliterate.html",
        our_text=transliteration(text=message, language=lang),
    )


if __name__ == "__main__":
    app.run(debug=True)
