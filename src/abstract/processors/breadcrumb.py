def breadcrumb(request):
    # breadcrumb = []
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
