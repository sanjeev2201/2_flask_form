from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')



@app.route('/home/')
def home():
    return render_template('home.html')


@app.route('/success/')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)
