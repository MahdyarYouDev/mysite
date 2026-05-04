from django.http import HttpResponse

def testHttp(request):
    return HttpResponse("you are in first view's page")