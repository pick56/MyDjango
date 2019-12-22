from django.urls import path

from . import views

app_name = 'long_fakenews_detection'
'''
# ex: /polls/
path('', views.index, name='index'),
# ex: /polls/5/
path('<int:question_id>/', views.detail, name='detail'),
# ex: /polls/5/results/
path('<int:question_id>/results/', views.results, name='results'),
# ex: /polls/5/vote/
path('<int:question_id>/vote/', views.vote, name='vote'),
'''
urlpatterns = [
    # 这边是使用通用视图的代码
    path('', views.index, name='index'),
    path('check_txt/', views.check_txt, name='check_txt'),
    # path('detail/', views.detail, name='detail'),
    path('<int:txt_id>/', views.detail, name='detail'),

    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]