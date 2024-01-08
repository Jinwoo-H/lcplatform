from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Question
# from django.contrib.postgres.fields import ArrayField

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'mt-3 block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500', 'placeholder': 'Email Address'}))
	name = forms.CharField(label="", max_length='100', widget=forms.TextInput(attrs={'class': 'mt-3 block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500', 'placeholder': 'Name'}))
	class Meta:
		model = User
		fields = ('username', 'name', 'email', 'password1', 'password2')
	
	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'mt-3 block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small>'

		self.fields['password1'].widget.attrs['class'] = 'mt-3 block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<small>Your password can\'t be too similar to your other personal information.</small><br/><small>Your password must contain at least 8 characters.</small><br/><small>Your password can\'t be a commonly used password.</small><br/><small>Your password can\'t be entirely numeric.</small>'

		self.fields['password2'].widget.attrs['class'] = 'mt-3 block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


class AddQuestionForm(forms.ModelForm):
	favorite = forms.BooleanField(required=False, widget=forms.widgets.CheckboxInput(attrs={"class": "mt-3 p-2.5 text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500"}),label="Favorite")
	question_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Question Name", "class": "mt-3 block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500"}),label="")
	link = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Question Link", "class": "mt-3 block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500"}),label="")
	notes = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={"placeholder": "Notes", "class": "mt-3 block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500"}),label="")
	# topics = ArrayField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Topics", "class": "mt-3 block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500"}),label="")
	# difficulty = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Difficulty", "class": "mt-3 block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500"}),label="")
	# belongs_to = forms.HiddenInput(widget=forms.widgets.HiddenInput())
	class Meta:
		model = Question
		# exclude = ("user",)
		fields = ('favorite','question_name', 'link', 'notes')