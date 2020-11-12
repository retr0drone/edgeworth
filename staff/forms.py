from django import forms
from claims.models import Claims


class ClaimsCreateForm(forms.ModelForm):
    class Meta:
        model = Claims
        fields = [ 'user','title','description','debt_currency',
                    'debt_amount', 'debtor_name', 'debtor_email',
                    'debtor_phone', 'debtor_location','support_files',
        ]