from django.shortcuts import render

from django.views.generic import View
from books.models import Books
from json import loads
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt,name="dispatch")
class BookCreateListView(View):
    def get(self,request):
        qs=Books.objects.all().values()
        all_emp=list(qs)
        return JsonResponse(all_emp,safe=False)

    def post(self,request):
        form_data=loads(request.body)
        Books.objects.create(
                                title=form_data.get("title"),
                                auther=form_data.get("auther"),
                                price=form_data.get("price"),
                                pages=form_data.get("pages"),
                                publication=form_data.get("publication")
                            )
        return JsonResponse({"Message":"Record Created ..."})

@method_decorator(csrf_exempt,name="dispatch")
class BookRetriveUpdateDeleteView(View):
    def get(self,request,pk=None):
        qs=Books.objects.filter(id=pk).values()
        emp_list=list(qs)

        return JsonResponse(emp_list,safe=False)
    
    def delete(self,request,pk=None):
        Books.objects.filter(id=pk).delete()
        return JsonResponse({"message":"Record Deleted ..."},safe=False)

    