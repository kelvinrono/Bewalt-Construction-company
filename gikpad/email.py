from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name,receiver):
    # Creating message subject and sender
    subject = 'Gikpad Technologies Feedback'
    sender = 'gikpadtechnologies@gmail.com'

    #passing in the context vairables
    text_content = render_to_string('email/feedback-email.txt',{"name": name})
    html_content = render_to_string('email/feedback-email.html',{"name": name})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()

def send_director_email(admin_name):
    # Creating message subject and sender
    subject = 'New Client Request'
    sender = 'gikpadtechnologies@gmail.com'
    admin_email=['ibrakipz7@gmail.com']

    #passing in the context vairables
    text_content = render_to_string('email/request-email.txt',{"admin_name": admin_name})
    html_content = render_to_string('email/request-email.html',{"admin_name": admin_name})

    msg = EmailMultiAlternatives(subject,text_content,sender,bcc=admin_email)
    msg.attach_alternative(html_content,'text/html')
    msg.send()