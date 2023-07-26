from modeltranslation.translator import register, TranslationOptions
from .models import *



@register(Slider)
class Slider1Translation(TranslationOptions):
    fields = ('text', 'low_text')

@register(Desc)
class DescTranslation(TranslationOptions):
    fields = ('text', 'low_text', 'inner_text')

@register(About_page_text)
class About_page_textTranslation(TranslationOptions):
    fields = ('text',)


@register(About_us_mainpaig)
class About_us_mainpaigTranslation(TranslationOptions):
    fields = ('text',)


@register(HelpCase)
class HelpCaseTranslation(TranslationOptions):
    fields = ('title', 'description_title', 'description_full', 'address')