from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from twitter_app.forms import AuthenticateForm, UserCreateForm, TweetForm
from twitter_app.models import Tweet


def index(request, auth_form=None, user_form=None):
  if request.user.is_authenticated():
    tweet_form = TweetForm()
    user = request.user
    tweets_self = Tweet.objects.filter(user=user.id)
    tweets_buddies = Tweet.objects.filter(user_userprofile_in=user.profile.follows.all)
    tweets = tweets_self | tweets_buddies

    return render(request,
                  'buddies.html',
                  {'tweet_form':tweet_form,'user':user,
                   'tweets':tweets,
                   'next_url': '/',})

  else:
   #If the user in question is not logged in
    auth_form = auth_form or AuthenticateForm()
    user_form = user_form or UserCreateForm()

    return render(request,
                   'home.html',
                   {'auth_form':auth_form,'user_form':user_form, })


    
def login_view(request):
  if request.method == 'POST':
    form = AuthenticateForm(data=request.POST)
    if form.is_valid():
      login(request, form.get_user())
    else:
      return index(request, auth_form=form)
  return redirect('/')


def logout_view(request):
  logout(request)
  return redirect('/')


def signup(request):
  user_form = UserCreateForm(data=request.POST)
  if request.method == 'POST':
    if user_form.is_valid():
      username=user_form.clean_username()
      password=user_form.clean_password2()
      user_form.save()
      user = authenticate(username = username, password=password)
      login(request, user)
      return redirect('/')
    else:
      return index(request, user_form=user_form)
  return redirect('/')
