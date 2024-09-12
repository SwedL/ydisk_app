from django import forms


class LinkForm(forms.Form):
    """ Форма ввода публичной ссылки для просмотра файлов """

    city = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'введите публичную ссылку'}),
        label='link',
    )
