from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
# Create your models here.
class UserManager(models.Manager):
    def validate(self,user):
        name_regex = re.compile(r'^[a-zA-Z]+$')
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(user['fname'])<2 and not name_regex.match(user['fname']):
            print "false first_name"
            return{'error': "Invalid first_name!"}
        elif len(user['lname'])<2 and not name_regex.match(user['lname']):
            print "false last_name"
            return{'error': "Invalid last_name!"}
        elif not EMAIL_REGEX.match(user['email']):
            print "false email"
            return{'error': "Invalid Email Address!"}
        elif len(user['password']) <8:
            print "false password"
            return{'error':"too short password"}
        elif not user['cpassword'] == user['password']:
            # print user['password']
            # print user['cpassword']
            print "false confirm password"
            return {'error':"password and confirm password do not match"}
        else:
            print "true"
            # print user
            pass2=user['password']
            pass3=pass2.encode()
            hashed= bcrypt.hashpw(pass3,bcrypt.gensalt())
            # print hashed
            # pass1= bcrypt.hashpw(pass3,hashed)
            # print pass1
            User.objects.create( first_name=user['fname'],last_name=user['lname'],email=user['email'],Password=hashed)
            return {'user':user}
    def login(self,user):
        print user
        user_log=self.filter(email=user['email'])
        if user_log:
            print user_log
            pass2=user['Password']
            pass3=pass2.encode()
            if bcrypt.hashpw(pass3,user_log[0].Password.encode())== user_log[0].Password:
                return {'user':user_log[0]}
            # else:
        return{'error':"email or password failed"}


class User(models.Model):
    first_name= models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email= models.EmailField()
    Password= models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)



    objects=UserManager()
