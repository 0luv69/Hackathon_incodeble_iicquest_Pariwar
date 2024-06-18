# Import Api Segment
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view

# Import Models & Serializer Segment
from django.contrib.auth.models import User
from main_app.serializer import *
from main_app.models import *
from .email import *

import random



# -----------------------------------------------------Accounts Api--------------------------------------------------------
 
class LoginApi(APIView):
    def post(self, request):
        data = request.data 
        username = data.get('username')
        password = data.get('password')
        if not username or not password:
            return Response({'message': 'username & password Fields is required', 'login': False}, status=status.HTTP_400_BAD_REQUEST)
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'posted': True,
                'user_id': user.pk,
                'user_name': user.username,
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials', 'posted':False}, status=status.HTTP_401_UNAUTHORIZED)

class RegisterApi(APIView):
    def post(self, request):
        data = request.data 
        email_token = str(random.randint(1000, 9999)) 
        data['email_token'] = email_token
        serializer = RegisterUserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            send_account_activation_email(user.email, email_token, user)
            return Response({'posted':True, 'id': user.id})
        
        elif 'username' in serializer.errors and serializer.errors['username'][0].code == 'unique':
            return Response({"message": "Username already exists", "posted": False}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": serializer.errors, "posted": False}, status=status.HTTP_400_BAD_REQUEST)



# -----------------------------------------------------Profile Api--------------------------------------------------------
#Get profile with User Id
@api_view(['POST'])
def get_profile(request):
    data = request.data
    try:
        user_id = data.get('id')
        user = User.objects.get(id=user_id)
        profile = ProfileModel.objects.get(user=user)
        serializer = GetProfile_Serializers(profile)
        return Response({'success': True, 'data': serializer.data})
    except User.DoesNotExist:
        return Response({'success': False, 'message': 'User not found'}, status=404)
    except ProfileModel.DoesNotExist:
        return Response({'success': False, 'message': 'Profile not found'}, status=404)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=500)



#               --------------------------------------Issue Segment-----------------------------------------

# Post New Issue 
@api_view(['POST'])
def Post_Issue(request):
        data = request.data
        serializer = PostIssueSerializer(data=data)
        if serializer.is_valid():
            serl =serializer.save()
            return Response({'posted':True, "payload": serl.data }) #LATER WE NEED TO REMOVE PAYLOAD
        else:
            return Response({'posted':False, "message" :serializer.errors})
    


#Get All Issue
@api_view(['POST'])
def Get_All_Issue(request):
    issuemodel = IssueModel.objects.all()
    serializer = IssueSerializer(issuemodel, many = True)
    return Response({'success':True, "payload": serializer.data})


#Get Issue with Charater Choice
@api_view(['POST'])
def Get_Issue_Charater(request):
    data = request.data
    try:
        id = data.get('id')
        character = ProfileModel.objects.get(user__id = id).character
        issuemodel = IssueModel.objects.filter(preferred_char= character)
        serializer = IssueSerializer(issuemodel, many = True)
        return Response({'success':True, "payload": serializer.data})
    except Exception as e:
        return Response({'success':False, "payload": []})


#Get Issue with User id
@api_view(['POST'])
def Get_Issue(request):
    data = request.data
    if data:
        try:
            id = data.get('id')
            issuemodel = IssueModel.objects.filter(issued_by__id= id)
            serializer = IssueSerializer(issuemodel, many = True)
            
            return Response({'success':True, "payload": serializer.data})
        except Exception as e:
            return Response({'success':False, "message": e, "hint": "Incorrect id of user"})
    return Response({'success':False, "message": "Got None or Incorrect id of user"})


#Get Issue with Issue id
@api_view(['POST'])
def Get_spefic_Issue(request):
    data = request.data
    try:
        id = data.get('issue_id')
        issuemodel = IssueModel.objects.get(id= id)
        serializer = IssueSerializer(issuemodel)
        return Response({'success':True, "payload": serializer.data})
    except Exception as e:
            return Response({'success':False, "message": e, "hint": "Incorrect id of user"})
    




# ----------------------------------------------------- Reply / Suggestion Segment-------------------------------------------------- 

# Post reply/Suggestion
@api_view(['POST'])
def Postreply(request):
        data = request.data
        serializer = PostReplySerializer(data=data)
        if serializer.is_valid():
            serl =serializer.save()
            return Response({'posted':True, "payload": serl.data })
        else:
            return Response({'posted':False, "message" :serializer.errors})



# Get Latest Suggestion to Issue
@api_view(['POST'])
def get_issue_reply(request):
    data = request.data
    id = data.get('id')
    try:
        latest_issue = IssueModel.objects.filter(issued_by__id=id).latest('created_at')
    except IssueModel.DoesNotExist:
        return Response({'success': False, 'message': 'id error, provide id with correction'})

    reply_model = ReplyModel.objects.filter(issued_by=latest_issue)
    serializer = ReplySerializer(reply_model, many=True)
    return Response({'success': True, 'payload': serializer.data})


# Get Suggestion With issued Id
@api_view(['POST'])
def get_reply_list(request):
    data = request.data
    issued_id = data.get('issued_id')

    issued_by = IssueModel.objects.get(id = issued_id)
    all_reply_model = ReplyModel.objects.filter(issued_by= issued_by)
    serializer = ReplySerializer(all_reply_model, many=True)






#       ----------------------------------------- Relation ---------------------------------------------

# Relation Update
@api_view(['POST'])
def relation_update(request):
    data = request.data
    try:
        suggested_by_id = data.get('suggested_by')
        issued_by_id = data.get('issued_by')

        if not suggested_by_id or not issued_by_id:
            return Response({'posted': False, 'message': 'Both suggested_by and issued_by must be provided.'}, status=400)

        suggested_by_user = User.objects.get(id=suggested_by_id)
        issued_by_user = User.objects.get(id=issued_by_id)

        issued_user_char = ProfileModel.objects.get(user=issued_by_user).character
        suggested_user_char = ProfileModel.objects.get(user=suggested_by_user).character

        relation_name = f"{suggested_user_char} and {issued_user_char}"
        relation_module = RelationModel.objects.create(
            issued_by=issued_by_user,
            suggested_by=suggested_by_user,
            relation_name=relation_name
        )
        
        serializer = RelationSerializer(relation_module)

        return Response({'posted': True, 'payload': serializer.data}, status=201)

    except User.DoesNotExist:
        return Response({'posted': False, 'message': 'Invalid user ID provided.'}, status=404)
        
    except ProfileModel.DoesNotExist:
        return Response({'posted': False, 'message': 'Profile for the provided user ID does not exist.'}, status=404)

    except Exception as e:
        return Response({'posted': False, 'message': str(e)}, status=400)
    


# Get Particular Relation
@api_view(['POST'])
def get_particular_relation(request):
    data = request.data

    user_id = data.get('id')

    try:
        user_obj = User.objects.get(id= user_id)
        relation_module = RelationModel.objects.filter(issued_by=user_obj)
        if not relation_module:
            relation_module = RelationModel.objects.filter(suggested_by=user_obj)


    except User.DoesNotExist:
        return Response({'posted': False, 'message':"User does not exits"}, status= 404)

    except Exception as e:
        return Response({'posted': False, 'message':e}, status= 404)


    serializer= RelationSerializer(relation_module, many= True)
    return Response({'posted': True, 'payload':serializer.data}, status=201)







#      ------------------------------------ Chat Segment ------------------------------------------------

# Get Chat with Relation Id 
@api_view(['POST'])
def get_chat(request):
    data = request.data
    try:
        relation_id = data.get('relation_id')

        relation_obj = RelationModel.objects.get(id = relation_id)
        chatmodel= ChatModel.objects.filter(relation= relation_obj)
        serializer = ChatSerializer(chatmodel, many= True)
        return Response({'success': True, "payload": serializer.data})
    
    except RelationModel.DoesNotExist:
        return Response({'success': False, 'message': "NO relation module found"})

    except Exception as e:
        return Response({'success': False, 'message': e})


# Post Chat 
@api_view(['POST'])
def post_chat(request):
    data = request.data
    try:
        sender_id = data.get('sender_id')
        message = data.get('message')
        relation_id = data.get('relation_id')
        if not relation_id and not sender_id:
            return Response({'success': False, 'message': 'relation_id or sender id is not alid'}, status=400)

        sender_urs_obj = User.objects.get(id=sender_id )
        relation_obj = RelationModel.objects.get(id = relation_id)
        chatmodel = ChatModel.objects.create(sender= sender_urs_obj,relation = relation_obj, message= message)
        return Response({'success': True})
    except Exception as e:
        return Response({'success': False, 'message': e})

    
