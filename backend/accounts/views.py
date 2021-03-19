from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

class SignupView(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def post(self, request, format=None):
        data = self.request.data
        
        name = data['name']
        email = data['email']
        password = data['password']
        cpassword = data['cpassword']
        
        if password == cpassword:
            if User.objects.filter(email=email).exists():
                return Response({'error': 'Email already exists'})
            else:
                if len(password) < 8:
                    return Response({'error': 'Password must be at least 8 characters long!'})
                else:
                    user = User.objects.create_user(email=email, name=name, password=password)
                    user.save()
                    return Response({'success': 'User created successfully!'})
        else:
            return Response({'error': 'Password fields do not match!'})