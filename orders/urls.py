from django.urls import path
from orders import views


urlpatterns =[
    
    path('', views.CreateOrderListView.as_view(), name= 'orders'),
    path('<int:order_id>/', views.OrderDetailsView.as_view(), name='order_detail'),
    path('update_status/<int:order_id>/', views.UpdateOrderStatusView.as_view(), name='update_orderstatus'),
    path('user/<int:user_id>/orders/', views.UserOrdersView.as_view() , name ='users_orders'),
    path('user/<int:user_id>/order/<int:order_id>', views.UserOrderDetailView.as_view(), name= 'user_specific_detail')
]