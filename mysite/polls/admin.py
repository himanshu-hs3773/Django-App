from django.contrib import admin

from .models import Question, Choice				# . means same directory

admin.site.register(Question)						# adds Question class to GUI

admin.site.register(Choice)