from django.shortcuts import render
from .models import Group
from .forms import GroupForm
# Create your views here.

def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group_name = form.cleaned_data['group_name']
            members = form.cleaned_data['members']
            if group_name is None or members is None:
                return 
            group = Group()
            group.group_name = group_name
            group.members = members
            group.save()
            note = "Group successfully created"
            return render(request, 'creategroup.html', {'form': form, 'note': note})
    else:
        form = GroupForm()
        return render(request, 'creategroup.html', {'form': form})