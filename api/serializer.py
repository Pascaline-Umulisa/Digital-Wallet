from pyexpat import model
from rest_framework import serializers
from wallet import models

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Customer
        fields=('first_name','email','age','address')  

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Wallet
        fields=('balance','customer','amount','date_created','status','currency','history','pin') 

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Account
        fields=('account_name','account_number','account_type','account_balance','wallet') 
        
class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Card
        fields=('card_number','card_type','expiry_date','date_of_issue','security_code','wallet','account','issuer') 
        
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Transaction
        fields=('message','wallet','transaction_description','transaction_amount','transaction_charge','transaction_type','origin_account','destination_account') 
        
class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Loan
        fields=('loan_id','loan_type','loan_balance','amount','guaranter','issuer','wallet') 
        
class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Receipt
        fields=('receipt_type','date','receipt_number','number','transaction','receipt_file') 
        
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Notification
        fields=('date','title','message','recipient') 