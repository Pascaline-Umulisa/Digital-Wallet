from django.urls import path
from . import views

urlpatterns=[
path("registercustomer/", views.register_customer, name="customer"),
path("customers/", views.list_customers, name="customers"),

path("registeraccount/", views.register_account, name="account"),
path("accounts/", views.list_account, name="accounts"),

path("registercard/", views.register_card, name="card"),
path("cards/", views.list_card, name="cards"),

path("registercurrency/", views.register_currency, name="currency"),
path("currencies/", views.list_currency, name="currencies"),

path("registerloan/", views.register_loan, name="loan"),
path("loans/", views.list_loan, name="loans"),

path("registernotification/", views.register_notification, name="notification"),
path("notifications/", views.list_notification, name="notifications"),

path("registerreceipt/", views.register_receipt, name="receipt"),
path("receipts/", views.list_receipt, name="receipts"),

path("registerreward/", views.register_reward, name="reward"),
path("rewards/", views.list_reward, name="rewards"),

path("registerthirdparty/", views.register_third_party, name="thirdParty"),
path("thirdparties/", views.list_third_party, name="thirdparties"),

path("registertransaction/", views.register_transaction, name="transaction"),
path("transactions/", views.list_transaction, name="transactions"),

path("registerwallet/", views.register_wallet, name="wallet"),
path("wallets/", views.list_wallet, name="wallets"),]