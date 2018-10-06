"""
.. module:: vanilla.views
   synopsis: project views.
"""
import logging
from django.http import HttpResponse

LOGGER = logging.getLogger(__name__)


def index(request):
    """Index view."""
    LOGGER.debug("request: %s", request)
    LOGGER.info("Index view.")
    return HttpResponse(
        "<html>"
        "    <body>"
        "        <h1>We did it!</h1>"
        "    </body>"
        "</html>"
    )
