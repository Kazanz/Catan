from django import forms


class MapSettingsForm(forms.Form):
    VERSION_CHOICES = (
        ('original', 'Original'),
        ('seafarers', 'Seafarers'),
    )
    version = forms.ChoiceField(choices=VERSION_CHOICES)
    players = forms.IntegerField(min_value=3, max_value=6)
    board_size = forms.IntegerField(min_value=19)
