from twilio.rest import Client
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email(members, amount, reason):
    try:
        sg = SendGridAPIClient('my_api_key')
        subject_line = 'Expense Split Notification'
        individual_members = members.split(',')
        amount_due = amount/len(individual_members)
        for individual in individual_members:
            body = 'Hello! ${} is due because of the following reason: {}'.format(amount_due, reason)
            message = Mail(
                from_email='expensesplit1@gmail.com',
                to_emails=individual,
                subject=subject_line,
                html_content=body
            )
            response = sg.send(message)
        return True
    except Exception as e:
        return False 