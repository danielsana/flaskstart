from flask import Flask

app = Flask(__name__)

@app.route('/home') # decorator defines a route
def home(): # each route has a function … recall def
 return 'Our first Flask website'
if __name__ == '__main__':
 app.run(debug=True)
