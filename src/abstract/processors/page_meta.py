from django.urls import resolve, reverse


def meta_processor(request):
    page_title = resolve(request.path).url_name
    if page_title == "boardlist_view":
        page_title = "Boards"
    return {
        "page_title": page_title,
    }
