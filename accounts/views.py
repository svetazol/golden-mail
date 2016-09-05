from accounts.serializer import UserSerializer
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Permission, User
from django.shortcuts import render, redirect, render_to_response

# Create your views here.
from django.template.context_processors import csrf
from rest_framework.response import Response
from rest_framework.views import APIView


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],
                                        password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render_to_response('accounts/register.html', args)


class UserList(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)