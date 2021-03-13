from django.contrib import admin
from .models import Choice, BlogPost, BlogComment, Question, Project


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class CommentInLine(admin.TabularInline):
    model = BlogComment
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldset = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']})
    ]
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

class BlogAdmin(admin.ModelAdmin):
    inlines = [CommentInLine]



admin.site.register(Question, QuestionAdmin)


admin.site.register(Choice)
# Register your models here.
admin.site.register(BlogPost, BlogAdmin)
admin.site.register(BlogComment)
admin.site.register(Project)
