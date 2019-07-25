from django.db import models

# Create your models here.


class UserInfo(models.Model):

    class Meta:

        db_table = 'user_info'

    id_user = models.IntegerField()
    scrollInfo = models.IntegerField()
    timeSpent = models.IntegerField()
    ip = models.IntegerField()
    location = models.IntegerField()
    clicks = models.IntegerField()

    def __str__(self):
        return self.id
