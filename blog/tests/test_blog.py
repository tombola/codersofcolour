from blog.models import BlogIndexPage


def test_blog_index_intro_is_richtext():
    assert BlogIndexPage._meta.get_field('intro').__class__.__name__ == 'RichTextField'
