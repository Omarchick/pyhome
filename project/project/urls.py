from django.urls import path, include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('entities/', views.entity_list, name='entity_list'),
    path('entities/<int:pk>/', views.entity_detail, name='entity_detail'),
    path('entities/new/', views.entity_create, name='entity_create'),
    path('entities/<int:pk>/edit/', views.entity_edit, name='entity_edit'),
    path('entities/<int:pk>/delete/', views.entity_delete, name='entity_delete'),
    path('analytics/', views.analytics, name='analytics'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.register, name='register'),
]
