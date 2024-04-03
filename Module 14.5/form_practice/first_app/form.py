from django import forms
from django.forms.widgets import NumberInput
from datetime import datetime
from .models import Student

# class contactForm(forms.Form):
#     name = forms.CharField(label="Enter your Name:")
#     email = forms.EmailField(label = "User Email")


class ExampleForm(forms.Form):
    name = forms.CharField(initial='Auny', max_length=20)
    comment = forms.CharField(widget=forms.Textarea,
                              required=False, help_text="Tell about yourself")
    email = forms.EmailField(
        label="Please enter your email address", initial='aunychowdhury@gmail.com')
    agree = forms.BooleanField(initial=True)
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))

    current_year = datetime.now().year
    BIRTH_YEAR_CHOICES = [str(year) for year in range(2020, current_year + 1)]
    birth_year = forms.DateField(
        widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))

    value = forms.DecimalField()

    day = forms.DateField(initial=datetime.now())

    FAVORITE_COLORS_CHOICES = [
        ('b', 'Blue'),
        ('g', 'Green'),
        ('bl', 'Black'),
    ]
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_color_radio = forms.ChoiceField(
        widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    favorite_colors_multi = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES,)

    GEEKS_CHOICES = (
        (1, "A"),
        (2, "B"),
        (3, "C"),
        (4, "D"),
        (5, "E"),
    )
    geeks_field = forms.TypedChoiceField(
        choices=GEEKS_CHOICES,
        coerce=str
    )

    geeks_field = forms.FileField() 
    geeks_field_url = forms.URLField( ) 



    
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        # labels = {
        #     'name' : 'Student Name',
        #     'roll' : "Student Roll"
        # }
        # widgets  = {
        #     'name' : forms.TextInput(),
        # }
        # help_texts = {
        #     'name' : "Write your full name"
        # }
        
        # error_messages = {
        #     'name' : {'required' : 'Your name is required'}
        # }

    
