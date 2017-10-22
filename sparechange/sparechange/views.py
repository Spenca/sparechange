from .helpers import Render

@Render("index.html")
def index_view(request):
    context = {}
    return context