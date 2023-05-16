from django.urls import path
from . import views
from django.contrib.auth import views as authViews
from .forms import UserPasswordResetForm,UserPasswordchangeForm,changePassword
urlpatterns = [
    path('home/<str:pk>',views.home,name="home"),
    path('',views.my_index,name="my_index"),
    path('About/',views.about_us,name="about_us"),
    path('Contact/',views.contact_us,name="contact_us"),
    path('login/',views.login_page,name="login_page"),
    path('signup/',views.signUp,name="signup"),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('result/<str:pk>',views.result,name="result"),
    path('show_result/<str:pk>',views.show_result,name="show_result"),
    path('delet_item/<str:pk>',views.delet_item,name="delet_item"),
    path('user_profile/<str:pk>',views.user_profile,name="user_profile"),
    path('search_history/<str:pk>',views.search_history,name="search_history"),




    path('password_reset/', authViews.PasswordResetView.as_view(template_name="loginTemp/reset_password.html",form_class=UserPasswordResetForm), name='password_reset'),
    path('password_reset_done/', authViews.PasswordResetDoneView.as_view(template_name="loginTemp/check_email.html"), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(template_name="loginTemp/password_reset_confirm.html",form_class=UserPasswordchangeForm), name='password_reset_confirm'),
    path('password_reset_complete/', authViews.PasswordResetCompleteView.as_view(template_name="loginTemp/change_password_complete.html"), name='password_reset_complete'),
    path('password_change/', authViews.PasswordChangeView.as_view(template_name="loginTemp/user_change_password.html",form_class=changePassword,), name='password_change'),
    path('password_change_done/', authViews.PasswordChangeDoneView.as_view(template_name="loginTemp/change_password_done.html"), name='password_change_done'),
]