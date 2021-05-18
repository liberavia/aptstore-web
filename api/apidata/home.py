from app.models import App, Category


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
        categories = Category.objects.values()
        self.categories = list(categories)
