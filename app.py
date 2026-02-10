#th is the actual code
from flask import Flask, render_template, request

app = Flask(__name__)

# Morse Code Dictionary
MORSE_CODE_MAP = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".",
    "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---",
    "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---",
    "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-",
    "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--",
    "z": "--..",

    "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..",
    "9": "----.", "0": "-----",

    " ": "/"   # Space between words
}


# Home Page Route
@app.route("/", methods=["GET", "POST"])
def home():
    output = ""

    if request.method == "POST":
        text = request.form.get("text", "").lower()

        # Convert Text → Morse Code
        output = " ".join(MORSE_CODE_MAP.get(ch, "?") for ch in text)

    return render_template("index.html", output=output)


# Run Flask App
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
