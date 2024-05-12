from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('list/grantgoal/', views.ListGrantGoal.as_view(), name = "list_gg"),
    path('new/grantgoal/', views.NewGrantGoal.as_view(), name = "new_gg"),
    path('detail/grantgoal/<int:pk>/', views.DetailGrantGoal.as_view(), name = "detail_gg"),
    path('update/grantgoal/<int:pk>/', views.UpdateGrantGoal.as_view(), name = "update_gg"),
    path('delete/grantgoal/<int:pk>/', views.DeleteGrantGoal.as_view(), name = "delete_gg")

    ]
