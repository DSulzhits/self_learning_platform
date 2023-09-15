from django.urls import path
from rest_framework.routers import DefaultRouter
from sections.apps import SectionsConfig
from sections.views import SectionListAPIView, SectionCreateApiView, SectionRetrieveAPIView, SectionUpdateAPIView, \
    SectionDestroyAPIView, ContentListAPIView, ContentCreateApiView, ContentRetrieveAPIView, ContentUpdateAPIView, \
    ContentDestroyAPIView, TestsListAPIView, TestQuestionAPIView
from django.views.decorators.cache import never_cache

app_name = SectionsConfig.name

router = DefaultRouter()

urlpatterns = [
    # Section urlpatterns
    path('section/', SectionListAPIView.as_view(), name='sections_list'),
    path('section/create/', never_cache(SectionCreateApiView.as_view()), name='section_create'),
    path('section/<int:pk>/', SectionRetrieveAPIView.as_view(), name='section_detail'),
    path('section/<int:pk>/update/', never_cache(SectionUpdateAPIView.as_view()), name='section_update'),
    path('section/<int:pk>/delete/', never_cache(SectionDestroyAPIView.as_view()), name='section_delete'),

    # Content urlpatterns
    path('content/', ContentListAPIView.as_view(), name='content_list'),
    path('content/create/', never_cache(ContentCreateApiView.as_view()), name='content_create'),
    path('content/<int:pk>/', ContentRetrieveAPIView.as_view(), name='content_detail'),
    path('content/<int:pk>/update/', never_cache(ContentUpdateAPIView.as_view()), name='content_update'),
    path('content/<int:pk>/delete/', never_cache(ContentDestroyAPIView.as_view()), name='content_delete'),

    # Tests urlpatterns
    path('tests/', TestsListAPIView.as_view(), name='tests_list'),
    path('tests/test/', TestQuestionAPIView.as_view(), name='test'),
] + router.urls
