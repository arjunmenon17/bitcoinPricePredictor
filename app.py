from flask import Flask, jsonify, request, render_template
app = Flask(__name__, template_folder='template')

@app.route('/')
def home_page():
    example_embed = 'This string is from python'
    return render_template('index.html', embed=example_embed)

@app.route('/test', methods=['GET', 'POST'])
def testfn():
    # GET request
    if request.method == 'GET':
        message = {'greeting':7827323.77}
        return jsonify(message)  # serialize and use JSON headers
    # POST request
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        return 'Sucesss', 200

app.run(debug=True)
