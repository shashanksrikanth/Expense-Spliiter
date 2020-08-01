# Expense-Split

## Overview
Expense-Split is a bill splitting Django application. A group of users can register as a group. After registration, one person can log in and provide the total amount. Expense-Split will then send an email to all the members of the group with how much each has to pay. 

## How to Run the Application
1. Install Docker for your specific operating system from https://docs.docker.com/get-docker/
2. Clone the repository `git clone https://github.com/shashanksrikanth/Expense-Split.git`
3. Run `cd Expense-Split/expense_split`
4. Run `docker-compose up --build`
5. Go to `localhost:8000` and you should see the application running.