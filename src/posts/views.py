from django.shortcuts import render

from config.components.log_config import get_logger
from instagram.utils import get_loader

from .forms import InstagramVideoPostShortForm, InstagramVideoPostURLForm

logger = get_logger(__name__)


def ig_video_post_url_view(request):
    url_form = InstagramVideoPostURLForm()
    post_data = {"view_count": 0, "likes_count": 0, "comments_count": 0}

    if request.method == "POST":
        url_form = InstagramVideoPostURLForm(request.POST)
        if url_form.is_valid():
            url = url_form.cleaned_data["url"]
            try:
                post_info = get_loader().get_instagram_post_info(post_url=url)
            except NotImplementedError as exc:
                logger.error("Error: {}", str(exc))
                return render(
                    request,
                    "posts/ig_video_post_url.html",
                    {
                        "url_form": url_form,
                        "post_form": InstagramVideoPostShortForm(initial=post_data),
                        "error": str(exc),
                    },
                )
            post_data = post_info.model_dump()
    post_form = InstagramVideoPostShortForm(initial=post_data)
    return render(
        request,
        "posts/ig_video_post_url.html",
        {
            "url_form": url_form,
            "post_form": post_form,
        },
    )
