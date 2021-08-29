-- Keep a log of any SQL queries you execute as you solve the mystery.
-- checking crime scene reports for 28 july 2020 on Chamberlain street
SELECT * FROM crime_scene_reports
WHERE year = 2020 AND month = 07 AND day = 28
AND street = "Chamberlin Street";

-- Theft took place at 10:15 am at chamberlain street courthouse
-- Interviews were conducted with three witnesses and transcripts are present. searching for the transcripts in the interviews table
SELECT * FROM interviews
WHERE year = 2020 AND month = 07 AND day = 28
AND transcript LIKE "%courthouse%";

-- Ruth, Eugene and Raymond are the witnesses
-- The thief left within 10 minutes of the theft from the courthouse in a car; the thief wanted to leave fiftyville on the earliest flight out on 29th july 2020
-- The thief withdrew money from the ATM on Fifer street on 28th morning

-- Getting the list of people exits from the courthouse security logs
SELECT name FROM people
JOIN courthouse_security_logs ON people.license_plate = courthouse_security_logs.license_plate
WHERE year = 2020 AND month = 07 AND day = 28 AND hour = 10
AND minute >= 15 AND minute <= 25 AND activity = "exit";

-- Patrick, Ernest, Amber, Danielle, Roger, Elizabeth, Russell, Evelyn are the suspects

-- Getting list of people with ATM transactions on 28 July 2020
SELECT name FROM people
JOIN bank_accounts ON people.id = bank_accounts.person_id
JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE year = 2020 AND month = 07 AND day = 28
AND atm_location = "Fifer Street"
AND transaction_type = "withdraw";

-- Ernest, Russell, Roy, Bobby, Elizabeth, Danielle, Madison, Victoria have withdrawn from the ATM on 28 July 2020

-- Selecting the people who made phone calls on the day of the robbery around 10:15 am
SELECT name FROM people
JOIN phone_calls ON people.phone_number = phone_calls.caller
WHERE year = 2020 AND month = 07 and day = 28
AND duration < 60;

-- List of people who travelled the first flight
SELECT name FROM people
JOIN passengers ON people.passport_number = passengers.passport_number
WHERE flight_id =
(SELECT id FROM flights
WHERE year = 2020 AND month = 07 AND day = 29
ORDER BY hour, minute LIMIT 1);


-- Intersecting the above mentioned details to see if the thief is identified
SELECT name FROM people
JOIN courthouse_security_logs ON people.license_plate = courthouse_security_logs.license_plate
WHERE year = 2020 AND month = 07 AND day = 28 AND hour = 10
AND minute >= 15 AND minute <= 25 AND activity = "exit"

INTERSECT

SELECT name FROM people
JOIN bank_accounts ON people.id = bank_accounts.person_id
JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE year = 2020 AND month = 07 AND day = 28
AND atm_location = "Fifer Street"
AND transaction_type = "withdraw"

INTERSECT


SELECT name FROM people
JOIN phone_calls ON people.phone_number = phone_calls.caller
WHERE year = 2020 AND month = 07 and day = 28
AND duration < 60

INTERSECT

SELECT name FROM people
JOIN passengers ON people.passport_number = passengers.passport_number
WHERE flight_id =
(SELECT id FROM flights
WHERE year = 2020 AND month = 07 AND day = 29
ORDER BY hour, minute LIMIT 1);

-- The Thief has been identified as Ernest

-- Getting the city where the thief escaped to from the flight destination
SELECT city FROM airports
WHERE id = (SELECT destination_airport_id FROM flights
WHERE year = 2020 AND month = 07 AND day = 29
ORDER BY hour, minute LIMIT 1);

-- The thief escaped to London

-- Getting the record of the person who Ernest spoke to over phone to grab the accomplice
SELECT name FROM people
JOIN phone_calls ON people.phone_number = phone_calls.receiver
WHERE year = 2020 AND month = 07 and day = 28
AND duration < 60
AND caller = (SELECT phone_number FROM people
WHERE name = "Ernest");

-- The Thief's accomplice was Berthold