from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Car

class CarsTests(TestCase):
   @classmethod
   def setUpTestData(cls):
      testuser1 = get_user_model().objects.create_user(
        username= 'test_user',
        email="test@email.com",
        password="1234") 

      test_car = Car.objects.create(
        buyer_id = testuser1,
        model = "test_car",
        brand = "test des",
        price = "18000",
        is_bought =False)

   def test_str_method(self):
       car =Car.objects.get(id=1) 
       self.assertEqual(str(car.model), "test_car")
