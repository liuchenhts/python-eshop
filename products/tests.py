from django.test import TestCase
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .models import Product

# Create your tests here.
class ProductModelTests(TestCase):

    def testProductCRUD(self):
        """
            some comments
        """
        product = Product()
        product.name="test product"
        product.price=1
        product.save()

        p = get_object_or_404(Product, pk=product.id)
        print (p)
        self.assertEqual(p.name, product.name)

        url = reverse('products:read', kwargs={'pk': product.id})
        response = self.client.get(url)
        self.assertContains(response, p.name)


        url = reverse('products:read', kwargs={'pk': 10000})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
