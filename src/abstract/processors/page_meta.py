from django.urls import resolve, reverse


def meta_processor(request):
    url_name = resolve(request.path).url_name
    if url_name == "boardlist_view":
        url_name = "Boards"
