from flask import Flask, render_template

app = Flask(__name_)

@app.route('/')
def home():
    return render_template('WebPage.html')

if __name__ == '__main__':
    app.run(debug=True)
