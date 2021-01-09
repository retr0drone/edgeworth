from django.contrib.auth import get_user_model
from rest_framework import serializers
from . models import Claims, Comments

User = get_user_model()


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ('id', 'username',)
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ('id', 'username',)
        fields = '__all__'


class ClaimsSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedIdentityField(many=False, view_name='owner-detail') #view_name == url name in urls.py
    comments = serializers.HyperlinkedRelatedField(queryset=Comments.objects.all(), many=True, view_name='comments-detail') #view_name == url name in urls.py
    
    class Meta:
        model = Claims
        fields = ('user', 'title', 'description', 'debt_currency',
                    'debt_amount', 'debtor_name', 'debtor_email',
                    'debtor_phone', 'debtor_location', 'support_files', 'comments',
        )