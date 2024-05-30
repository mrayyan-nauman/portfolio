from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')
        database.write(f"\n{email},\n{subject},\n{message}\n")

def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route("/<page_name>")
def page_render(page_name):
    try:
        return render_template(page_name)
    except:
        return 'Page not found', 404

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except Exception as e:
            return f'An error occurred: {e}'
    else:
        return 'Something went wrong'

if __name__ == '__main__':
    app.run(debug=True)
