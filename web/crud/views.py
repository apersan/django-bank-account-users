from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
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
