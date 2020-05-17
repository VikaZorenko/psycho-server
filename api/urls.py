from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^token-auth/?$', views.CustomAuthToken.as_view()),
    url(r'^register/?$', views.CreateUserView.as_view()),
    url(r'^tests/', include(([
        url(r'^$', views.TestsListApiView.as_view(), name='list'),
        url(r'^(?P<test_id>[-a-z0-9]+)/', include([
            url(r'^$', views.TestRetrieveApiView.as_view(), name='retrieve'),
            url(r'^start/?$', views.TestResultCreateApiView.as_view(), name='start'),
            url(r'^questions/', include(([
                url(r'^$', views.QuestionsListApiView.as_view(), name='list'),
                url(r'^(?P<question_id>[-a-z0-9]+)/', include([
                    url(r'^$', views.QuestionRetrieveApiView.as_view(), name='retrieve'),
                ]))
            ], 'questions'), namespace='questions'), name='questions'),
            url(r'^results/', include(([
                url(r'^$', views.TestResultsListApiView.as_view(), name='list'),
                url(r'^(?P<result_id>[-a-z0-9]+)/', include([
                    url(r'^$', views.TestResultRetrieveApiView.as_view(), name='retrieve'),
                    url(r'^next-question/?$', views.NextQuestionRetrieveApiView.as_view(), name='next-question'),
                    url(r'^answer/?$', views.QuestionResultCreateApiView.as_view(), name='answer'),
                ]))
            ], 'results'), namespace='results'), name='results'),
        ]))
    ], 'tests'), namespace='tests'), name='tests'),
]