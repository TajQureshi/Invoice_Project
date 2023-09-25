from django.shortcuts import render
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer, InvoiceDetailSerializer
from rest_framework import viewsets

# Create your views here.
class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoiceDetailViewSet(viewsets.ModelViewSet):
    queryset = InvoiceDetail.objects.all()
    serializer_class = InvoiceDetailSerializer