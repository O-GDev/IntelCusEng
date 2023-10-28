
from django.contrib import admin
from django.urls import path, include
from .views import MainView
from . import views
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="",
        default_version="1.0.0",
        description="API Documentation",
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),                              
    path('/preferred-response', MainView.as_view(), name='main'),             
    path('home/', views.admin_dashboard, name='admin_dashboard'),             
    path('admin-login/', views.admin_login, name='admin_login'),
    path('logout/', views.signout_view, name="logout"),
    # path(''),
    path('api/v1/',
         include([
            #  path('post', include(('post.api.urls', 'post'), namespace='posts')),
             path('swagger/schemas/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema")
         ])
         )
]
