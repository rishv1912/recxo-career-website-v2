from flask import Flask,render_template,redirect,url_for,jsonify

app  = Flask(__name__)

app.config['STATIC_FOLDER'] = 'static'


JOBS = [{
    'id':1,
    'title':'Data Analyst',
    'location':'Bengaluru,India',
    'salary':'Rs. 10,00,000'
},
{
    'id':2,
    'title':'Data Scientist',
    'location':'Delhi,India',
    'salary':'Rs. 15 ,00,000'
},
{
    'id':3,
    'title':'Frontend Engineer',
    'location':'Remote',
    'salary':'Rs. 11,00,000'
},
{
    'id':4,
    'title':'Backend Engineer',
    'location':'San Francisco, US',
    'salary':'$110,000'
},
]

@app.route('/')
def index():
    return render_template('index.html',jobs=JOBS,company_name = "Recxo")

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)