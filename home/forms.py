from django import forms

class TicketBookingForm(forms.Form):
    """
    A simple form for booking tickets, with name and contact details.
    """
    full_name = forms.CharField(
        max_length=100,
        label="Full Name",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    phone_number = forms.CharField(
        max_length=20,
        label="Phone Number",
        help_text="Include country code if outside the UK",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label="Email Address",
        help_text="For booking confirmation",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    number_of_tickets = forms.IntegerField(
        min_value=1,
        max_value=10,
        label="Number of Tickets",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
