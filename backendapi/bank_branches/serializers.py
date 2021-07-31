from rest_framework import serializers
from .models import BankBranches

class BankBranchesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=BankBranches
        fields=('ifsc','bank_id','branch','address','city','district','state')