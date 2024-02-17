from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserForm
from .serializers import UserFormSerializer
from django.core.mail import send_mail

@api_view(['POST'])
def submit_form(request):
    serializer = UserFormSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        subject = 'Form Submission Confirmation'
        message = 'Thank you for submitting the form!'
        from_email = 'sender email address'
        to_email = serializer.data['email']
        send_mail(subject, message, from_email, [to_email])
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_forms(request):
    forms = UserForm.objects.all()
    serializer = UserFormSerializer(forms, many=True)
    return Response(serializer.data)
