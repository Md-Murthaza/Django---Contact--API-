from django.shortcuts import render
from .serializers import ContactSerializer
from .models import Contact
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404 
from rest_framework import filters
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ContactFilter
from rest_framework.permissions import IsAuthenticated
# Create your views here.

#GET METHOD TO RETRIVE ALL CONTACT
class ContactListView(APIView):
   
    def get(self,request):
        contacts = Contact.objects.all()
        filterset = ContactFilter(request.GET ,queryset = contacts)
        if filterset.is_valid():
            contacts = filterset.qs
        else:
            return Response({"message":"Invalid Filters","error":filterset.errors},status = status.HTTP_400_BAD_REQUEST)
        serializer = ContactSerializer(contacts,many=True)
        return Response({"message":"Contact list retrieved sucessfully","data":serializer.data},status=status.HTTP_200_OK)
   
#GET METHOD BY ID
class ContactDetailView(APIView):
    def get(self,request,pk):
        contact = get_object_or_404 (Contact,pk=pk)
        serializer = ContactSerializer(contact)
        return Response({"message": "Contact retrieved successfully", "data": serializer.data},status=status.HTTP_200_OK)


#POST METHOD FOR THE CONTACT
class ContactCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer = ContactSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": " New contact created successfully", "data": serializer.data},status=status.HTTP_200_OK)
        return Response({"message": "Failed to create contact", "errors": serializer.errors},status=status.HTTP_400_BAD_REQUEST)



#UPDATE METHOD FOR THE CONTACT

class ContactUpdateView(APIView):
    def put(self,request,pk):
        contact = get_object_or_404(Contact,pk=pk)
        serializer = ContactSerializer(contact,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Contact updated successfully", "data": serializer.data},status=status.HTTP_200_OK)
        return Response({"message": "Failed to update contact", "errors": serializer.errors},status = status.HTTP_400_BAD_REQUEST)



#DELETE METHOD FOR THE CONTACT
class ContactDeleteView(APIView):
    def delete(self,request,pk):
        contact = get_object_or_404(Contact,pk = pk)
        contact.delete()
        return Response({"message": "This contact has been deleted successfully"},status=status.HTTP_204_NO_CONTENT)







