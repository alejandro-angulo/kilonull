from codesnip.models import Snippet
from django.core.exceptions import ObjectDoesNotExist


def shortcode_snippet(*args):
    try:
        snippet = Snippet.objects.get(slug=args[0])
        html = snippet.pygmentized
    except (ObjectDoesNotExist, IndexError):
        html = "<div class='alert alert-warning' " \
            "role='alert'>Could not load code snippet. :(</div>"

    return html
