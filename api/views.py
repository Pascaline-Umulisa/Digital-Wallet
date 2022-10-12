from django.shortcuts import render
from rest_framework import viewsets
from wallet import models
from . import serializer

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