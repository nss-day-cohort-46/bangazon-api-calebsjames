from bangazonapi.models.payment import Payment
import datetime
import json
from rest_framework import status
from rest_framework.test import APITestCase


class PaymentTests(APITestCase):
    def setUp(self) -> None:
        """
        Create a new account and create sample category
        """
        url = "/register"
        data = {"username": "steve", "password": "Admin8*", "email": "steve@stevebrownlee.com",
                "address": "100 Infinity Way", "phone_number": "555-1212", "first_name": "Steve", "last_name": "Brownlee"}
        response = self.client.post(url, data, format='json')
        json_response = json.loads(response.content)
        self.token = json_response["token"]
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    # def test_create_payment_type(self):
    #     """
    #     Ensure we can add a payment type for a customer.
    #     """
    #     # Add product to order
    #     url = "/paymenttypes"
    #     data = {
    #         "merchant_name": "American Express",
    #         "account_number": "111-1111-1111",
    #         "expiration_date": "2024-12-31",
    #         "create_date": datetime.date.today()
    #     }
    #     self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
    #     response = self.client.post(url, data, format='json')
    #     json_response = json.loads(response.content)

    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(json_response["merchant_name"], "American Express")
    #     self.assertEqual(json_response["account_number"], "111-1111-1111")
    #     self.assertEqual(json_response["expiration_date"], "2024-12-31")
    #     self.assertEqual(json_response["create_date"], str(datetime.date.today()))

    
    def test_delete_payment_type(self):
        """
        Ensure we can delete a payment_type.
        """
        payment_type = Payment()
        payment_type.merchant_name = "A"
        payment_type.account_number = "512312312"
        payment_type.customer_id = 1
        payment_type.expiration_date = "2022-01-01"
        payment_type.create_date = "2019-01-01"
        payment_type.save()
        


        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.delete(f"/paymenttypes/{payment_type.id}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)