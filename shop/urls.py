from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .views import ProductsListView, basket_add, basket_delete

app_name = 'products'

urlpatterns = [
    # path('', Index.as_view(), name='index'),
    path('', ProductsListView, name='products_index'),
    path('category/<int:category_id>/', ProductsListView, name='products_filter'),
    path('page/<int:page>/', ProductsListView, name='page'),
    path('basket-add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket-delete/<int:basket_id>/', basket_delete, name='basket_delete')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# {% for product in object_list %}
#                 <div class="col-lg-4 col-md-6 mb-4">
#                     <div class="card h-100">
#                         <a href="#">
#                             <img class="card-img-top"
#                                  src="/media/{{ product.image }}"
#                                  alt="">
#                         </a>
#                         <div class="card-body">
#                             <h4 class="card-title">
#                                 <a href="#">{{ product.name }}</a>
#                             </h4>
#                             <h5>{{ product.price }} руб.</h5>
#                             <p class="card-text">{{ product.short_description }}</p>
#                         </div>
#                         <div class="card-footer text-center">
#                             <a href="{% url 'products:basket_add' product.id %}">
#                                 <button type="button" class="btn btn-outline-success">
#                                     Отправить в корзину
#                                 </button>
#                             </a>
#
#                         </div>
#                     </div>
#                 </div>
#                 {% endfor %}

# </div>
#                 {% if is_paginated %}
#                     <nav aria-label="Page navigation example">
#                         <ul class="pagination justify-content-center">
#                             <li class="page-item {% if not page_obj.has_previous %} disabled {% endif %}">
#                                 <a class="page-link"
#                                    href="{% if page_obj.has_previous %} {% url 'products:page' page_obj.previous_page_number %} {% else %} # {% endif %}"
#                                    tabindex="-1" aria-disabled="true">
#                                     Предыдущая
#                                 </a>
#                             </li>
#                             {% for page in paginator.page_range %}
#                                 <li class="page-item">
#                                     <a class="page-link" href="{% url 'products:page' page %}">
#                                         {{ page }}
#                                     </a>
#                                 </li>
#                             {% endfor %}
#                             <li class="page-item {% if not page_obj.has_next %} disabled {% endif %}">
#                                 <a class="page-link"
#                                    href="{% if page_obj.has_next %} {% url 'products:page' page_obj.next_page_number %} {% else %} # {% endif %}">
#                                     Следующая
#                                 </a>
#                             </li>
#                         </ul>
#                     </nav>
#
#                 {% endif %}
#         </div>

