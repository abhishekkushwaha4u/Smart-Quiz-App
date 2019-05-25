from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=9, blank=True)
    phone_number = models.CharField(max_length=10)
    profile_picture = models.ImageField(upload_to="profile_pictures",blank=True)
    email = models.EmailField()
    role_choices = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=7,choices=role_choices)

    def __str__(self):
        if self.registration_number=='':
            return "{} {}".format(self.role,str(self.first_name)+" "+str(self.last_name))
        else:
            return "{} {} {}".format(self.registration_number,self.role, str(self.first_name)+" "+str(self.last_name))



