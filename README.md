Simulated Device Monitoring and Alert System
Student Name: Laceda, Andrei Miguel D.
Student Number: 2600407
Section: 1CPE-A

Project Description
The Simulated Device Monitoring and Alert System is a Python program that monitors simulated device temperature readings. It classifies each reading as NORMAL, WARNING, or CRITICAL based on its temperature value. The program allows users to view stored readings, record new temperatures, inspect sensor statuses, and generate a system performance report. It also validates user input to prevent invalid temperature readings and menu choices.

Features
View all stored temperature readings.
Add a new temperature reading using whole numbers from 0 to 100 only.
Classify every reading as NORMAL, WARNING, or CRITICAL.
Inspect temperature statuses using indicators such as [OK], [!], and [ALERT].
Generate a numerical summary, including the total, average, lowest, and highest temperatures.
Display the number and percentage of readings in each temperature category.
Determine the overall system condition.
Reject invalid menu choices and temperature readings.
Requirements
Python 3
No external packages required.
How to Run
Open a terminal inside the Week17 folder.
Type the following command:
   python device_monitor.py
On macOS or Linux, use:

   python3 device_monitor.py
Sample Output
The following is a sample run using the program's actual input prompts, temperature classifications, and report format.

==========================================
       SMART TEMPERATURE CONTROL
==========================================
How many readings do you want to record? 4
Temperature #1: 25
Temperature #2: 32
Temperature #3: 35
Temperature #4: 40

Initial readings successfully recorded!

==========================================
           CONTROL CENTER
==========================================
  [1] Display All Temperatures
  [2] Record New Temperature
  [3] Check Temperature Status
  [4] View System Report
  [5] Shut Down
==========================================
Select an operation (1-5): 1

--- TEMPERATURE LOGBOOK ---
Sensor 01:  25 °C | NORMAL
Sensor 02:  32 °C | WARNING
Sensor 03:  35 °C | WARNING
Sensor 04:  40 °C | CRITICAL

==========================================
           CONTROL CENTER
==========================================
  [1] Display All Temperatures
  [2] Record New Temperature
  [3] Check Temperature Status
  [4] View System Report
  [5] Shut Down
==========================================
Select an operation (1-5): 4

==========================================
          SYSTEM PERFORMANCE REPORT
==========================================
Total sensor records : 4
Combined temperature : 132 °C
Average temperature : 33.00 °C
Lowest temperature  : 25 °C
Highest temperature : 40 °C

--- STATUS DISTRIBUTION ---
NORMAL    :   1 (25.00%)
WARNING   :   2 (50.00%)
CRITICAL  :   1 (25.00%)

--- FINAL SYSTEM ASSESSMENT ---
Condition: ACTION NEEDED
==========================================

==========================================
           CONTROL CENTER
==========================================
  [1] Display All Temperatures
  [2] Record New Temperature
  [3] Check Temperature Status
  [4] View System Report
  [5] Shut Down
==========================================
Select an operation (1-5): 5

System shutting down...
Thank you for using Smart Temperature Control!
Note: This is a sample run based on the provided code. Run the program yourself if your instructor requires actual captured output.

Test Cases
I performed 10 tests. passed and failed.

The tests cover the following functions:

Recording valid initial temperature readings.
Rejecting zero or negative numbers as the number of initial readings.
Rejecting temperatures outside the range of 0 to 100.
Displaying all stored temperature readings.
Recording a new temperature.
Classifying temperatures as NORMAL, WARNING, or CRITICAL.
Inspecting sensor statuses.
Calculating the total and average temperatures.
Generating the system performance report and determining the overall condition.
Rejecting invalid menu choices and shutting down the program correctly.
Full details are provided in test_cases.md.

Known Limitations
Temperature readings are lost when the program closes because the data is not saved to a file or database.
The program uses simulated temperature readings instead of collecting data from actual devices.
The system accepts only whole-number temperature readings from 0 to 100.
The program does not provide real-time monitoring or automatic temperature collection.
The system operates through a text-based interface rather than a graphical user interface.
Reflection
The hardest part of developing this project was implementing the temperature classification system and ensuring that every reading was assigned the correct status. I also needed to make sure that the numerical summary correctly calculated the total, average, lowest, and highest temperatures. Input validation was important because it prevented invalid temperature values and menu choices from being accepted. Through this project, I learned how to use conditional statements, loops, functions, and lists to organize a Python program. In the future, I would improve the system by saving temperature readings to a file and adding real-time monitoring features and a graphical user interface.

Before submitting:

Replace the test counts with your actual results after running your 10 tests.

Create or update test_cases.md with the results of those tests.

Make sure the filename in your instructions (device_monitor.py) matches the name of your actual Python file.

Your program's title is Smart Temperature Control, while your project title is Simulated Device Monitoring and Alert System. You can keep both, but using the same title throughout would make the submission more consistent.