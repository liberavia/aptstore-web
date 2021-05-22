from app.models import App, AppRegional, CategoryRegional


class DetailsPage:
    appid = None
    region = None
    app_data = None

    def __init__(self, appid, region):
        self.appid = appid
        self.region = region
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
        categories_list = self.get_categories_i18n(categories)
        tags = app.first().tags.all()
        tags_list = [tag.name for tag in tags]

        app_data['platforms'] = platforms_list
        app_data['categories'] = categories_list
        app_data['tags'] = tags_list

        app_i18n = self.get_app_i18n(app)
        if app_i18n:
            app_data['name'] = app_i18n['name']
            app_data['description_short'] = app_i18n['short']
            app_data['description_long'] = app_i18n['long']
            app_data['price'] = app_i18n['price']
            app_data['price_initial'] = app_i18n['price_initial']

        self.app_data = app_data

    def get_app_data(self):
        return dict(self.app_data)

    def get_categories_i18n(self, categories):
        categories_i18n = []
        for category in categories:
            cregional = CategoryRegional.objects.filter(region=self.region, category=category.pk).first()
            if cregional:
                categories_i18n.append(cregional.name)
            else:
                categories_i18n.append(category.name)

        return categories_i18n

    def get_app_i18n(self, app):
        app_i18n = None
        app_entity = app.first()
        app_regional = AppRegional.objects.filter(region=self.region, app=app_entity.pk).first()
        if app_regional:
            app_i18n = {
                'name': app_regional.name,
                'short': app_regional.description_short,
                'long': app_regional.description_long,
                'price': app_regional.price,
                'price_initial': app_regional.price_initial,
                'currency': app_regional.currency
            }

        return app_i18n

