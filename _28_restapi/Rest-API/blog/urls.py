from django.urls import path
from .views import PostView, SinglePostView

app_name = "blog"

urlpatterns = [
    path('blog/', PostView.as_view()),
    path('blog/<int:pk>', SinglePostView.as_view())
]