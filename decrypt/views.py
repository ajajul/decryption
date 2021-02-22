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
            message = serializer.decrypt_message()
            response = {"DecryptedMessage": message}
            response_status = status.HTTP_200_OK
        else:
            response = serializer.errors
            response_status = status.HTTP_400_BAD_REQUEST
        return Response(response, status=response_status)



