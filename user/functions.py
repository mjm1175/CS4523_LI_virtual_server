################
#NEW
################
# in user directory
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context



class WelcomeEmail():
    def __init__(self, verificationCode):
        self.verificationCode = verificationCode

    subject='[LinkedIncognito] Email Address Verification'
    
    def email(self):
        return {
        'title' : 'Welcome to LinkedIncognito',
        'subtitle' : 'Verify your email to start job hunting now.',
        'message' : 'Enter this code when prompted to verify your email address: {}'.format(self.verificationCode)
        }


def send_email(email, subject, to_email):
    from_email = settings.EMAIL_HOST_USER

    text_content = """
    {}

    {}

    Regards,
    LinkedIncognito Support 
    """.format(email['subtitle'], email['message'])

    html_c = get_template('email.html')
    d = {'email':email}
    html_content = html_c.render(d)

    msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
