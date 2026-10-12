Test No.	Test Description	Test Input	Expected Result
TC01	Record valid initial readings	Number of readings: 4; temperatures: 25, 32, 35, 40	The program records all four readings successfully.
TC02	Enter an invalid number of readings	0 or -1	The program displays an error message and asks for a positive whole number.
TC03	Enter an invalid temperature	101 or -5	The program rejects the temperature and asks for a whole number between 0 and 100.
TC04	Display all temperatures	Select menu option 1	The program displays all stored temperatures and their classifications.
TC05	Record a new temperature	Select option 2, then enter 28	The program adds the new temperature and displays a success message.
TC06	Check temperature classifications	Enter 25, 32, 35, and 40; select option 3	The program classifies 25 as NORMAL, 32 and 35 as WARNING, and 40 as CRITICAL.
TC07	Inspect sensor status indicators	Select menu option 3	The program displays [OK], [!], or [ALERT] according to each temperature's status.
TC08	Calculate temperature statistics	Use readings 25, 32, 35, 40; select option 4	The program displays a total of 132°C, an average of 33.00°C, a minimum of 25°C, and a maximum of 40°C.
TC09	Generate the system performance report	Use readings 25, 32, 35, 40; select option 4	The program displays 1 NORMAL reading, 2 WARNING readings, 1 CRITICAL reading, and the condition ACTION NEEDED.
TC10	Handle an invalid menu choice and exit	Enter menu choice 6, then select 5	The program rejects choice 6 and displays the shutdown messages after choice 5.
3. Test Results
The following table is provided for recording the actual results after running the program.

Test No.	Actual Result	Status
TC01	____________________	Pending
TC02	____________________	Pending
TC03	____________________	Pending
TC04	____________________	Pending
TC05	____________________	Pending
TC06	____________________	Pending
TC07	____________________	Pending
TC08	____________________	Pending
TC09	____________________	Pending
TC10	____________________    Pending