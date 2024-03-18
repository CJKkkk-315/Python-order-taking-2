from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .serializers import ItemSerializer, MatchSerializer
from .serializers import UserSerializer
from .models import Item, Match
#from .models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404

from django.db.models import Q

class ItemView(viewsets.ModelViewSet):
			serializer_class = ItemSerializer
			queryset = Item.objects.all()

			def create(self, request):
					serializer = ItemSerializer(data=request.data)
					if serializer.is_valid():
							serializer.save()
							return Response({"status": "Successfully added item", "data": serializer.data}, status=status.HTTP_200_OK)
					else:
							return Response({"status": "Error, item cannot be added", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

			def patch(self, request, id=None):#update an item
					itemToUpdate = Item.objects.get(id=id)
					serializer = ItemSerializer(itemToUpdate, data=request.data, partial = True)#Partial is used to denote that not all fields may be filled
					if serializer.is_valid():
							serializer.save()
							return Response({"status": "Successfully updated item", "data": serializer.data})
					else:
							return Response({"status": "Error, item cannot be updated", "data": serializer.errors})

			def delete(self, request, id=None):#delete an item
					itemtoDelete = get_object_or_404(Item, id = id)
					itemtoDelete.delete()
					return Response({"status": "Item deleted successfully"})
			
			def get_queryset(self):
					queryset = super().get_queryset()
					price = self.request.GET.get('price')
					if price:
						queryset = queryset.filter(price=int(price))
					return queryset


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


''' Not used!?!?!?!?!?
class UserCreate(APIView):
    """ 
    Creates the user. 
    """

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/login/")
			messages.error(request, "Unsuccessful registration. Invalid information.")
		else:
			return render (request=request, template_name="main/register.html", context={"register_form":form})
	form = NewUserForm()
	return render (request=request, template_name="main/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/static/build/index.html")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("http://localhost:3000/")

# methods to add:
# USER STUFF
# (m) request user info - 
# return: UserID, User and Email | REQUEST
# parameters: UserID (ID)

def user_info_request(request):
	users = User.objects.get(username = request)
	serializer = UserSerializer(users)
	return Response(serializer.data, status=status.HTTP_200_OK)

# (m) delete a user -
# return: N/A
# parameters: UserID (ID)

def delete_user_request(request, UserID):
	user = int(UserID) == int(request.User.id)
	if not user:
		return Response(
			{"res": "Error, User with ID " + str(UserID) + ": not found."},
			status = status.HTTP_400_BAD_REQUEST
		)
	user_instance = request.User.id
	user_instance.delete()
	return Response(
		{"res": "User deleted successfully."},
		status = status.HTTP_200_OK
	)


# ----------

# ITEM STUFF
# (m) request item (specific) -
# return: the whole item
# parameters: ItemID, Username, Size, Brand, Item (Type!) | REQUEST
# parameters can be NULL

# @permission_classes([IsAuthenticated])
def item_specific_request(request):
	items = items.objects.filter(user = request.User.username)
	serializer = ItemSerializer(items, many = True)
	return Response(serializer.data, status=status.HTTP_200_OK)

# (m) create item -
# return: a message (STRING) that item was CREATED or NOT
# parameters: everything that an item has
# ID, Image, userImage, user, location, rating, title, item, size,
# brand, description, show | REQUEST

def create_item_request(request):
	serializer = ItemSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"status": "Success", "data": serializer.data}, status=status.HTTP_200_OK)
	else:
		return Response({"status": "Error", "data": serializer.data}, status=status.HTTP_400_BAD_REQUEST)

# (m) update item -
# return: a message (STRING) that item was UPDATED or NOT
# parameters: just like create item but | REQUEST
# parameters can be NULL
#PUT

def update_item_request(request, ItemID):
	item = (int(ItemID) == int(request.Item.id))
	if not item:
		return Response(
			{"res": "Error, Item with ID " + str(ItemID) +  ": not found."},
			status = status.HTTP_400_BAD_REQUEST
		)
	data = {
		'id': request.data.get('id'),
		'image': request.data.get('image'),
		'userImage': request.data.get('userImage'),
		'user': request.data.get('user'),
		'location': request.data.get('location'),
		'rating': request.data.get('rating'),
		'title': request.data.get('title'),
		'item': request.data.get('item'),
		'size': request.data.get('size'),
		'brand': request.data.get('brand'),
		'description': request.data.get('description'),
		'show': request.data.get('show')
	}

	serializer = ItemSerializer(instance = item, data = data, partial = True)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status = status.HTTP_200_OK)
	return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# (m) delete item -
# return: a message (STRING) that the item was DELETED or NOT
# parameters: ItemID (ID) | REQUEST

def delete_item_request(request, ItemID):
	item = (int(ItemID) == int(request.Item.id))
	if not item:
		return Response(
			{"res": "Error, Item with ID " + str(ItemID) +  ": not found."},
			status = status.HTTP_400_BAD_REQUEST
		)
	item_instance = request.Item.id
	item_instance.delete()
	return Response(
		{"res": "Item deleted successfully."},
		status = status.HTTP_200_OK
	)

class MoreItemViews(APIView):
    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "Successfully added item", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "Error, item cannot be added", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):#update an item
        itemToUpdate = Item.objects.get(id=id)
        serializer = ItemSerializer(itemToUpdate, data=request.data, partial = True)#Partial is used to denote that not all fields may be filled
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "Successfully updated item", "data": serializer.data})
        else:
            return Response({"status": "Error, item cannot be updated", "data": serializer.errors})

    def delete(self, request, id=None):#delete an item
        itemtoDelete = get_object_or_404(Item, id = id)
        itemtoDelete.delete()
        return Response({"status": "Item deleted successfully"})



class MoreUserViews(APIView):
    def delete(self, request, id=None):#Deletes a user
        userToDelete = get_object_or_404(User, id=id)
        userToDelete.delete()
        return Response({"status":"User deleted successfully"})




@api_view(['GET','POST'])
def item_list(request):
    if request.method == 'GET':
        price = request.GET.get('price')
        print(User.objects.all())
        if price:
            items = Item.objects.filter(price=int(price))
            serializer = ItemSerializer(items,many=True)
            return Response(serializer.data)
        else:
            items = Item.objects.all()
            serializer = ItemSerializer(items,many=True)
            return Response(serializer.data)

    elif(request.method == 'POST'):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET','PUT','DELETE'])
def item_details(request,pk):
    try:
        item = Item.objects.get(pk=pk)
    except item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ItemSerializer(item)
        print(type(serializer.data))
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ItemSerializer(item,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    # elif request.method == 'PATCH':
    #     itemToUpdate = Item.objects.get(id=pk)
    #     serializer = ItemSerializer(itemToUpdate, data=request.data, partial = True)#Partial is used to denote that not all fields may be filled
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({"status": "Successfully updated item", "data": serializer.data})
    #     else:
    #         return Response({"status": "Error, item cannot be updated", "data": serializer.errors})
    

    elif request.method == 'DELETE':
        try:
            item.delete()
            return Response({"status": "Item deleted successfully"})
        except:
            return Response({"status": "Error"})

@api_view(['GET','PUT','DELETE'])
def item_match(request,pk):
    # try:
        # item = Match.objects.get(pk=pk)
    # except:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # items = Match.objects.filter(Q(item1_id=pk) | Q(item2__id=pk))
        items = Match.objects.filter(item1_id=pk)
        serializer = MatchSerializer(items,many=T)
        return Response(serializer.data)
    
    elif(request.method == 'POST'):
        serializer = MatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    # elif request.method == 'PUT':
    #     serializer = ItemSerializer(item,request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)			

@api_view(['GET','PUT','DELETE', 'POST'])
def match(request):
    # try:
        # item = Match.objects.get(pk=pk)
    # except:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        pk = request.GET.get('pk')
        items = Match.objects.filter(item1_id=pk)
        serializer = MatchSerializer(items,many=True)
        return Response(serializer.data[0])
    
    if request.method == 'POST':
        serializer = MatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def match1(request):
    # try:
    # item = Match.objects.get(pk=pk)
    # except:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        pk = request.GET.get('pk')
        items = Match.objects.all()
        serializer = MatchSerializer(data=request.data)
        return Response(items[0].item2.user)

    if request.method == 'POST':
        serializer = MatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def matchedUser(request):
    # try:
        # item = Match.objects.get(pk=pk)
    # except:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        items = Match.objects.filter(pk=pk)
        serializer = MatchSerializer(items,many=True)
        print(type(serializer.data))
        return Response(serializer.data)
    
    if(request.method == 'POST'):
        serializer = MatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def matchUUser(request,pk):
    if request.method == 'GET':
        items = User.objects.filter(id=pk)
        serializer = UserSerializer(User.objects)
        return Response(serializer.data)


