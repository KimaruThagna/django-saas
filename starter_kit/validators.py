import os
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension. Strictly upload .png files only')

def validate_file_shape(value):
    width,height=get_image_dimensions(value)
    if width!=240 and height!=1200:
        raise ValidationError(u'Unsupported file Shape. Strictly upload 240x1200 shaped images')