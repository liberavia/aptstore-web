import json

from app.models import App

class Homepage:
    categories = None
    teaser = None
    featured = None

    def __init__(self):
        self.set_categories()
        self.set_teaser()
        self.set_featured()

    def get_data(self):
        data = {
            'categories': self.categories,
            'teaser': self.teaser,
            'featured': self.featured,
        }

        return data

    def set_teaser(self):
        teaser_apps = App.objects.filter(teaser=True).values()
        self.teaser = list(teaser_apps)

    def set_featured(self):
        featured_apps = App.objects.filter(featured=True).values()
        self.featured = list(featured_apps)

    def set_categories(self):
        """ Create dummy data """
        self.categories = {
            'categoryid1': {
                'name': 'category1',
                'image_banner': '',
                'image_thumb': '',
                'image_zoom': '',
            },
            'categoryid2': {
                'name': 'category2',
                'image_banner': '',
                'image_thumb': '',
                'image_zoom': '',
            },
        }
