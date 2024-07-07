# from django.core.mail.message import EmailMessage
# from django.conf import settings
# from .models import contact
# from django.core.mail import send_mail
# from django.core import mail

# def contact(request):
    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     subject = request.POST.get('subject')
    #     message = request.POST.get('message')
    #     email = request.POST.get('email')
    #     query = contact(name=name, email=email, subject=subject, message=message)
    #     query.save()

    #     #email sending start from here
    #     from_email = settings.EMAIL_HOST_USER 
    #     connection = mail.get_connection()
    #     connection.open()
    #     email_message = mail.EmailMessage(f'Email from : {name}', f'user email : {email}', 
    #                                       f'message : {message}',from_email,['shahlathasni3@gmail.com'],
    #                                       connection=connection)

    #     connection.send_messages([email_message])
    #     connection.close()
        
        # recipient_list = ['shahlathasni3@gmail.com']
        # send_mail( subject, message, email, recipient_list,name )
