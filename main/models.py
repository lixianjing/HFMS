# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Account(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id = models.PositiveIntegerField(unique=True)
    uid = models.PositiveIntegerField()
    type = models.PositiveIntegerField(blank=True, null=True)
    name = models.CharField(max_length=200)
    balance = models.FloatField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    create_time = models.TextField()
    modify_time = models.TextField()

    class Meta:
        managed = False
        db_table = 'account'


class Category(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=200)
    type = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'category'


class CategorySub(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id = models.PositiveIntegerField(unique=True)
    pid = models.PositiveIntegerField()
    name = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'category_sub'


class Record(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id = models.PositiveIntegerField(unique=True)
    cate_id = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    account_id = models.PositiveIntegerField()
    type = models.PositiveIntegerField(blank=True, null=True)
    type_id = models.PositiveIntegerField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    occur_time = models.TextField()
    status = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'record'


class Test(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id = models.PositiveIntegerField(unique=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'



