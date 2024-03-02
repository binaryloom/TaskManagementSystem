from django.urls import resolve, reverse


def meta_processor(request):
    """
    Generate meta information for the current page based on the URL resolver.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        dict: A dictionary containing meta information for the current page with keys:
            - 'page_title' (str): The title of the current page.
    """
    page_title = resolve(request.path).url_name
    if page_title == "dashboard_view":
        page_title = "Dashboard"
    if page_title == "boardlist_view":
        page_title = "Boards"
    if page_title == "boarddetail_view":
        page_title = "Board Details"
    if page_title == "listlist_view":
        page_title = "Lists"
    if page_title == "listdetail_view":
        page_title = "List Details"
    if page_title == "tasklist_view":
        page_title = "Tasks"

    if page_title == "login_view":
        page_title = "LOGIN"
    return {
        "page_title": page_title,
    }
