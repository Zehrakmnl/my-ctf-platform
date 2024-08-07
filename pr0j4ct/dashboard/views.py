from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from item.models import Item
from django.contrib.auth.decorators import login_required
from .models import UserScore

def pointGet(request):
    # return JsonResponse({'status': 'error', 'message':request.GET.get('nokta',0) } )
    if request.user.is_authenticated:
        myanswer = request.GET.get('point', 0) # answer ve point kullanımı aynı hatayı verdi
        total = request.session.get('total', 0)
        puan = request.GET.get('price',0) 
        
        Itemname = request.GET.get('name',0)
        items = Item.objects.filter(name=Itemname)
        # item = items.first()
        # correctAnswer = item.correctAnsw
        if items.exists():  # Check if any items exist in the queryset
            item = items.first()  # Get the first item in the queryset
            if item is not None:  # Check if item is not None
                correctAnswer = item.correctAnsw  # Access the attribute on the item
                if myanswer==correctAnswer:
                    total=int(total)+int(puan)
                    request.session['total'] = total

                    user_score, created = UserScore.objects.get_or_create(user=request.user)
                    user_score.total_points = total
                    user_score.save()
            else:
                return JsonResponse({'error': 'Item found but has no attributes'}, status=500)
    else:
        return JsonResponse({'error': 'Item not found'}, status=404)
        # return JsonResponse({'answerimzeh': myanswer, 'totalimiz':total, 'reqnamemimiz': puan, 'itmname': Itemname, 'correctAnswerimiz':correctAnswer } )
    username = request.user.username if request.user.is_authenticated else "Guest"
    context = {
        'username': username,
        'total': total,
    }
    return render(request, 'dashboard/index.html', context)
    

def score_table(request):
    if request.user.is_authenticated:
        total_points = request.session.get('total', 0)
        
        user_score, created = UserScore.objects.get_or_create(user=request.user)
        user_score.total_points = total_points
        user_score.save()
        
        user_data = UserScore.objects.all()
        
        if not user_data:
            print("No user data found.")
        else:
            for score in user_data:
                print(f'User: {score.user.username}, Total Points: {score.total_points}')
        
        context = {
            'user_data': user_data,
        }
        print("Context data being passed to template:", context)  # Debugging output
        return render(request, 'dashboard/index.html', context)
    else:
        return render(request, 'dashboard/index.html')

 
# ###########

        # Itemname = request.GET.get('name',0)
        # items = Item.objects.filter(name=Itemname)
        # item = items.first()  
        # item.is_sold=True
        # burada doğru cevap verildiğinde sorunun görünmemesini ayarlamak istiyorum. ama olmuyor?

  ################

# @login_required
# def index(request):
#     items = Item.objects.filter(created_by=request.user)

#     return render(request, 'dashboard/index.html',{
#         'items':items,
#     })

# def score_table(request):
#     if request.user.is_authenticated:
        
#         total_points = request.session.get('total', 0)

#         user_score= UserScore.objects.get_or_create(user=request.user)
#         user_score.total_points = total_points
#         user_score.save()

#         user_data = UserScore.objects.all()
        
#         context = {
#             'user_data': user_data,
#         }
#         # return render(request, 'dashboard/score_table.html', context)
#     else:
#         return render(request, 'dashboard/index.html')