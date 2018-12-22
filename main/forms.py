from django import forms

class ListingForm(forms.Form):
    name = forms.CharField(
        max_length=55,
        widget=forms.TextInput(attrs={'placeholder': 'Name'}),
    )
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={'placeholder': 'Email'}),
    )
    phone = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Phone number'}),
    )
    website = forms.URLField(
        max_length=254,
        widget=forms.URLInput(attrs={'placeholder': 'Website'}),
    )

    address = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'placeholder': 'Address', 'id': 'full-address'}),
    )

    latitude = forms.CharField(widget=forms.HiddenInput(), required=False)
    longitude = forms.CharField(widget=forms.HiddenInput(), required=False)

    city = forms.CharField(widget=forms.HiddenInput(), required=False)
    zip_code = forms.CharField(widget=forms.HiddenInput(), required=False)
    country = forms.CharField(widget=forms.HiddenInput(), required=False)
