from django.urls import path

from .views import about, logout_user, ContactFormView, FootballerHome, FootballerPosition, ShowPost, AddPage, \
    RegisterUser, LoginUser, FootballerClub, FootballerCountry

urlpatterns = [
    path('', FootballerHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('add_page/', AddPage.as_view(), name='add_page'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('position/<slug:position_slug>/', FootballerPosition.as_view(), name='position'),
    path('club/<slug:club_slug>/', FootballerClub.as_view(), name='club'),
    path('country/<slug:country_slug>/', FootballerCountry.as_view(), name='country')
]
