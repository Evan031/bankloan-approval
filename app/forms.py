from django import forms


class ApprovalForm(forms.Form):
    gender = forms.ChoiceField(
        choices=[(1, 'Male'), (0, 'Female')])
    married = forms.ChoiceField(choices=[(1, 'Yes'), (0, 'No')])
    dependents = forms.IntegerField(widget=forms.NumberInput(
        attrs={'placeholder': 'Enter Number of Dependents'}))
    education = forms.ChoiceField(
        choices=[(1, 'Graduate'), (0, 'Not Graduate')])
    self_employed = forms.ChoiceField(choices=[(1, 'Yes'), (0, 'No')])
    applicant_income = forms.IntegerField(widget=forms.NumberInput(
        attrs={'placeholder': 'Enter Monthly Gross Income'}))
    coapplicant_income = forms.IntegerField(widget=forms.NumberInput(
        attrs={'placeholder': 'Enter Co-Applicant Monthly Gross Income'}))
    loan_amount = forms.IntegerField(widget=forms.NumberInput(
        attrs={'placeholder': 'Requested Loan Amount'}))
    loan_amount_term = forms.IntegerField(widget=forms.NumberInput(
        attrs={'placeholder': 'Loan Term in Months'}))
    credit_history = forms.ChoiceField(
        choices=[('0', 0), ('1', 1), ('2', 2), ('3', 3)])
    property_area = forms.ChoiceField(
        choices=[(0, 'Rural'), (1, 'Semiurban'), (2, 'Urban')])
