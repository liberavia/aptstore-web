from app.models import App


class DetailsPage:
    appid = None
    app_data = None

    def __init__(self, appid):
        self.appid = appid
        self.set_appdata()

    def set_appdata(self):
        """
        @todo: catch type error on wrong appid
        :return:
        """
        app = App.objects.filter(pk=self.appid)
        app_data = app.values().first()
        platforms = app.first().platforms.all()
        platforms_list = [platform.name for platform in platforms]
        categories = app.first().categories.all()
        # categories_i18n = self.get_categories_i18n(categories)
        categories_list = [category.name for category in categories]
        tags = app.first().tags.all()
        tags_list = [tag.name for tag in tags]

        app_data['platforms'] = platforms_list
        app_data['categories'] = categories_list
        app_data['tags'] = tags_list

        self.app_data = app_data

    def get_app_data(self):
        return dict(self.app_data)
