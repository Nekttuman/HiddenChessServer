from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


# @permission_classes([AllowAny])
# def index(request):
#     if request.user.is_authenticated:
#         # Пользователь вошел в систему, выполните действия для авторизованных пользователей
#         user = request.user
#         # ...
#         return JsonResponse({"mess": "not auth"})
#     else:
#         data = {'key1': 'value1', 'key2': 'value2'}
#         print(request.GET.get('param1', None), request.GET.get('param2', None))
#         return JsonResponse(data)

@permission_classes([AllowAny])
def check_connection(request):
    return JsonResponse({'message': 'Connection available'})



# @authentication_classes([SessionAuthentication])
@permission_classes([AllowAny])
# @csrf_exempt
@api_view(['POST'])
def api_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'message': 'Login failed'}, status=401)
