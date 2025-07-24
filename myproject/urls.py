from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('accounts.urls')),   # ⬅ root delegated to accounts
    path('admin/', admin.site.urls),
]
