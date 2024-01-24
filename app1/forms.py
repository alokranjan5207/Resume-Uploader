from django import forms
from .models import Resume

#choices
Gender_Choices=[
    ('Male','Male'),
    ('Female','Female')
]

Job_City=[('Bangalore','Bangalore'),
          ('Chenai','Chenai'),
            ('Hyderabad','Hyderabad'),
            ('Noida','Noida'),
            ('Pune','Pune'),
          ]

class ResumeForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=Gender_Choices, widget=forms.RadioSelect)

    job_city=forms.MultipleChoiceField(label='Prefer Job Locations',choices=Job_City,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model=Resume
        fields=['id','name','dob','gender','city','pin','state','mobile','email','job_city','profile_image','my_file']

        labels={'name':'Full Name', 'dob':'Date of Birth','pin':'Pin Code','mobile':'Mobile No','Profile_image':'Profile Image','my_file':'Document','email':'Email ID'} #ye dikhega

        #widgets use for apply bootstrap
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control','ID':'datepicker'}),                        
            'city':forms.TextInput(attrs={'class':'form-control'}),            
            'pin':forms.NumberInput(attrs={'class':'form-control'}),            
            'state':forms.Select(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
           

        }