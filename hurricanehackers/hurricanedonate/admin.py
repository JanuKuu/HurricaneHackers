from django.contrib import admin

# Register your models here.
from .models import Question, Answer

admin.site.site_header = "Hurricane Hackers Admin"
admin.site.site_title = "Hurricane Hackers Admin Area"
admin.site.index_titel = "Welcome to the Hurricane Hackers admin area"

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']})]
    inlines = [AnswerInline]
# admin.site.register(Question)
# admin.site.register(Answer)

admin.site.register(Question, QuestionAdmin)