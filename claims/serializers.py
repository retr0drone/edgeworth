from rest_framework import serializers
from . models import Claims, Comments


class ClaimsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Claims
        fields = ('title','description','debt_currency',
                    'debt_amount', 'debtor_name', 'debtor_email',
                    'debtor_phone', 'debtor_location','support_files',
        )