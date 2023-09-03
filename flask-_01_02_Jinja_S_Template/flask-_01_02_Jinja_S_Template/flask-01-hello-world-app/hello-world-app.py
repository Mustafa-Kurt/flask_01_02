from flask import Flask 
app = Flask(__name__)

@app.route('/')
def head():
    return "Hello Mustafa"

@app.route('/second')
def second():
    return "Hello Mustafa Second"

@app.route('/third')
def third():
    return "Hello Mustafa Third"

@app.route('/forth/<string:id>')
def forth(id):
    return f'Id of bu sayfa is {id}'






if __name__ == '__main__':

    app.run(debug=True, port=30000)
    # app.run(host= '0.0.0.0', port=8081)


    