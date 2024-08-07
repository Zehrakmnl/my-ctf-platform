from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.http import StreamingHttpResponse, Http404, FileResponse

from .models import Item, Category, Point
from .forms import NewItemForm, EditItemForm
from wsgiref.util import FileWrapper
import mimetypes
import os



def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category',0   )
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:  
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'item/items.html', {
        'items':items,
        'query':query,
        'categories':categories,
        'category_id':int(category_id)
    })

def downloadfile(request, pk):
    dwnldfile = request.GET.get('file', '')
    cheatsheet = get_object_or_404(Item, pk=pk)
    if not cheatsheet.file:
        raise Http404("File not found")
    file_path = cheatsheet.file.path
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = f'attachment; filename="{cheatsheet.name}"'
    return response

    # base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # filename = request.GET.get('file', '')  # Using 'file' parameter from the query string

    # if not filename:
    #     raise Http404("File parameter not provided")

    # filepath = os.path.join(base_dir, 'file', filename)
    
    # if not os.path.exists(filepath):
    #     raise Http404("File not found")

    # thefile = filepath
    # filename = os.path.basename(thefile)
    # chunk_size = 8192
    # response = StreamingHttpResponse(FileWrapper(open(thefile, 'rb'), chunk_size), content_type=mimetypes.guess_type(thefile)[0])
    # response['Content-Length'] = os.path.getsize(thefile)
    # response['Content-Disposition'] = f'attachment; filename="{filename}"'
    # return response

# def pointGet(request):
    
#     point = int(request.GET.get('point', 0))
#     username = request.user.username if request.user.is_authenticated else "Guest"
#     total += point

#     context = {
#         'username': username,
#         'total': total,
#     }
#     return render(request, 'dashboard/index.html', context)

    # point = request.GET.get('point', '')


    # if point:  
    #     items = items.filter(Q(name__icontains=point) | Q(description__icontains=point))

    # return render(request, 'item/items.html', {
    #     'point':point,
    # })

    # new_point = Point(x=3.14, y=2.71)

    # new_point.save()
    
    # all_points = Point.objects.all()

    # for point in all_points:
    #     print(point)


def detail(request, pk ):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html', {
        'item':item,
        'related_items':related_items
    })



@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit = False)
            item.created_by = request.user
            item.save()
 
            return redirect('item:detail', pk=item.id)
        
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form':form, 
        'title': 'New Item',
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user) 
    item.delete()

    return redirect('dashboard:index' ) 

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user) 

    if request.method == 'POST':

        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()
 
            return redirect('item:detail', pk=item.id)
        
    else: 
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form':form, 
        'title': 'Edit Item',
    })