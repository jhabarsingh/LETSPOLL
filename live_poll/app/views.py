from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from .models import Poll, PollOptions
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from .serializers import PollSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from django.conf import settings

# Create your views here.


def home(request, *args, **kwargs):
	return render(request, 'index.html')


def create_poll(request, *args, **kwargs):
	if request.user.is_superuser:
		return render(request, 'create_poll.html')
	return render(request, 'login.html')

def save_poll(request, *args, **kwargs):
	question = request.POST.get('question')
	options = request.POST.get('options')
	options_arr = []
	for i in range(int(options)):
		options_arr.append(request.POST.get("option" + str(i+1)))

	print(options_arr)
	if question:
		poll = Poll(question=question)
		poll.save()

	for i in options_arr:
		if i != None:
			poll_options = PollOptions(question=poll, option=i)
			poll_options.save()

	return redirect(reverse('poll:create_poll'))

def show_polls(request, *args, **kwargs):
    contact_list = Poll.objects.all()
    paginator = Paginator(contact_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'all_polls.html', {'page_obj': page_obj, 'cs':settings.REAL_SITE})


@api_view(['GET', 'POST'])
def get_data(request, id, *args, **kwargs):
	if request.method == 'POST':
		id = id
		serializer = PollSerializer(Poll.objects.all().get(id=id))
		return Response(serializer.data)
	return JsonResponse({'msg': 'Invalid URL'})	


def poll_result(request, id, *args, **kwargs):
	return render(request, 'poll_result.html', {'id':id})


def admin_login(request, *args, **kwargs):
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = authenticate(request, username=username, password=password)
	print(user)
	if user:
		print(1)

		login(request, user)
		return redirect(reverse('poll:create_poll'))
	return render(request, 'login.html')

def polling(request, id, *args, **kwargs):
	if request.method == 'POST':
		uid = request.POST.get('id')
		if uid:
			poll_option = PollOptions.objects.all().filter(id=uid).first()
			poll_option.value = poll_option.value + 1
			poll_option.save()
			return redirect('poll:poll_result', id=id)
	return render(request, 'polling.html', {'id':id})

def admin_logout(request, *args, **kwargs):
	if request.POST.get('logout') == 'ok':
		logout(request)
	return render(request, 'login.html')