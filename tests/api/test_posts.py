import allure
import pytest
from pydantic import TypeAdapter

from models.post import Post

pytestmark = [allure.feature("REST API"), allure.story("Posts")]


@pytest.mark.smoke
def test_get_post_returns_200(api_client):
    response = api_client.get("/posts/1")
    assert response.status_code == 200


@pytest.mark.regression
def test_get_post_matches_schema(api_client):
    response = api_client.get("/posts/1")
    post = Post.model_validate(response.json())
    assert post.id == 1
    assert post.user_id == 1
    assert post.title
    assert post.body


@pytest.mark.regression
def test_list_posts_match_schema(api_client):
    response = api_client.get("/posts")
    assert response.status_code == 200
    posts = TypeAdapter(list[Post]).validate_python(response.json())
    assert posts
    assert all(post.id > 0 for post in posts)


@pytest.mark.regression
def test_missing_post_returns_404(api_client):
    response = api_client.get("/posts/0")
    assert response.status_code == 404
