from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from Note_app.Api.views import (CreateNoteView,  FetchNotesbyIDView, 
                                SearchQueryNotesView, UpdateNoteView)

schema_view = get_schema_view(
    openapi.Info(
        title="Note_Taking Api",
        default_version='Version V1',
        description="API for a simple note-taking application",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@notes.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('Api/', CreateNoteView.as_view(), name='Creating-Note'),
    path('Api/<int:pk>/', FetchNotesbyIDView.as_view(), name='Fetching-Note'),
    path('Api/search/', SearchQueryNotesView.as_view(), name='Search_by_Query'),
    path('Api/update/<int:pk>/', UpdateNoteView.as_view(), name='Updating-Note'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
