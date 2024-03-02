def breadcrumb(request):
    """
    Generate breadcrumb navigation based on the current URL path.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        dict: A dictionary containing the breadcrumb navigation data with keys:
            - 'breadcrumb' (list): A list of dictionaries, each representing a breadcrumb item. Each dictionary contains two keys:
                - 'title' (str): The title of the breadcrumb item.
                - 'link' (str): The URL link of the breadcrumb item.
    """
    breadcrumb = [{"title": "Home", "link": "/"}]
    if current_link := request.path[1:]:
        current_link = current_link[:-1] if current_link[-1] == "/" else current_link
        link_segments = "/"
        for fragment in current_link.split("/"):
            breadcrumb.append(
                {"title": fragment, "link": link_segments + str(fragment)}
            )
            link_segments += f"{str(fragment)}/"

    return {"breadcrumb": breadcrumb}
