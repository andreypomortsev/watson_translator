import os
import sys
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)
from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/english_to_french")
def englishToFrench():
    text_to_translate = request.args.get('textToTranslate')
    # Write your code here
    return translator.english_to_french(text_to_translate)

@app.route("/french_to_english")
def frenchToEnglish():
    text_to_translate = request.args.get('textToTranslate')
    # Write your code here
    return translator.french_to_english(text_to_translate)

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')
  

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
