# home/forms.py

from django import forms

class TicketBookingForm(forms.Form):
    """
    A simple form for booking tickets.
    """
    number_of_tickets = forms.IntegerField(
        min_value=1,
        max_value=10, # You can set a max limit for tickets per booking
        label="Number of Tickets",
        widget=forms.NumberInput(attrs={'class': 'form-control'}) # Bootstrap styling
    )
    email = forms.EmailField(
        label="Email Address",
        help_text="For booking confirmation",
        widget=forms.EmailInput(attrs={'class': 'form-control'}) # Bootstrap styling
    )
    # You could add a field for event selection later, e.g.:
    # event = forms.ChoiceField(
    #    choices=[('concert1', 'Concert A'), ('concert2', 'Concert B')],
    #    label="Select Event",
    #    widget=forms.Select(attrs={'class': 'form-control'})
    # )