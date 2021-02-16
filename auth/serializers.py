from rest_framework.serializers import Serializer, CharField, IntegerField


class UserSerializer(Serializer):
    id = IntegerField(read_only=True)
    username = CharField(max_length=150)
    first_name = CharField(max_length=150)
    last_name = CharField(max_length=150)
