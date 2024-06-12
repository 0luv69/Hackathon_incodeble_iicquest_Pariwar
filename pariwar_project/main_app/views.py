# from django.shortcuts import render

# # Create your views here.


# # Accounts Api 

# class LoginApi(APIView):
#     def post(self, request):
#         data = request.data 
#         username = data.get('username')
#         password = data.get('password')
#         if not username or not password:
#             return Response({'error': 'Username & Password Fields is required', 'login': False}, status=status.HTTP_400_BAD_REQUEST)
        

#         user = authenticate(username=username, password=password)
#         if user is not None:
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 'login': True,
#                 'access': str(refresh.access_token),
#                 'refresh': str(refresh),
#             }, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': 'Invalid credentials', 'login':False}, status=status.HTTP_401_UNAUTHORIZED)

# class RegisterApi(APIView):
#     def post(self, request):
#         data = request.data 
#         email_token = str(random.randint(1000, 9999)) 
#         data['email_token'] = email_token
#         serializer = UserSerializer(data=data)
#         if serializer.is_valid():
#             user = serializer.save()
#             send_account_activation_email(user.email, email_token, user)
#             return Response({'posted':True, 'id': user.id})
        
#         elif 'username' in serializer.errors and serializer.errors['username'][0].code == 'unique':
#             return Response({"error": "Username already exists", "posted": False}, status=status.HTTP_400_BAD_REQUEST)
#         return Response({"error": serializer.errors, "posted": False}, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# def email_verify_token(request):
#     data = request.data
#     id = data.get('id')
#     token = data.get('emailtoken')
    
#     try:
#         user = User.objects.get(id = id)
#         bio_obj = Bio.objects.get(user__id=id, email_token=token)
#         bio_obj.is_verified = True
#         bio_obj.save()

#         refresh = RefreshToken.for_user(user)  # Generate JWT token
#         return Response({
#                 'verified': True,
#                 'id': user.pk,
#                 'username':user.username,
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#             }, status=status.HTTP_201_CREATED)

#     except User.DoesNotExist:
#         return Response({
#             'verified':False,
#             'message': 'Invalid ID or token',
#         }, status=403)
#     except Exception as e:
#         return Response({
#             'verified':False,
#             'message': f'An unexpected error occurred,{e}'
#         }, status=500)

