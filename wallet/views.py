from django.shortcuts import render
from . import views
from . import models
# Create your views here.
def register_customer(request):
    if request.method == 'POST':
        form=views.CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=views.CustomerRegistrationForm()
    return render(request, 'wallet/register_customer.html',{'form':form})

def list_customers(request):
        customers=models.Customer.objects.all()
        return render(request, 'wallet/customer_list.html',{'customers':customers})



def register_account(request):
    if request.method == 'POST':
        form=views.AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=views.AccountRegistrationForm()
    return render(request,"wallet/register_account.html",{"form":form})

def list_account(request):
        accounts=models.Account.objects.all()
        return render(request, 'wallet/account_list.html',{'accounts':accounts})



def register_wallet(request):
    if request.method == 'POST':
        form=views.WalletRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=views.WalletRegistrationForm()
    return render(request,"wallet/register_wallet.html",{"form":form})

def list_wallet(request):
        wallets=models.Wallet.objects.all()
        return render(request, 'wallet/wallet_list.html',{'wallets':wallets})




def register_third_party(request):
    if request.method == 'POST':
        form=views.ThirdPartyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=views.ThirdPartyRegistrationForm()
    return render(request,"wallet/register_third_party.html",{"form":form})

def list_third_party(request):
        third_parties=models.ThirdParty.objects.all()
        return render(request, 'wallet/third_party_list.html',{'third_parties':third_parties})




def register_transaction(request):
    if request.method == 'POST':
        form=views.TransactionRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=views.TransactionRegistrationForm()
    return render(request,"wallet/register_transaction.html",{"form":form})
    
def list_transaction(request):
        transactions=models.Transaction.objects.all()
        return render(request, 'wallet/transaction_list.html',{'transactions':transactions})



def register_receipt(request):
    if request.method == 'POST':
        form=views.ReceiptRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=views.ReceiptRegistrationForm()
    return render(request,"wallet/register_receipt.html",{"form":form})
    
def list_receipt(request):
        receipts=models.Receipt.objects.all()
        return render(request, 'wallet/receipt_list.html',{'receipts':receipts})




def register_reward(request):
    if request.method == 'POST':
        form=views.RewardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=views.RewardRegistrationForm()
    return render(request,"wallet/register_reward.html",{"form":form})
    
def list_reward(request):
        rewards=models.Reward.objects.all()
        return render(request, 'wallet/reward_list.html',{'rewards':rewards})




def register_card(request):
    if request.method == 'POST':
        form=views.CardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=views.CardRegistrationForm()
    return render(request,"wallet/register_card.html",{"form":form})
    
def list_card(request):
        cards=models.Card.objects.all()
        return render(request, 'wallet/card_list.html',{'cards':cards})




def register_currency(request):
    if request.method == 'POST':
        form=views.CurrencyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=views.CurrencyRegistrationForm()
    return render(request,"wallet/register_currency.html",{"form":form})
    
def list_currency(request):
        currencies=models.Currency.objects.all()
        return render(request, 'wallet/currency_list.html',{'currencies':currencies})




def register_notification(request):
    if request.method == 'POST':
        form=views.NotificationRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=views.NotificationRegistrationForm()
    return render(request,"wallet/register_notification.html",{"form":form})
    
def list_notification(request):
        notifications=models.Notification.objects.all()
        return render(request, 'wallet/notification_list.html',{'notifications':notifications})




def register_loan(request):
    if request.method == 'POST':
        form=views.LoanRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=views.LoanRegistrationForm()
    return render(request,"wallet/register_loan.html",{"form":form})
    
def list_loan(request):
        loans=models.Loan.objects.all()
        return render(request, 'wallet/loan_list.html',{'loans':loans})
