from django import forms

from .models import New


class NewForm(forms.ModelForm):

    class Meta:
        model= New
        fields = ('title','subtitle','body','image')

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if not isinstance(image, str):
            if image.name.endswith('.jpg') or image.name.endswith('.png'):
                if image.size > 10*1024*1024:
                    self.add_error(('image', "Image file too large (>10MB"))

                return image
            else:
                self.add_error('image', "Couldn't read uploaded image, due to image format")

