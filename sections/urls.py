from django.urls import path
from sections.apps import SectionsConfig
from sections.views import SectionListAPIView, SectionCreateApiView, SectionRetrieveAPIView, SectionUpdateAPIView, \
    SectionDestroyAPIView, ContentListAPIView, ContentCreateApiView, ContentRetrieveAPIView, ContentUpdateAPIView, \
    ContentDestroyAPIView

app_name = SectionsConfig.name

urlpatterns = [
    # Section urlpatterns
    path('', SectionListAPIView.as_view(), name='sections_list'),
    path('create/', SectionCreateApiView.as_view(), name='section_create'),
    path('<int:pk>/', SectionRetrieveAPIView.as_view(), name='section_detail'),
    path('<int:pk>/update/', SectionUpdateAPIView.as_view(), name='section_update'),
    path('<int:pk>/delete/', SectionDestroyAPIView.as_view(), name='section_delete'),

    # Content urlpatterns
    path('content/', ContentListAPIView.as_view(), name='content_list'),
    path('content/create/', ContentCreateApiView.as_view(), name='content_create'),
    path('content/<int:pk>/', ContentRetrieveAPIView.as_view(), name='content_detail'),
    path('content/<int:pk>/update/', ContentUpdateAPIView.as_view(), name='content_update'),
    path('content/<int:pk>/delete/', ContentDestroyAPIView.as_view(), name='content_delete'),

]
