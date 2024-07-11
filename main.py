
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schedule', methods=['POST'])
def schedule():
    tasks = request.form.getlist('task')
    time_slots = request.form.getlist('time_slot')
    
    # Validate input
    if not tasks or not time_slots:
        return render_template('index.html', error="Please enter tasks and time slots.")

    # Generate schedule
    schedule = []
    for task in tasks:
        for time_slot in time_slots:
            schedule.append({'task': task, 'time_slot': time_slot})

    # Render schedule
    return render_template('schedule.html', schedule=schedule)

if __name__ == '__main__':
    app.run(debug=True)
