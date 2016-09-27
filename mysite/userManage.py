#!/usr/bin/env python
from django.contrib.auth.models import User, Group
from django.core.mail import send_mail

initMessage="""\
Hi {0},

Here is your account on apt.lfu.space.

The username is \t\t{1}
with email address \t\t{2}
The initial password is \tapt123456789

The link will navigate you to the website.
http://apt.lfu.space
You can login to change the password.

Best,
Admin"""

def getUserFromGroup(groupName='test_mail'):
    group=Group.objects.get(name=groupName)
    user_ingroup=[{'name':"%s %s"%(u.first_name, u.last_name), 'email':u.email, 'username':u.username} for u in group.user_set.all()]
    return user_ingroup

def sendInitMail(users):
    counter=0
    for u in users:
        counter+=send_mail('New account for %s at apt.lfu.space'%u['name'].strip(),\
                           initMessage.format(u['name'].strip(), u['username'], u['email']), 'noreply@lfu.space', [u['email']], fail_silently=False,)
    print "%s of %s has been sent"%(counter, len(users))

def sendMail(users, subject, message):
    """
        for \{0\} is name
            \{1\} is username
            \{2\} is email
    """
    counter=0
    for u in users:
        counter+=send_mail(subject.format(u['name'].strip(), u['username'], u['email']),\
                           message.format(u['name'].strip(), u['username'], u['email']), 'noreply@lfu.space', [u['email']], fail_silently=False,)
    print "%s of %s has been sent"%(counter, len(users))
