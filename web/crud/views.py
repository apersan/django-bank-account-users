from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import UserForm
from .models import User


@login_required(login_url='/admin')
def view_user_list(request):
    if request.user.has_perm('crud.view_user') is False and request.user.is_superuser is False:
        return HttpResponse("You don't have access to this page.")
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'view_user_list.html', context)


@login_required(login_url='/admin')
def add_user(request):
    if request.user.has_perm('crud.add_user') is False and request.user.is_superuser is False:
        return HttpResponse("You don't have access to this page.")
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.creator = request.user
            form.save()
            return redirect('view_user_list')
        else:
            print(form.errors)
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})
