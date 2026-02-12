from flask import Flask, render_template, request
from payroll import calculate_net_pay

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    hours = float(request.form['hours'])
    rate = float(request.form['rate'])
    
    gross, taxes, net = calculate_net_pay(hours, rate)
    
    return render_template('result.html',
                           hours=hours,
                           rate=rate,
                           gross=gross,
                           taxes=taxes,
                           net=net)
    
    
if __name__ == '__main__':
    app.run(debug=True)