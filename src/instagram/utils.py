from typing import Optional

from django.utils.translation import gettext_lazy as _
from instaloader.instaloader import Instaloader
from instaloader.structures import Post

from config.components.log_config import get_logger
from config.config_models import InstagramLoginCreditentials
from instagram.data_models import InstagramVideoPostModel
from instagram.exceptions import InstaloaderLoginException

logger = get_logger(__name__)


class InstagramLoader:
    __logged_users = {}

    def __init__(
        self,
        user_data: InstagramLoginCreditentials,
        download_pictures: bool = False,
        download_videos: bool = False,
        download_video_thumbnails: bool = False,
        save_metadata: bool = False,
    ) -> None:
        self.username = user_data.username
        self.loader = self.get_loader(
            user_data,
            download_pictures=download_pictures,
            download_videos=download_videos,
            download_video_thumbnails=download_video_thumbnails,
            save_metadata=save_metadata,
        )

    @classmethod
    def instaloader_login(
        cls, loader: Instaloader, user_data: InstagramLoginCreditentials
    ) -> None:
        try:
            logger.info("Logging in...")
            loader.login(user_data.username, user_data.password)
            loader.save_session_to_file()
        except InstaloaderLoginException as exc:
            logger.exception("Failed to login. Details: {}", str(exc))
            raise
        except PermissionError as exc:
            logger.exception("Failed to save session to file. Details: {}", str(exc))
        else:
            logger.info("Session successfully saved to file")

    @classmethod
    def get_loader(
        cls,
        user_data: InstagramLoginCreditentials,
        download_pictures: bool = False,
        download_videos: bool = False,
        download_video_thumbnails: bool = False,
        save_metadata: bool = False,
    ) -> Instaloader:
        if user_data.username in cls.__logged_users:
            return cls.__logged_users[user_data.username]

        loader = Instaloader(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0",
            download_pictures=download_pictures,
            download_videos=download_videos,
            download_video_thumbnails=download_video_thumbnails,
            save_metadata=save_metadata,
        )

        try:
            loader.load_session_from_file(user_data.username)
            logger.info("Session loaded from file")
        except FileNotFoundError:
            logger.info("Session file not found")
            cls.instaloader_login(loader, user_data)

        cls.__logged_users[user_data.username] = loader

        return loader

    @staticmethod
    def get_shortcode(post_url: str) -> str:
        return post_url.split("/")[-2]

    def _get_instagram_post(self, shortcode: str) -> Post:
        logger.debug("Getting post with shortcode: {}", shortcode)
        post = Post.from_shortcode(self.loader.context, shortcode)
        return post

    def _create_video_post_model(self, post: Post) -> InstagramVideoPostModel:
        return InstagramVideoPostModel(
            media_id=post.mediaid,
            shortcode=post.shortcode,
            owner_id=post.owner_id,
            owner_username=post.owner_username,
            typename=post.typename,
            create_date=post.date_utc,
            likes_count=post.likes,
            comments_count=post.comments,
            url=post.video_url,  # type: ignore
            thumbnail=post.url,  # type: ignore
            duration=post.video_duration,
            view_count=post.video_view_count,
        )

    def get_instagram_post_info(self, *, post_url: str = "", post_shortcode: str = ""):
        logger.debug("Getting post info")
        if not post_shortcode and not post_url:
            raise ValueError(_("You must provide either post_url or post_shortcode"))
        if post_shortcode and post_url:
            other_shortcode = self.get_shortcode(post_url)
            if post_shortcode != other_shortcode:
                raise ValueError(
                    _(
                        "Provided post_shortcode and post_url are different. You must provide only one of post_url or post_shortcode"
                    )
                )
        if not post_shortcode:
            post_shortcode = self.get_shortcode(post_url)

        post = self._get_instagram_post(post_shortcode)

        if post.is_video:
            return self._create_video_post_model(post)
        else:
            raise NotImplementedError(_("Only video posts are supported for now"))


default_user = InstagramLoginCreditentials()  # type: ignore


def get_loader(
    user_data: Optional[InstagramLoginCreditentials] = None,
) -> InstagramLoader:
    if user_data is None:
        return InstagramLoader(default_user)
    return InstagramLoader(user_data)
