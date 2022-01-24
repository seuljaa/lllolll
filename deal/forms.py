from django import forms
from .models import DealItems,Group

from django_summernote.widgets import SummernoteWidget



class PostForm(forms.ModelForm):
    class Meta:
        model = DealItems
        fields = ['content']
        widgets = {
            'content': SummernoteWidget(),
        }
        labels = {
            'content': '내용'
        }

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['kind', 'part_armor', 'part_accessory', 'part_weapon', 'star_force', 'ability_1', 'ability_2']

        labels = {
            'kind':'종류',
            'part_armor':'방어구',
            'part_accessory':'장신구',
            'part_weapon':'무기',
            'star_force':'스타포스',
            'ability_1':'윗잠',
            'ability_2':'아랫잠'
        }