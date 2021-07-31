from rest_framework import viewsets
from .serializers import BankBranchesSerializer
from .models import BankBranches
from django.shortcuts import render
from django.http import Http404
from django.db.models import Q
from functools import reduce
import operator



# Create your views here.
class SearchBankBranchesViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        if self.request.method == 'GET':
            maxLimit=1000
            queryset = BankBranches.objects.all()
            searchParam = self.request.GET.get('q', None)
            offset=int(self.request.GET.get('offset', 0))
            limit=int(self.request.GET.get('limit', maxLimit))
            limit = maxLimit if limit>maxLimit else limit
            if searchParam is not None:
                q_query = Q()
                q_filters={f'{field.name}__icontains':searchParam for field in BankBranches._meta.get_fields()}
                queryset = queryset.filter(reduce(operator.or_, (Q(**d) for d in (dict([i]) for i in q_filters.items())))).order_by('ifsc')[offset:offset+limit]
                return queryset

    serializer_class=BankBranchesSerializer

class IFSCBankBranchesViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        if self.request.method == 'GET':
            maxLimit=1000
            queryset = BankBranches.objects.all()
            branch_name = self.request.GET.get('q', None)
            offset=int(self.request.GET.get('offset', 0))
            limit=int(self.request.GET.get('limit', maxLimit))
            limit = maxLimit if limit>maxLimit else limit
            if branch_name is not None:
                queryset = queryset.filter(branch__icontains=branch_name).order_by('ifsc')[offset:offset+limit]
                print(queryset.query)
                return queryset
    serializer_class=BankBranchesSerializer

    