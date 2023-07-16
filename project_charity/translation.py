from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(About_us_mainpaig)
class About_us_mainpaigTranslation(TranslationOptions):
    fields = ('text',)


@register(HelpCase)
class HelpCaseTranslation(TranslationOptions):
    fields = ('title', 'description_title', 'description_full', 'address')