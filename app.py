from flask import Flask, jsonify, request, render_template
import final

app = Flask(__name__, template_folder='template')
@app.route('/test', methods=['GET', 'POST'])
def testfn():
    # GET request
   if request.method == 'GET':
      message = {'btc_price':final.bitcoin(), 'eth_price':final.eth()}
      return render_template('index.html', jsonify(message))
    


if __name__ == "__main__":
   app.run()