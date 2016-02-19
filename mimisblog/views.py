from django.shortcuts import render


def post_list(request):
    return render(request, 'mimisblog/post_list.html', {})
