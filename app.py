from flask import Flask, render_template, request

app = Flask(__name__, template_folder='C:\devops\pythonproject')

@app.route("/", methods=["GET", "POST"])

def index():
    if request.method == "POST":
        full_name = request.form["full_name"]
        mobile_no = request.form["mobile_no"]
        age = request.form["age"]
        address = request.form["address"]
        prescription = request.files["prescription"]

        # Submit the form data to the backend function/API

        # Save the form data into the MySQL database

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
