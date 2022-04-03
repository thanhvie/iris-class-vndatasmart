from model import model  # Import the python file containing the ML model
from flask import Flask, request, render_template  # Import flask libraries

# Initialize the flask class and specify the templates directory
app = Flask(__name__, template_folder="templates")


# Default route set as 'home'
@app.route('/')
def home():
    return render_template('home.html')  # Render home.html


# Route 'classify' accepts GET request
@app.route('/classify', methods=['POST', 'GET'])
def classify_type():
    try:
        # Get parameters for sepal length
        sepal_len = float(request.args.get('sepal_length'))
        # Get parameters for sepal width
        sepal_wid = float(request.args.get('sepal_width'))
        # Get parameters for petal length
        petal_len = float(request.args.get('petal_length'))
        # Get parameters for petal width
        petal_wid = float(request.args.get('petal_width'))

        # Get the output from the classification model
        variety = model.classify(sepal_len, sepal_wid, petal_len, petal_wid)

        # Render the output in new HTML page
        return render_template('output.html', variety=variety)
    except Exception:
        return 'Error'


# Run the Flask server
if(__name__ == '__main__'):
    app.run(host="0.0.0.0")
