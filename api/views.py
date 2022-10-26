from django.shortcuts import render
from rest_framework import viewsets
from wallet import models
from . import serializer
from rest_framework import views
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    queryset=models.Customer.objects.all()
    serializer_class=serializer.CustomerSerializer
    
class WalletViewSet(viewsets.ModelViewSet):
    queryset=models.Wallet.objects.all()
    serializer_class=serializer.WalletSerializer
    
class AccountViewSet(viewsets.ModelViewSet):
    queryset=models.Account.objects.all()
    serializer_class=serializer.AccountSerializer
    
class CardViewSet(viewsets.ModelViewSet):
    queryset=models.Card.objects.all()
    serializer_class=serializer.CardSerializer
    
class TransactionViewSet(viewsets.ModelViewSet):
    queryset=models.Transaction.objects.all()
    serializer_class=serializer.TransactionSerializer
    
class LoanViewSet(viewsets.ModelViewSet):
    queryset=models.Loan.objects.all()
    serializer_class=serializer.LoanSerializer
    
class ReceiptViewSet(viewsets.ModelViewSet):
    queryset=models.Receipt.objects.all()
    serializer_class=serializer.ReceiptSerializer
    
class NotificationViewSet(viewsets.ModelViewSet):
    queryset=models.Notification.objects.all()
    serializer_class=serializer.NotificationSerializer
    
class AccountDepositView(views.APIView):
   def post(self, request, format=None):       
       account_id = request.data["account_id"]
       amount = request.data["amount"]
       try:
           account = models.Account.objects.get(id=account_id)
       except ObjectDoesNotExist:
           return Response("Account Not Found", status=404)
      
       message, status = account.deposit(amount)
       return Response(message, status=status)
   


class AccountTransferView(views.APIView):
   def post(self, request, format=None):       
       account_id = request.data["account_id"]
       destination=request.data["account2_id"]
       amount = request.data["amount"]
       try:
           account = models.Account.objects.get(id=account_id)
           destination=models.Account.objects.get(id=destination)
       except ObjectDoesNotExist:
           return Response("Account Not Found", status=404)
      
       message, status = account.transfer(destination,amount)
       return Response(message, status=status)
   
class AccountWithdrawView(views.APIView):
   def post(self, request, format=None):       
       account_id = request.data["account_id"]
       amount = request.data["amount"]
       try:
           account = models.Account.objects.get(id=account_id)
       except ObjectDoesNotExist:
           return Response("Account Not Found", status=404)
      
       message, status = account.withdraw(amount)
       return Response(message, status=status)