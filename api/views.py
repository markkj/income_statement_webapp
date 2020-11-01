from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from account.models import Account , Transaction
from account.forms import AddTransaction
from django.http.response import HttpResponseNotAllowed
from datetime import datetime


def add_statement(request):
    hist_trans = query_transaction(request)
    todayreport = today_report(request)
    profilereport = get_all_total(request)
    if request.method == 'POST':
        form = AddTransaction(request.POST)
        print(request.POST)
        if form.is_valid():
            type = form.cleaned_data.get('type')
            value = form.cleaned_data.get('value')
            ps  = form.cleaned_data.get('ps')
            trans = Transaction()
            trans.account_id = request.user
            trans.value = value
            trans.type = type
            trans.ps = ps
            trans.save()
            
            acc = Account.objects.get(id=request.user.id)
            if type == 'IN':
                acc.total_in += value
            else:
                acc.total_ex += value
            acc.total = acc.total_in - acc.total_ex
            acc.save()
            return redirect('/')
        else:
            return render(request, 'index.html', {
                'form': form,
                'hist_trans':hist_trans,
                'today_report':todayreport,
                'profilereport':profilereport
                })
    else:
        return HttpResponseNotAllowed(['POST'])

def query_transaction(request):
    hist_trans = Transaction.objects.filter(account_id=request.user.id).order_by('-date')
    return hist_trans

def today_report(request):
    hist_trans = Transaction.objects.filter(account_id=request.user.id,date__year=datetime.today().year, 
                      date__month=datetime.today().month,date__day=datetime.today().day)
    total_in = 0
    total_ex = 0
    total = 0
    for his in hist_trans:
        if his.type == 'IN':
            total_in += his.value
        elif his.type == 'EX':
            total_ex += his.value
    total = total_in - total_ex
    todayreport = {
        'total_in':total_in,
        'total_ex':total_ex,
        'total':total
    }
    return todayreport

def get_all_total(request):
    acc = Account.objects.get(id=request.user.id)
    data_acc = {
        'total_in':acc.total_in,
        'total_ex':acc.total_ex,
        'total':acc.total
    }
    print(data_acc)
    return data_acc