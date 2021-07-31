# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# class Banks(models.Model):
#     name = models.TextField(blank=True, null=True)  # This field type is a guess.
#     id = models.BigIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'banks'


# class Branches(models.Model):
#     ifsc = models.TextField()  # This field type is a guess.
#     bank_id = models.BigIntegerField(blank=True, null=True)
#     branch = models.TextField(blank=True, null=True)  # This field type is a guess.
#     address = models.TextField(blank=True, null=True)  # This field type is a guess.
#     city = models.TextField(blank=True, null=True)  # This field type is a guess.
#     district = models.TextField(blank=True, null=True)  # This field type is a guess.
#     state = models.TextField(blank=True, null=True)  # This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'branches'

class BankBranches(models.Model):
    ifsc = models.TextField(primary_key=True)  # This field type is a guess.
    bank_id = models.BigIntegerField(blank=True, null=True)
    branch = models.TextField(blank=True, null=True)  # This field type is a guess.
    address = models.TextField(blank=True, null=True)  # This field type is a guess.
    city = models.TextField(blank=True, null=True)  # This field type is a guess.
    district = models.TextField(blank=True, null=True)  # This field type is a guess.
    state = models.TextField(blank=True, null=True)  # This field type is a guess.
    bank_name = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'bank_branches'
