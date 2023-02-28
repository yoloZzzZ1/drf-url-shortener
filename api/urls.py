from .spectacular.urls import urlpatterns as doc_urls
from tokens.urls import urlpatterns as token_urls

app_name = 'api'

urlpatterns = [
    
]

urlpatterns += doc_urls
urlpatterns += token_urls