from rest_framework import viewsets, permissions, status, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import redirect
import requests


class RegisterUser(APIView):
    """User registration API."""


    def get(self, request):
        return redirect('https://oauth.yandex.ru/authorize?response_type=code&client_id=6e05c91a25f74e4c8661025fc46baa2b')


class CreateToken(APIView):
    """Get token API."""

    def get(self, request):
        print(request)
        print(request.args)
        if request.args.get('code'):
            code = request.args.get('code')

        res = requests.post(f'https://oauth.yandex.ru/token', data={'grant_type': 'authorization_code',
                                                            'code': code,
                                                            'client_id': '6e0534534dffdfg',
                                                            'client_secret': '2566dfgdfgdfgd345345345345'})
        if "error" in res:
            return Response({"error": res["error"]}, status=status.HTTP_400_BAD_REQUEST)
        # Token creation!
        return Response({"access": res["access"]}, status=status.HTTP_200_OK)