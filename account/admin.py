from django.contrib import admin
from .models import Account , Transaction
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm , CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Account
    list_display = ['username']

class CustomTransaction(admin.ModelAdmin):
    model = Transaction
    list_display = ['account_id', 'type','value','date']

admin.site.register(Account, CustomUserAdmin)
admin.site.register(Transaction , CustomTransaction)