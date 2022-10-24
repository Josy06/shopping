from . models import Categoery#category part5

def menu_links(request):
    links=Categoery.objects.all()
    return dict(links=links)