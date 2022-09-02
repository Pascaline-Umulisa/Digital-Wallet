from django.urls import path
from .views import register_customer, register_account,register_card,register_currency,register_loan,register_notification,register_receipt,register_reward,register_third_party,register_transaction,register_wallet

urlpatterns=[path("registercustomer/", register_customer, name="customer"),
path("registeraccount/", register_account, name="account"),
path("registercard/", register_card, name="card"),
path("registercurrency/", register_currency, name="currency"),
path("registerloan/", register_loan, name="loan"),
path("registernotification/", register_notification, name="notification"),
path("registerreceipt/", register_receipt, name="receipt"),
path("registerreward/", register_reward, name="reward"),
path("registerthirdparty/", register_third_party, name="thirdParty"),
path("registertransaction/", register_transaction, name="transaction"),
path("registerwallet/", register_wallet, name="wallet"),]