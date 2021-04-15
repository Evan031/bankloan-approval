import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# API Test to confirm response of HTTP 200


class API_TestCase(APITestCase):

    def test_prediction_api(self):
        data = {
            "Gender": 1,
            "Married": 0,
            "Dependents": 1,
            "Education": 1,
            "Self_Employed": 1,
            "ApplicantIncome": 2000,
            "CoapplicantIncome": 2500,
            "LoanAmount": 128000,
            "Loan_Amount_Term": 360,
            "Credit_History": 1,
            "Property_Area": 2,
            "csrfmiddlewaretoken": "oyivivvNMwALhcrx9P5ekaQCcpFq0Zs9Yynv7UMX3m3gmETFNxM0r8bhP3J9CUd0"
        }
        response = self.client.post('/api/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
