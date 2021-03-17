from django import forms


class ApprovalForm(forms.Form):
    first_name = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={'placeholder': 'Enter Firstname'}))
    last_name = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={'placeholder': 'Enter Lastname'}))
    dependents = forms.IntegerField(widget=forms.NumberInput(
        attrs={'placeholder': 'Enter Number of Dependents'}))
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
    gender = forms.ChoiceField(
        choices=[('Male', 'Male'), ('Female', 'Female')])
    married = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')])
    education = forms.ChoiceField(
        choices=[('Graduate', 'Graduate'), ('Not_Graduate', 'Not_Graduate')])
    self_employed = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')])
    property_area = forms.ChoiceField(
        choices=[('Rural', 'Rural'), ('Semiurban', 'Semiurban'), ('Urban', 'Urban')])
