from django.contrib import admin
# Register your models here.
from . import models
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'email')
    search_fields = ('first_name', 'last_name')
admin. site.register(models.Customer,CustomerAdmin)
    
class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_name', 'account_number', 'account_balance')
    search_fields = ('account_name', 'account_number')
admin.site.register(models.Account,AccountAdmin)
    
class WalletAdmin(admin.ModelAdmin): 
    list_display = ('customer', 'status', 'amount')
    search_fields = ('customer', 'status')
admin.site.register(models.Wallet,WalletAdmin)
    
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_type', 'transaction_description', 'transaction_amount')
    search_fields = ('transaction_type', 'transaction_description')
admin.site.register(models.Transaction,TransactionAdmin)
    
class CardAdmin(admin.ModelAdmin):   
    list_display = ('card_type', 'card_number', 'issuer')
    search_fields = ('card_type', 'card_number', 'issuer')
admin.site.register(models.Card,CardAdmin)
    
class ThirdPartyAdmin(admin.ModelAdmin): 
    list_display = ('wallet', 'issuer', 'transaction_amount')
    search_fields = ('wallet', 'issuer', 'transaction_amount')
admin.site.register(models.ThirdParty,ThirdPartyAdmin)
    
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('message', 'date', 'title')
    search_fields = ('message', 'date', 'title')
admin.site.register(models.Notification,NotificationAdmin)
    
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('date', 'receipt_type', 'number')
    search_fields = ('date', 'receipt_type', 'number')
admin.site.register(models.Receipt,ReceiptAdmin)
    
class LoanAdmin(admin.ModelAdmin):
    list_display = ('loan_type', 'guaranter', 'issuer')
    search_fields = ('loan_type', 'guaranter', 'issuer')
admin.site.register(models.Loan,LoanAdmin)
    
class RewardAdmin(admin.ModelAdmin):
    list_display = ('transaction', 'recipient', 'points')
    search_fields = ('transaction', 'recipient', 'points')
admin.site.register(models.Reward,RewardAdmin)
    
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('country', 'symbol', 'amount')
    search_fields = ('country', 'symbol', 'amount')
admin.site.register(models.Currency,CurrencyAdmin)
