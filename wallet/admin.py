from django.contrib import admin
# Register your models here.
from .models import Account, Card, Customer,Currency, Loan, Notification, Receipt, Reward, ThirdParty, Transaction, Wallet
admin. site.register(Customer)
class Customer(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'email')
    search_fields = ('first_name', 'last_name')
    
admin.site.register(Account)
class Account(admin.ModelAdmin):
    list_display = ('account_name', 'account_number', 'amount')
    search_fields = ('account_name', 'account_number')
    
admin.site.register(Wallet)
class Wallet(admin.ModelAdmin): 
    list_display = ('customer', 'status', 'amount')
    search_fields = ('customer', 'status')
    
admin.site.register(Transaction)
class Transaction(admin.ModelAdmin):
    list_display = ('type', 'description', 'amount')
    search_fields = ('type', 'description')
    
admin.site.register(Card)
class Card(admin.ModelAdmin):   
    list_display = ('type', 'number', 'issuer')
    search_fields = ('type', 'number', 'issuer')
    
admin.site.register(ThirdParty)
class ThirdParty(admin.ModelAdmin): 
    list_display = ('wallet', 'issuer', 'amount')
    search_fields = ('wallet', 'issuer', 'amount')
    
admin.site.register(Notification)
class Notification(admin.ModelAdmin):
    list_display = ('message', 'date', 'title')
    search_fields = ('message', 'date', 'title')
    
admin.site.register(Receipt)
class Receipt(admin.ModelAdmin):
    list_display = ('date', 'type', 'number')
    search_fields = ('date', 'type', 'number')
    
admin.site.register(Loan)
class Loan(admin.ModelAdmin):
    list_display = ('type', 'guaranter', 'issuer')
    search_fields = ('type', 'guaranter', 'issuer')
    
admin.site.register(Reward)
class Reward(admin.ModelAdmin):
    list_display = ('transaction', 'recepient', 'points')
    search_fields = ('transaction', 'recepient', 'points')
    
admin.site.register(Currency)
class Currency(admin.ModelAdmin):
    list_display = ('country', 'symbol', 'amount')
    search_fields = ('country', 'symbol', 'amount')
