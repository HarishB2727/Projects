from django.shortcuts import render, redirect
from django.http import HttpResponse

Data = [{'title': 'Holiday', 'text': 'Festival', 'contact': '7777999'},{'title': 'Holiday', 'text': 'Festival', 'contact': '7777999'},
{'title': 'Holiday', 'text': 'Festival', 'contact': '7777999'},{'title': 'Holiday', 'text': 'Festival', 'contact': '7777999'},
{'title': 'Holiday', 'text': 'Festival', 'contact': '7777999'},{'title': 'Holiday', 'text': 'Festival', 'contact': '7777999'},]

def show_board(request):
    context = {'data': Data}
    return render(request, 'NoticeBoard/Notice_board.html',context)

def Notice_board(request):
    dict_ ={}
    # temp = []
    title = request.POST.get('title')
    text = request.POST.get('text')
    contact = request.POST.get('contact_number')
    dict_['title'] = title
    dict_['text'] = text
    dict_['contact'] = contact
    Data.insert(0,dict_)
    Data.pop()
    # return HttpResponse("hi ra kanna")

    # context = {'title': title, 'text' : text, 'contact': contact}
    # return render(request, 'tic_tac_toe/board.html', context)
    # return HttpResponse(f"{Data}")
    return redirect('Notice:show_')

# Create your views here.
