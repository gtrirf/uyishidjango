from django.db import models

# Create your models here.


class Teachers(models.Model):
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'teachers'

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


class Groups(models.Model):
    groupname = models.CharField(max_length=255)

    class Meta:
        db_table = 'groups'

    def __str__(self):
        return self.groupname


class Students(models.Model):
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    group_id = models.ForeignKey(to='Groups', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Students'

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


class Weekdays(models.Model):
    day_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'weekdays'

    def __str__(self):
        return self.day_name


class Darsjadvali(models.Model):
    teacher_id = models.ForeignKey(to='Teachers', on_delete=models.CASCADE)
    group_id = models.ForeignKey(to='Groups', on_delete=models.CASCADE)
    weekday_id = models.ForeignKey(to='Weekdays', on_delete=models.CASCADE)

    class Meta:
        db_table = 'darsjadvali'

    def __str__(self):
        return f'{self.group_id} {self.teacher_id}'