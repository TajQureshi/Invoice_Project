from django.db import models

# Create your models here.
class Invoice(models.Model):
    date = models.DateField()
    customer_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Invoice-{self.id}"

class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='invoice_details')
    description = models.CharField(max_length=500, blank=True, null=True)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detail-{self.id} of Invoice-{self.invoice.id}"