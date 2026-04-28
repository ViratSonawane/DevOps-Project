from flask import Flask, render_template

app = Flask(__name__)

# Route for the Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the Pathways Page
@app.route('/pathways')
def pathways():
    return render_template('pathways.html')

# Route for the Community Page
@app.route('/community')
def community():
    return render_template('community.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)