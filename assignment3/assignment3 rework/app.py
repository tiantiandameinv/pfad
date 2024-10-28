from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    days_diff = None
    if request.method == 'POST':
        year = request.form.get('year')
        month = request.form.get('month')
        day = request.form.get('day')
        try:
            past_date = datetime(int(year), int(month), int(day))
            current_date = datetime.now()
            days_diff = (current_date - past_date).days
        except ValueError:
            days_diff = 'Invalid date. Please enter a valid date.'

    return render_template('index.html', days_diff=days_diff)

if __name__ == '__main__':
    app.run(debug=True)
