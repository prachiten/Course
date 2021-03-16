from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('addcourse',views.add_course),
    path('remove/<int:course_id>', views.show_delete_page),
    path('remove/<int:remove_id>/delete',views.remove),
    path('comment/<int:course_id>',views.display_comments),
    path('comment/<int:course_id>/add',views.add_comments),
]
