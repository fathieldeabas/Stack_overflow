from django import forms
class Search_form(forms.Form):
    choice1=[(True,True),(False,False),("","")]
    choice_order=[("asc","asc"),("desc","desc")]
    choice_sort=[("activity","activity"),("votes","votes"),("creation","creation"),("relevance","relevance")]

    
    page=forms.CharField(label="page",required=False)
    todate = forms.DateField(label='todate',required=False,widget=forms.TextInput(     
        attrs={'type': 'date'} 
    ))
    order=forms.ChoiceField(choices=choice_order,label="order",required=False)
    min = forms.DateField(label='min',required=False,widget=forms.TextInput(     
        attrs={'type': 'date'} 
    ))
    max=forms.DateField(label='max',required=False,widget=forms.TextInput(     
        attrs={'type': 'date'} 
    ))
    sort=forms.ChoiceField(choices=choice_sort ,label="sort",required=False)
    q=forms.CharField(label="q",required=False)
    accepted=forms.ChoiceField(choices=choice1,label="accepted",required=False)
    answers= forms.ChoiceField(choices=choice1, label="answers",required=False)
    body=forms.CharField(label="body",required=False)
    nottagged= forms.ChoiceField(label="nottagged",choices=choice1,required=False)
    closed=forms.ChoiceField(label="closed",choices=choice1,required=False)
    tagged= forms.ChoiceField(label="tagged",choices=choice1,required=False)
    title= forms.CharField(label="title",required=False)
    migrated=forms.ChoiceField(label="migrated",choices=choice1,required=False)
    user= forms.CharField(label="user",required=False)
    url= forms.CharField(label="url",required=False)
    notice=forms.ChoiceField(label="notice",choices=choice1,required=False)
    views= forms.CharField(label="views",required=False)
    wiki=forms.ChoiceField(label="wiki",choices=choice1,required=False)
    pagesize=forms.CharField(label="pagesize",required=False)
    fromdate=forms.DateField(label="fromdate",required=False,widget=forms.TextInput(     
        attrs={'type': 'date'} 
    ))
