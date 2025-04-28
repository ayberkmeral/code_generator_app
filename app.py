from flask import Flask, request, render_template
import openai

app = Flask(__name__)


openai.api_key = "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"

@app.route("/", methods=["GET", "POST"])
def index():
    code = ""
    title = ""
    if request.method == "POST":
        prompt = request.form["prompt"]


        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sen bir Python kod üretici asistansın. Kullanıcıdan istek alıp ona Python kodu ve bir başlık döndür."},
                {"role": "user", "content": prompt}
            ]
        )
        answer = response['choices'][0]['message']['content']


        if "Başlık:" in answer and "Kod:" in answer:
            parts = answer.split("Kod:")
            title = parts[0].replace("Başlık:", "").strip()
            code = parts[1].strip()

    return render_template("index.html", code=code, title=title)

if __name__ == "__main__":
    app.run(debug=True)
