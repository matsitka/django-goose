from django import forms

from models import Article

#django test modal forms + crispy forms
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, Field, ButtonHolder, Submit



class ArticleForm(forms.ModelForm):

    created_at = forms.DateTimeField(widget=forms.HiddenInput(), required=False)
    url = forms.CharField(max_length=500, widget=forms.TextInput(attrs = {'label':'inputlink-label', 'class': 'inputlink', 'placeholder': 'http://example.com/article.html'}))



    class Meta:
        model = Article
        exclude = ('title', 'description', 'keywords', 'content', 'domain', 'original_image_url', 'favicon_url',
        'domain_link', 'movies', 'final_url', 'random')



    """
    @property
    def helper(self):
        helper = FormHelper()
        helper.form_tag = False # don't render form DOM element
        helper.render_unmentioned_fields = True # render all fields

        helper.layout = Layout (
            Field('url'),
            Field('folder', css_class="m-t-11"),
        )

        helper.label_class = 'col-md-2 inputlink-label'
        helper.field_class = 'col-md-10'
        return helper
    """



