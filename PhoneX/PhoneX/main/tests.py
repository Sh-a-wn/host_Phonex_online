from django.test import TestCase, Client
from django.urls import reverse
from main.models import Make


# Create your tests here.
class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.homepage_url = reverse('homepage')
        self.brands_url = reverse('brands')
        self.addBrand_url = reverse('addBrand')
        self.minimum_requirements = Make.objects.create(name='Iphone 15', price=2000000)


    def test_homepage_url(self):
        response = self.client.get(self.homepage_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'homepage.html')

    def test_brands_url(self):
        response = self.client.get(self.brands_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'brands.html')

    def test_addBrand_POST(self):
        new_brand = Make.objects.create(name='Itel', condition=True, price=100000, description='4 GB RAM', color='Red')

        response = self.client.post(self.addBrand_url)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.minimum_requirements.name, 'Iphone 15')
        self.assertEquals(new_brand.name, "Itel")
        self.assertTemplateUsed(response, 'add_Brand.html')
        