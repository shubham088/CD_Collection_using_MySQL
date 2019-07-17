from django.forms import ModelForm
from myapp.models import CD


class AddCD(ModelForm):

    class Meta:
        model = CD
        fields = ['title', 'description', 'artist', 'date', 'genre']
