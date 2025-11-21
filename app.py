from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    message = None

    if request.method == "POST":
        # Get data from contact form
        name = request.form.get("name")
        email = request.form.get("email")
        message_text = request.form.get("message")

        # For now we just print in terminal (no database / email needed)
        print("New contact message:")
        print("Name:", name)
        print("Email:", email)
        print("Message:", message_text)

        message = "Thank you for contacting me, " + (name or "friend") + "!"

    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)
