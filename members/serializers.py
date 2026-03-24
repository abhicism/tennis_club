from rest_framework import serializers
from .models import Member


class MemberSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # ✅ FIX

    class Meta:
        model = Member
        fields = '__all__'