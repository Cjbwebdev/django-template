from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ecom import views  
from ecom.views import user_logout
from ecom.forms import LoginForm
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='ecom/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', user_logout, name='logout'),
    path('cart/', views.cart_view, name='cart'),
    
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0]) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
