from django import forms


g=[['MALE','Male'],['FEMALE','Female'],['OTHERS','Others']]
s=[['BANGALORE','Bangalore'],['HYDERABAD','Hyderabad'],['CHENNAI','Chennai'],['MYSORE','Mysore']]
c=[['PYTHON','Python'],['DJANGO','Django'],['SQL','sql']]

class Forms(forms.Form):
    Username=forms.CharField()
    Password=forms.CharField(widget=forms.PasswordInput)
    Confirm_Password=forms.CharField(widget=forms.PasswordInput)
    Email=forms.EmailField()
    # Gender=forms.ChoiceField(choices=g)
    Gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    # State=forms.ChoiceField(choices=s)
    State=forms.ChoiceField(choices=s,widget=forms.RadioSelect)

    Date_of_birth=forms.DateTimeField()
    # Coures=forms.MultipleChoiceField(choices=c)
    Coures=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)

    Address=forms.CharField(widget=forms.Textarea(attrs={'cols':22,'rows':4}))

    