from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Benguluru , India',
  'Salary': 'Rs. 1,000,00'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Benguluru , India',
  'Salary': 'Rs. 5,600,00'
}, {
  'id': 3,
  'title': 'FrontEnd Engineer',
  'location': 'Patna , India',
  'Salary': 'Rs. 2,000,00'
}, {
  'id': 4,
  'title': 'BackEnd Engineer',
  'location': 'Kolkata , India',
  'Salary': '$ 4,00,00'
}]


@app.route("/")
def helo():
  return render_template('home.html', jobs=JOBS, company_name='Automation')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
