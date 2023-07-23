from django.urls import path

from playground.web.views import UserRegistrationView, UserLoginView, FieldListView, FieldUpdateView, \
    FieldDeleteView, LogoutView, first_page, FieldView

urlpatterns =[
    path('', first_page, name='first_page'),
    path('registration/', UserRegistrationView.as_view(), name='register-user'),
    path('login/', UserLoginView.as_view(), name='login' ),
    path('fields/', FieldListView.as_view(), name='fields'),
    # path('field-detail/', FieldView.as_view(), name='field-detail'),
    # path('fields/create/', FieldCreateView.as_view(), name='add-field'),
    path('fields/update/<int:pk>/', FieldUpdateView.as_view(), name='edit-field'),
    path('fields/delete/<int:pk>/', FieldDeleteView.as_view(), name='delete-field'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

# Play1235

