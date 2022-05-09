from django.contrib.auth.decorators import login_required
from email import message
from multiprocessing import context
from webbrowser import get
from django.shortcuts import render, redirect

from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from user.models import Account
from .models import ThreadModel, Messages
from .forms import ThreadForm, MessageForm

from django.core.files.storage import default_storage
from django.db.models import Q 
# Create your views here.
@login_required
def messenger(request):
	return render(request, 'messenger.html', {})

class ListThreads(View):
    def get(self, request, *args, **kwargs):
        threads = ThreadModel.objects.filter(Q(user=request.user) | Q(receiver=request.user))
        context = {
            'model': threads
        }
        return render(request, 'messenger.html', context)

class CreateThread(View):
    def post(self, request, username, *args, **kwargs):
        form = ThreadForm(request.POST)
        try:
            receiver = Account.objects.get(username=username)
            if ThreadModel.objects.filter(user=request.user, receiver=receiver).exists():
                thread = ThreadModel.objects.filter(user=request.user, receiver=receiver)[0]
                return redirect('thread', pk=thread.pk)
            elif ThreadModel.objects.filter(user=receiver, receiver=request.user).exists():
                thread = ThreadModel.objects.filter(user=receiver, receiver=request.user)[0]
                return redirect('thread', pk=thread.pk)

            if form.is_valid():
                thread = ThreadModel(
                    user = request.user,
                    receiver = receiver
                )
                thread.save()
                return redirect('thread', pk=thread.pk)
        except:
            return redirect('create-thread')

class ThreadView(View):
    def get(self, request, pk, *args, **kwargs):
        form = MessageForm()
        model = ThreadModel.objects.all()
        thread = ThreadModel.objects.get(pk=pk)
        message_list = Messages.objects.filter(thread__pk__contains=pk)
        context = {
            'thread': thread,
            'form': form,
            'model': model,
            'message_list': message_list
        }

        return render(request, 'messenger.html', context)
class openMessenger(View):
    def get(self, request, *args, **kwargs):
        form = MessageForm()
        model = ThreadModel.objects.all()
        context = {
            'form': form,
            'model': model
        }
        return render(request, 'messenger.html', context)


class CreateMessage(View):
    def post(self, request, pk, *args, **kwargs):
        thread = ThreadModel.objects.get(pk=pk)
        if thread.receiver == request.user:
            receiver = thread.user
        else:
            receiver = thread.receiver

        message = Messages(
            thread=thread,
            sender_user=request.user,
            receiver_user=receiver,
            body=request.POST.get('message')
        )

        message.save()
        return redirect('thread', pk=pk)
