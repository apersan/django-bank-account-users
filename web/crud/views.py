from django.shortcuts import render, redirect, get_object_or_404
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


@login_required(login_url='/admin')
def edit_user(request, pk):
    if request.user.has_perm('crud.change_user') is False and request.user.is_superuser is False:
        return HttpResponse("You don't have access to this page.")
    user = get_object_or_404(User, pk=pk)
    form = UserForm(request.POST or None, instance=user)
    if request.user != user.creator and request.user.is_superuser is False:
        return HttpResponse("You don't have permission to do this.")
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('view_user_list')
        else:
            print(form.errors)
    return render(request, 'edit_user.html', {'form': form})


@login_required(login_url='/admin')
def delete_user(request, pk):
    if request.user.has_perm('crud.delete_user') is False and request.user.is_superuser is False:
        return HttpResponse("You don't have access to this page.")
    user = get_object_or_404(User, pk=pk)
    if request.user != user.creator and request.user.is_superuser is False:
        return HttpResponse("You don't have permission to do this.")
    User.objects.filter(id=pk).delete()
    users = User.objects.all()

    context = {
        'users': users,
    }
    return render(request, 'view_user_list.html', context)
