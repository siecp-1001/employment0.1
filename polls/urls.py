from django.urls import path
from .views import polls_list,polls_detail
from .apiviews import PollList, PollDetail,Choicelist,Createvote,UserCreate,LoginView
from rest_framework.routers import DefaultRouter
from .apiviews import PollViewSet
router= DefaultRouter()
router.register('polls',PollViewSet,basename='polls')
urlpatterns = [
    path("polls/", PollList.as_view(),name="polls_list"),
    path("polls/<pk>",PollDetail.as_view(),name="polls_detail"),
    path("login/", LoginView.as_view(), name="login"),
    path("users/", UserCreate.as_view(), name="user_create"),
    path("choices/",Choicelist.as_view(),name="choice_list"),
    path("vote/",Createvote.as_view(),name="create_vote"),
    path("polls/<int:pk>/choices",Choicelist.as_view(),name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/",Createvote.as_view(),name="create_vote"),
]

urlpatterns += router.urls