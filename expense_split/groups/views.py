from django.shortcuts import render
from .models import Group
from .forms import GroupForm, EmailForm, DeleteForm
from .tasks import send_email
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
                note = "Provide group name"
                return render(request, 'creategroup.html', {'form': form, 'note': note})
            if members is None:
                note = "Provide members"
                return render(request, 'creategroup.html', {'form': form, 'note': note})
            if password is None:
                note = "Provide password"
                return render(request, 'creategroup.html', {'form': form, 'note': note})
            allGroups = Group.objects.all()
            for group in allGroups:
                if group.group_name == group_name:
                    note = "Group exists. Use different group name"
                    return render(request, 'creategroup.html', {'form': form, 'note': note})
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
                note = "Group with name {} does not exist".format(group_name)
                return render(request, 'emailgroup.html', {'form': form, 'note': note})
            if not check_password_hash(group.password, form.cleaned_data['password']):
                note = "Incorrect password"
                return render(request, 'emailgroup.html', {'form': form, 'note': note})
            amount = form.cleaned_data['amount']
            reason = form.cleaned_data['reason']
            email_status = send_email(group.members, amount, reason)
            if email_status:
                note = "Message successfully sent"
            else:
                note = "Message not successfully sent"
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
                note = "Group with name {} does not exist".format(group_name)
                return render(request, 'deletegroup.html', {'form': form, 'note': note})
            if not check_password_hash(group.password, form.cleaned_data['password']):
                note = "Incorrect password"
                return render(request, 'deletegroup.html', {'form': form, 'note': note})
            for g in group:
                g.delete()
            note = "Group successfully deleted"
            return render(request, 'deletegroup.html', {'form': form, 'note': note})
    else:
        form = DeleteForm()
        return render(request, 'deletegroup.html', {'form': form})

def homepage(request):
    return render(request, 'homepage.html')