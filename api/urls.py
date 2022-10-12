from django.urls import path, include
from rest_framework import routers
from . import views

router=routers.DefaultRouter()
router.register('customers', views.CustomerViewSet)
router.register('wallets', views.WalletViewSet)
router.register('accounts', views.AccountViewSet)
router.register('cards', views.CardViewSet)
router.register('transactions', views.TransactionViewSet)
router.register('loans', views.LoanViewSet)
router.register('receipts', views.ReceiptViewSet)
router.register('notifications', views.NotificationViewSet)


urlpatterns = [
    path('', include(router.urls))
]
