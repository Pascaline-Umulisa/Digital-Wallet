from django.urls import path
from . import views

urlpatterns=[
path("registercustomer/", views.register_customer, name="customer"),
path("customers/", views.list_customers, name="customers"),
path('customers/<int:id>/', views.customer_profile, name="customer_profile"),
path('customers/edit/<int:id>/',views.edit_customer, name="edit_customer"),

path("registeraccount/", views.register_account, name="account"),
path("accounts/", views.list_account, name="accounts"),
path('accounts/<int:id>/', views.account_profile, name="account_profile"),
path('accounts/edit/<int:id>/',views.edit_account, name="edit_account"),

path("registercard/", views.register_card, name="card"),
path("cards/", views.list_card, name="cards"),
path('cards/<int:id>/', views.card_profile, name="card_profile"),
path('cards/edit/<int:id>/',views.edit_card, name="edit_card"),

path("registercurrency/", views.register_currency, name="currency"),
path("currencies/", views.list_currency, name="currencies"),

path("registerloan/", views.register_loan, name="loan"),
path("loans/", views.list_loan, name="loans"),

path("registernotification/", views.register_notification, name="notification"),
path("notifications/", views.list_notification, name="notifications"),

path("registerreceipt/", views.register_receipt, name="receipt"),
path("receipts/", views.list_receipt, name="receipts"),
path('receipts/<int:id>/', views.receipt_profile, name="receipt_profile"),
path('receipts/edit/<int:id>/',views.edit_receipt, name="edit_receipt"),

path("registerreward/", views.register_reward, name="reward"),
path("rewards/", views.list_reward, name="rewards"),

path("registerthirdparty/", views.register_third_party, name="thirdParty"),
path("thirdparties/", views.list_third_party, name="thirdparties"),

path("registertransaction/", views.register_transaction, name="transaction"),
path("transactions/", views.list_transaction, name="transactions"),
path('transactions/<int:id>/', views.transaction_profile, name="transaction_profile"),
path('transactions/edit/<int:id>/',views.edit_transaction, name="edit_transaction"),

path("registerwallet/", views.register_wallet, name="wallet"),
path("wallets/", views.list_wallet, name="wallets"),
path('wallets/<int:id>/', views.wallet_profile, name="wallet_profile"),
path('wallets/edit/<int:id>/',views.edit_wallet, name="edit_wallet"),]