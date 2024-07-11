## Flask Application Design for Smart Time

### HTML Files

* **index.html:**
    * This is the main page of the application. It will contain a form for users to input their tasks and time slots and a button to generate the schedule.
* **schedule.html:**
    * This page will display the generated schedule to the user.

### Routes

* **@app.route('/')**
    * This route handles the main page of the application. It will render the index.html file.
* **@app.route('/schedule', methods=['POST'])**
    * This route handles the submission of the form from the main page. It will validate the input, generate the schedule, and render the schedule.html file.

### Usage

1. The user opens the main page of the application at `localhost:5000/`.
2. They enter their tasks and time slots into the form and click the "Generate Schedule" button.
3. The application validates the input and generates a schedule.
4. The application renders the schedule.html file, displaying the schedule to the user.