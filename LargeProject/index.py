from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/postproduct')
def postproduct():
    return render_template('postproduct.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/thankyou')
def thankyou():
    first = request.args.get('firstname')
    return render_template('thankyou.html', first = first)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/lifestyle')
def lifestyle():
    return render_template('lifestyle.html')

@app.route('/sports')
def sports():
    return render_template('sports.html')

if __name__ == '__main__':
    app.run(debug = True)
