from flask import Flask, render_template #flask - framework ; Flask - python datatype

app = Flask(__name__) # create an instance of Flask class 

@app.route('/')
def home():
    return render_template('home.html') # function is mapped to home, or '/'

@app.route('/research/')
def research():
    return render_template('research.html')

@app.route('/projects/')
def projects():
    return render_template('projects.html')

@app.route('/links/')
def links():
    return render_template('links.html')

if __name__ == '__main__':
    app.run(debug=True)