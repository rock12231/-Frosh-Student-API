from django.urls import path
from API.views import UserList
from rest_framework.urlpatterns import format_suffix_patterns



from API.views import (
    UserView,
    GetAuthUserView,
    ProfileView,
    ProfilesView,
    SingleProfileView,
    ExperienceView,
    EducationView,
    GitProfileView,
    PostView,
    LikeUnlikeView,
    CommentView
)



urlpatterns = [
    path('get', UserList.as_view()),

    path('users', UserView.as_view()),
    path('auth', GetAuthUserView.as_view()),

    path('posts', PostView.as_view()),
    path('posts/<int:id>', PostView.as_view()),
    path('posts/<int:id>/like', LikeUnlikeView.as_view()),
    path('posts/<int:id>/comments', CommentView.as_view()),
    path('posts/comments/<int:id>', CommentView.as_view()),

    path('profile', ProfileView.as_view()),
    path('profiles', ProfilesView.as_view()),
    path('profile/me', ProfileView.as_view()),
    path('profile/experience', ExperienceView.as_view()),
    path('profile/experience/<int:e_id>', ExperienceView.as_view()),
    path('profile/education', EducationView.as_view()),
    path('profile/education/<int:e_id>', EducationView.as_view()),
    path('profile/<int:id>', SingleProfileView.as_view()),

    path('github/<str:username>', GitProfileView.as_view())
    
    ]

urlpatterns = format_suffix_patterns(urlpatterns)