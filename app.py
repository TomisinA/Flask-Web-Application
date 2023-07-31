from flask import Flask, jsonify, request, url_for, redirect, session, render_template #importing relevant tools 

app = Flask(__name__) #instantiating the app
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'Thisisasecret!'

@app.route('/home', methods=['GET', 'POST'], defaults = {'name': 'Default'}) #passes Default as the value for name if it isn't specified
@app.route('/home/<name>', methods=['POST', 'GET']) #passes a name variable to display in the home page
def home(name):
    session['name'] = name
    return render_template('home.html', name=name, display=False, myList=[1, 2, 3], myDict=[{'name': 'Zack'}, {'name': 'Zoe'}]) #renders an html template and includes the name variable
    

@app.route('/<person>')
def index(person):
    return '<h1>Hello {}!</h1>'.format(person)

@app.route('/')
def index2():
    return '<h1>Hello World!</h1>'

@app.route('/json') #return json data 
def json():
    name = session['name']
    return jsonify({'key1': 'value1', 'key2': [1,2,3], 'name': name})

@app.route('/query') #use query name and location to display
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return '<h1>Hi {}, you are from {}. You are on the query page</h1>'.format(name, location)

@app.route('/form') #submit a form
def form():
    return render_template('form.html')

@app.route('/process', methods=['POST']) #pass the form to process which outputs the details
def process():
    name = request.form['name']
    location = request.form['location']
    return '<h1>Hi {} from {}, your form has been submitted successfully</h1>'.format(name,location)

if __name__ == '__main__':
    app.run(debug=True)