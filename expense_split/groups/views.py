from django.shortcuts import render
from django.core.exceptions import ValidationError, ObjectDoesNotExist, PermissionDenied
from .models import Group
from .forms import GroupForm, EmailForm, DeleteForm
from werkzeug.security import generate_password_hash, check_password_hash
# Create your views here.

def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group_name = form.cleaned_data['group_name']
            members = form.cleaned_data['members']
            password = form.cleaned_data['password']
            if group_name is None:
                raise ValidationError({'group_name': 'Group name cannot be empty'})
            if members is None:
                raise ValidationError({'members': 'Members cannot be 0'})
            if password is None:
                raise ValidationError({'password': 'Password cannot be empty'})
            group = Group()
            group.group_name = group_name
            group.members = members
            group.password = generate_password_hash(password)
            group.save()
            note = "Group successfully created"
            return render(request, 'creategroup.html', {'form': form, 'note': note})
    else:
        form = GroupForm()
        return render(request, 'creategroup.html', {'form': form})

def email_group(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            group_name = form.cleaned_data['group_name']
            group = Group.objects.get(group_name=group_name)
            if group is None:
                raise ObjectDoesNotExist
            if not check_password_hash(group.password, form.cleaned_data['password']):
                print(group.password)
                raise PermissionDenied
            amount = form.cleaned_data['amount']
            reason = form.cleaned_data['reason']
            note = "Message successfully sent"
            return render(request, 'emailgroup.html', {'form': form, 'note': note})
    else:
        form = EmailForm()
        return render(request, 'emailgroup.html', {'form': form})

def delete_group(request):
    if request.method == 'POST':
        form = DeleteForm(request.POST)
        if form.is_valid():
            group_name = form.cleaned_data['group_name']
            group = Group.objects.get(group_name=group_name)
            if group is None:
                raise ObjectDoesNotExist
            if not check_password_hash(group.password, form.cleaned_data['password']):
                print(group.password)
                raise PermissionDenied
            group.delete()
            note = "Group successfully deleted"
            return render(request, 'deletegroup.html', {'form': form, 'note': note})
    else:
        form = DeleteForm()
        return render(request, 'deletegroup.html', {'form': form})

def homepage(request):
    return render(request, 'homepage.html')