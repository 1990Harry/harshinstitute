from django import forms
class ContactForm(forms.Form):
    firstname=forms.CharField(
        label='Enter Your First Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your Name'
            }
        )
    )
    lastname=forms.CharField(
        label='Enter Your Last Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your Last Name'
            }
        )
    )
    email=forms.CharField(
        label='Enter Your Email-ID',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your Email'
            }
        )
    )
    mobile=forms.CharField(
        label='Enter Your Mobile Number',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your Mobile Number'
            }
        )
    )
    course=forms.CharField(
        label='Enter Course Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your Name'
            }
        )
    )
class FeedbackForm(forms.Form):
    name=forms.CharField(
        label='Enter Your Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your Name'
            }
        )
    )
    rating=forms.CharField(
        label='Enter Your Rating',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter only Digits'
            }
        )
    )
    feedback=forms.CharField(
        label='Enter your Feedback',
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your Feedback'
            }
        )
    )