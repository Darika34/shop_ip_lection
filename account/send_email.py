from django.core.mail import send_mail


def send_confirmation_email(email,code):
    send_mail(
        'your account is activate',
        f'copy and paste secret_code'
        f'\n{code}'
        f'\ndo not take this code anyone',
        'darikaakmatsaeva@gmail.com',
        [email],
        fail_silently=False

    )