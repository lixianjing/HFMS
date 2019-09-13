from django.db import models

# Create your models here.
class User(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id = models.PositiveIntegerField(unique=True)
    group_id = models.PositiveIntegerField()
    account = models.CharField(max_length=100)
    pwd = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=200)
    avatar = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    sex = models.PositiveIntegerField(blank=True, null=True)
    auth = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class UserGroup(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=200)
    avatar = models.TextField(blank=True, null=True)
    auth = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_group'
