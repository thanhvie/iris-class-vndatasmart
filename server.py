import model # Import the python file containing the ML model
from flask import Flask, request, render_template # Import flask libraries

# Initialize the flask class and specify the templates directory
app = Flask(__name__,template_folder="templates")

# Default route set as 'home'
@app.route('/')
def home():
    return render_template('home.html') # Render home.html

# Route 'classify' accepts GET request
@app.route('/classify',methods=['POST','GET'])
def classify_type():
    try:
        sepal_len = request.args.get('sepal_length') # Get parameters for sepal length
        sepal_wid = request.args.get('sepal_width') # Get parameters for sepal width
        petal_len = request.args.get('petal_length') # Get parameters for petal length
        petal_wid = request.args.get('petal_width') # Get parameters for petal width

        # Get the output from the classification model
        variety = model.classify(sepal_len, sepal_wid, petal_len, petal_wid)

        # Render the output in new HTML page
        return render_template('output.html', variety=variety)
    except:
        return 'Error'

# Run the Flask server
if(__name__=='__main__'):
    app.run(debug=True)        