from collections.abc import Mapping
from typing import Any
from django.contrib.auth.models import User
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms.utils import ErrorList

class userform(ModelForm):
    def __init__(self, data: Mapping[str, Any] | None = ..., files: Mapping[str, File] | None = ..., auto_id: bool | str = ..., prefix: str | None = ..., initial: dict[str, Any] | None = ..., error_class: type[ErrorList] = ..., label_suffix: str | None = ..., empty_permitted: bool = ..., instance: Model | None = ..., use_required_attribute: bool | None = ..., renderer: Any = ...):
        super().__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, instance, use_required_attribute, renderer)
        self.fields['username'].widget.attrs.update({
            'type':"text",
            'required':'',
            
        })
        self.fields['password1'].widget.attrs.update({
            'type':"password",
            'required':""
            
        })
    
    class Meta:
        model=User
        fields='__all__'