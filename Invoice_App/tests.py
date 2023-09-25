from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Invoice


# Create your tests here.

class InvoiceAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice_data = {
            'date': '2023-09-23',
            'customer_name': 'Test Customer',
        }

    def test_create_invoice(self):
        response = self.client.post('/invoices/', self.invoice_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Invoice.objects.count(), 1)
        self.assertEqual(Invoice.objects.get().customer_name, 'Test Customer')
