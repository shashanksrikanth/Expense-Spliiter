# Expense-Split

## Overview
Expense-Split is a bill splitting Django application. A group of users can register as a group. After registration, one person can log in and provide the total amount. Expense-Split will then send an email to all the members of the group with how much each has to pay. 

With Expense-Split, you can do the following:
1. Register a Group
2. Send an email to the members of the Group
3. Delete a Group
4. Add a new member to the Group

For developing purposes, an API has also beeen created to list and create groups. The URLs for these APIs are given in the `urls.py` file in the repository.

## How to Run the Application
1. Install Docker for your specific operating system from https://docs.docker.com/get-docker/
2. Clone the repository `git clone https://github.com/shashanksrikanth/Expense-Split.git`
3. Run `cd Expense-Split/expense_split`
4. Run `docker-compose up --build`
5. Go to `localhost:8000` and you should see the application running.

## Further Work
I am currently working on the following new features for this project:
1. Adding an option to add an image to the email that is sent to the group
2. Adding a data dashboard for expense reports
3. A better way to hide the API key needs to be researched. For now, I have simply not included it in the repository. 
