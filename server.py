from flask import Flask, render_template, request, redirect
import csv

'''Setting up the App'''
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<page_name>')
def page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open("Database.txt" , mode="a") as db:
        email = data["email"]
        sub = data["subject"]
        msg = data["message"]
        file = db.write(f"\n==========================================="
                        f"\nFrom:    {email},"
                        f"\nSubject: {sub},"
                        f"\nMessage: {msg}")


def write_to_csv(data):
    with open("Database.csv" , mode="a") as db_csv:
        email = data["email"]
        sub = data["subject"]
        msg = data["message"]
        csv_writer = csv.writer(db_csv, delimiter="|", quotechar=" ", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, sub, msg])


@app.route('/submit_data', methods=['POST', 'GET'])
def submit_data():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_file(data)
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return "Opps !!! Something went WRONG. \n Please tra Again"

