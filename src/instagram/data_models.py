from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field
from pydantic_core import Url


class InstagramBasePostModel(BaseModel):
    model_config: ConfigDict = ConfigDict(
        title="Instagram Base Post Model",
        extra="ignore",
        validate_assignment=True,
    )

    media_id: int = Field(description="Post ID")
    shortcode: str = Field(description="Post shortcode")
    owner_id: int = Field(description="Post owner ID")
    owner_username: str = Field(description="Post owner username")
    typename: str = Field(
        description="Type of post: GraphImage, GraphVideo or GraphSidecar"
    )
    create_date: datetime = Field(description="Post creation date at UTC time")
    comments_count: int = Field(description="Comments count including answers")
    likes_count: int = Field(description="Likes count")


class InstagramImagePostModel(InstagramBasePostModel):
    model_config: ConfigDict = ConfigDict(
        title="Instagram Image Post Model",
        extra="ignore",
        validate_assignment=True,
    )

    url: Url = Field(description="URL of the picture")


class InstagramVideoPostModel(InstagramBasePostModel):
    model_config: ConfigDict = ConfigDict(
        title="Instagram Video Post Model",
        extra="ignore",
        validate_assignment=True,
    )

    url: str = Field(description="URL of the video")
    thumbnail: str = Field(description="URL of the video thumbnail")
    duration: Optional[float] = Field(description="Duration of the video in seconds")
    view_count: Optional[int] = Field(description="View count of the video")
