from django.urls import path
from .views import register_customer, register_account,register_card,register_currency,register_loan,register_notification,register_receipt,register_reward,register_third_party,register_transaction,register_wallet
from . import views

urlpatterns=[
path("registercustomer/", register_customer, name="customer"),
path("customers/", views.list_customers, name="customers"),

path("registeraccount/", register_account, name="account"),
path("accounts/", views.list_account, name="accounts"),

path("registercard/", register_card, name="card"),
path("cards/", views.list_card, name="cards"),

path("registercurrency/", register_currency, name="currency"),
path("currencie/", views, name="currencies"),

path("registerloan/", register_loan, name="loan"),
path("loans/", views, name="loans"),

path("registernotification/", register_notification, name="notification"),
path("notifications/", views, name="notifications"),

path("registerreceipt/", register_receipt, name="receipt"),
path("receipts/", views, name="receipts"),

path("registerreward/", register_reward, name="reward"),
path("rewards/", views, name="rewards"),

path("registerthirdparty/", register_third_party, name="thirdParty"),
path("thirdparties/", views, name="thirdparties"),

path("registertransaction/", register_transaction, name="transaction"),
path("transactions/", views, name="transactions"),

path("registerwallet/", register_wallet, name="wallet"),
path("wallets/", views, name="wallets"),]