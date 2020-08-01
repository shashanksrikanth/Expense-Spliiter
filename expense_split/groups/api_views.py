from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.exceptions import ValidationError
from .models import Group
from .serializers import GroupSerializer

class GroupList(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupCreate(CreateAPIView):
    serializer_class = GroupSerializer
    def create(self, request, *args, **kwargs):
        try:
            group_name = request.data.get('group_name')
            if group_name is None:
                raise ValidationError({'group_name': 'Group name cannot be empty'})
            members = request.data.get('members')
            if members is None:
                raise ValidationError({'members': 'Members cannot be 0'})
        except Exception as e:
            print(e)
        return super().create(request, *args, **kwargs)  