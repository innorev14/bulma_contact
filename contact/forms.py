from django.forms import ModelForm, forms

from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    # def clean_content(self):
    #     phone = self.cleaned_data.get("phone_num")
    #     if phone != r'^[0-9]{2,4}[-\s\./0-9]*$':
    #         raise forms.ValidationError("잘못된 전화번호 입니다")
    #     return phone

    def clean(self):
        super(ContactForm, self).clean()
        phone = self.cleaned_data.get('phone_num')

        if phone != r'^[0-9]{2,4}[-\s\./0-9]*$':
            self._errors['phone_num'] = self.eror_class(["잘못된 전화번호 입니다"])
        return self.cleaned_data
