from django.urls import path
from grantgoal import views

app_name = "gg"

urlpatterns = [
    path("client/list/grantgoal/", views.ListGrantGoalClient.as_view(), name = "client_list_gg"),
    path("client/detail/grantgoal/<int:pk>/", views.DetailGrantGoalClient.as_view(), name = "detail_list_gg"),
    path("client/create/grantgoal/", views.CreateGrantGoalClient.as_view(), name = "create_gg_cl"),


]
