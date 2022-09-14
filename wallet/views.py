from django.shortcuts import render
from .forms import CustomerRegistrationForm, AccountRegistrationForm,WalletRegistrationForm,ThirdPartyRegistrationForm,TransactionRegistrationForm,ReceiptRegistrationForm,RewardRegistrationForm,CardRegistrationForm,CurrencyRegistrationForm,NotificationRegistrationForm,LoanRegistrationForm
from . import models
# Create your views here.
def register_customer(request):
    if request.method == 'POST':
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=CustomerRegistrationForm()
    return render(request, 'wallet/register_customer.html',{'form':form})

def list_customers(request):
        customers=models.Customer.objects.all()
        return render(request, 'wallet/customer_list.html',{'customers':customers})



def register_account(request):
    if request.method == 'POST':
        form=AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=AccountRegistrationForm()
    return render(request,"wallet/register_account.html",{"form":form})

def list_account(request):
        accounts=models.Account.objects.all()
        return render(request, 'wallet/account_list.html',{'accounts':accounts})



def register_wallet(request):
    if request.method == 'POST':
        form=WalletRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=WalletRegistrationForm()
    return render(request,"wallet/register_wallet.html",{"form":form})

def list_wallet(request):
        wallets=models.Wallet.objects.all()
        return render(request, 'wallet/wallet_list.html',{'wallets':wallets})




def register_third_party(request):
    if request.method == 'POST':
        form=ThirdPartyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ThirdPartyRegistrationForm()
    return render(request,"wallet/register_third_party.html",{"form":form})

def list_third_party(request):
        third_parties=models.ThirdParty.objects.all()
        return render(request, 'wallet/third_party_list.html',{'third_parties':third_parties})




def register_transaction(request):
    if request.method == 'POST':
        form=TransactionRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=TransactionRegistrationForm()
    return render(request,"wallet/register_transaction.html",{"form":form})
    
def list_transaction(request):
        transactions=models.Transaction.objects.all()
        return render(request, 'wallet/transaction_list.html',{'transactions':transactions})



def register_receipt(request):
    if request.method == 'POST':
        form=ReceiptRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ReceiptRegistrationForm()
    return render(request,"wallet/register_receipt.html",{"form":form})
    
def list_receipt(request):
        receipts=models.Receipt.objects.all()
        return render(request, 'wallet/receipt_list.html',{'receipts':receipts})




def register_reward(request):
    if request.method == 'POST':
        form=RewardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=RewardRegistrationForm()
    return render(request,"wallet/register_reward.html",{"form":form})
    
def list_reward(request):
        rewards=models.Reward.objects.all()
        return render(request, 'wallet/reward_list.html',{'rewards':rewards})




def register_card(request):
    if request.method == 'POST':
        form=CardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=CardRegistrationForm()
    return render(request,"wallet/register_card.html",{"form":form})
    
def list_card(request):
        cards=models.Card.objects.all()
        return render(request, 'wallet/card_list.html',{'cards':cards})




def register_currency(request):
    if request.method == 'POST':
        form=CurrencyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=CurrencyRegistrationForm()
    return render(request,"wallet/register_currency.html",{"form":form})
    
def list_currency(request):
        currencies=models.Currency.objects.all()
        return render(request, 'wallet/currency_list.html',{'currencies':currencies})




def register_notification(request):
    if request.method == 'POST':
        form=NotificationRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=NotificationRegistrationForm()
    return render(request,"wallet/register_notification.html",{"form":form})
    
def list_notification(request):
        notifications=models.Notification.objects.all()
        return render(request, 'wallet/notification_list.html',{'notifications':notifications})




def register_loan(request):
    if request.method == 'POST':
        form=LoanRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=LoanRegistrationForm()
    return render(request,"wallet/register_loan.html",{"form":form})
    
def list_loan(request):
        loans=models.Loan.objects.all()
        return render(request, 'wallet/loan_list.html',{'loans':loans})
