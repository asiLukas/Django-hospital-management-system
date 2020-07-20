from django.urls import path
from .views import case_list_view, case_create_view, case_index_view, case_delete_view, case_update_view, \
    patient_create_view, patient_list_view, patient_index_view, patient_delete_view, patient_update_view

app_name = 'cases'

urlpatterns = [
    path('list/', case_list_view),
    path('create/', case_create_view),
    path('<int:id>', case_index_view, name='detail'),
    path('<int:id>/delete/', case_delete_view),
    path('<int:id>/update/', case_update_view),

    path('patient/create/', patient_create_view),
    path('patient/list/', patient_list_view),
    path('patient/<int:id>', patient_index_view, name='patient_detail'),
    path('patient/<int:id>/delete/', patient_delete_view),
    path('patient/<int:id>/update/', patient_update_view)
]
