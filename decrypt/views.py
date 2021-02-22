from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from decrypt import serializers


class DecryptMessage(APIView):
    serializer_class = serializers.DecryptMessageSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            decrypted_data = serializer.decrypt_message()
            response = {
                "DecryptedMessage": decrypted_data.data
            }
            response_status = status.HTTP_200_OK
        else:
            response = serializer.errors
            response_status = status.HTTP_400_BAD_REQUEST
        return Response(response, status=response_status)



class encryptMessage(APIView):
    serializer_class = serializers.encryptMessageSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            encrypted_data = serializer.encrypt_message()
            response = encrypted_data
            response_status = status.HTTP_200_OK
        else:
            response = serializer.errors
            response_status = status.HTTP_400_BAD_REQUEST
        return Response(response, status=response_status)



