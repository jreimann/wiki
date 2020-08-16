from django.shortcuts import render
from markdown2 import markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request,page):
    try:
        return render(request,"encyclopedia/entry.html", {
            "content": markdown(util.get_entry(page.upper())), "title": page.upper()
        })
    except:
        return render(request,"encyclopedia/entry.html", {
                "content": "No entry for {xpage} found.".format(xpage=page), "title": "404"
            })

