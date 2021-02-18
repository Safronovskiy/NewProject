from django.shortcuts import render
from .models import *
from django.views.generic import ListView
from django.shortcuts import get_object_or_404



# -----------------------Function-Based views------------------------------
def startpage_shop(request):
    categories = CategoryModel.objects.all()
    clothes = WearModel.objects.all()

    context = {'cats':categories, 'clothes':clothes}
    return render(request, 'shop_app/shop_startpage.html', context=context)


def cat_sort(request, pk):
    categories = CategoryModel.objects.all()
    clothes = WearModel.objects.filter(category=pk)

    return render(request, 'shop_app/cat_sorted.html', {'clothes':clothes,'cats':categories,
                                                        })


def details(request, pk):
    info = get_object_or_404(WearModel, pk=pk)
    return render(request, 'shop_app/details.html', {'info':info})

# --------------------------Class_based_views ------------------------------

# class AllItemsView(ListView):
#     model = WearModel
#     context_object_name = 'clothes'
#     template_name = 'shop_app/shop_startpage.html'
#     paginate_by = 8
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super(AllItemsView, self).get_context_data(**kwargs)
#         context['cats'] = CategoryModel.objects.all()[:9]
#         return context






