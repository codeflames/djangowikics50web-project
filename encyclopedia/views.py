from django.shortcuts import render
import markdown2

from . import util


def index(request):
    if request = POST:
        # search first for the search query else:
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def detailpage(request, title):
    entry_title = util.get_entry(title)
    if entry_title is None:
        return render(request, 'encyclopedia/error_page.html')
    entries = markdown2.markdown(entry_title)
    
    return render(request, 'encyclopedia/entry_detail.html', {'entries': entries})

# def errorpage(request):
#     return render(request, 'encyclopedia/error_page.html')