from django.urls import path
from events import views

urlpatterns = [
    
    path('signup/',views.SigUpView.as_view()),
    
    path('signin/',views.SigninView.as_view(),name="signin"),
    
    path('eventsadd/',views.EventsaddView.as_view(),name="eventadd"),
    
    path('eventslist/',views.EventListView.as_view(),name="eventlist"),
    
    path('signout/',views.SignOutView.as_view(),name="signout")

]
