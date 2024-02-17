from rest_framework import status
from rest_framework.response import Response
from .models import UserForm
from .serializers import UserFormSerializer,UserRegistrationSerializer,UserLoginSerializer
from django.core.mail import send_mail
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def submit_form(request):
    serializer = UserFormSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        subject = 'Form Submission Confirmation'
        message = 'Thank you for submitting the form!'
        from_email = 'sender@example.com'  # Update with your email
        to_email = serializer.data['email']
        send_mail(subject, message, from_email, [to_email])
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_forms(request):
    forms = UserForm.objects.all()
    serializer = UserFormSerializer(forms, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def user_registration(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def user_login(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(request, username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
