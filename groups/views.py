from .models import Branches
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
	ListView,
	CreateView,
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.

class GroupListView(ListView):
	model = Branches
	template_name = 'groups/groups.html'
	context_object_name = 'group'
	ordering = ['-name']



class GroupCreateView(LoginRequiredMixin, CreateView):
	model = Branches
	fields = ['name','discripton']
	def form_valid(self, form):
		name = form.cleaned_data.get('name')
		messages.success(self.request, f'Group {name} Created!')
		form.instance.user = self.request.user
		return super().form_valid(form)

def error_404_view(request, exception):
	return render(request,'error404.html')

def error_500_view(request):
	return render(request,'error500.html')


def user_details_after(strategy, details, user=None, *args, **kwargs):
    messages.info(strategy.request,"Logged in with email:" + details['email'])



def valid(request ,backend, *args, **kwargs):
    try:
        messages.error(request, backend )
    except Exception as e:
        messages.error(request, str(e) )
    return redirect('login')