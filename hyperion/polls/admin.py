from django.contrib import admin
from polls.models import Question ,Choice

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text','votes')


admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice, ChoiceAdmin)

