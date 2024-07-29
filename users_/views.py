from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth.models import User
from users_.api.serializers import UserSerializer, RegisterSerializer
from rest_framework.authtoken.models import Token

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)


@api_view(['POST'])
def register(request):
    
    # if(str(type(request.data)) == "<class 'dict'>"):
    #     account = User.objects.create_user(request.data.get('username'), request.data.get('email'), request.data.get('password'))
    #     data['response'] = "registration Successfully."
    #     data['username'] = request.data.get('username')
    #     data['email'] = request.data.get('email')
    #     token = Token.objects.get(user=account).key
    #     data['token'] = token
    #     print(data)
    #     return JsonResponse(data, status=status.HTTP_200_OK)
    
    serializer = RegisterSerializer(data=request.data)
    data = {}
    
    if serializer.is_valid():
        account = serializer.save()
        data['response'] = "registration Successfully."
        data['username'] = account.username
        data['email'] = account.email
        
        token = Token.objects.get(user=account).key
        data['token'] = token
        return JsonResponse(data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_200_OK)

@api_view(['POST'])
def logout(request):
    request.user.auth_token.delete()
    return JsonResponse({'detail': 'User logged out successfully.'}, status=status.HTTP_200_OK)