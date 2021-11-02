django-CustomSelectWidget
=======================

This is a custom Select Widget for django forms and modelforms. This widget will enable you to have a select field in HTML that can take free text value along with a limited
select options. the selectable option can be selected by user or if need be, the user can type their own free text in the field. This widget works with django.forms.CharField.ChildProcessError



Supported Python versions:  3.4+

Supported Django versions: 2.0+

Installation
============


Install with pip
----------------

.. code-block:: bash

    $ pip install django-CustomSelectWidget

Configure your models.py or forms.py
-------------------------------------

.. code-block:: python

    from django.forms.models import ModelForm
    from customselectwidget import CustomSelectWidget
    from django import forms

    # ...

    
    class MyModelForm(ModelForm):

        # .....
        my_field=forms.CharField(required=False,max_length=200, label='Please select your task')
        def __init__(self, *args, **kwargs):
            _type_list = kwargs.pop('data_list', None)
            super(MyModelForm, self).__init__(*args, **kwargs)
            # the "name" parameter will allow you to use the same widget more than once in the same
            # form, not setting this parameter differently will cuse all inputs display the
            # same list.
            self.fields['my_field'].widget = CustomSelectWidget(data_list=['option 1','option 2','option 3'], name='type-list')
    


In your settings.py
-------------------



.. code-block:: python

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.admin',

        #.....................#

        'customselectwidget',
    )



