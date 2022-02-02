from app.models import App, AppRegional


class Featured:
    region = None
    featured = None

    def __init__(self, region):
        self.region = region
        self.set_featured()

    def get_data(self):
        return self.featured

    def set_featured(self):
        featured_apps = App.objects.filter(featured=True).all()
        parsed_featured_apps = []
        for featured_app in featured_apps:
            app = App.objects.filter(pk=featured_app.pk)
            app_data = app.values().first()
            app_i18n = self.get_app_i18n(app)
            if app_i18n:
                app_data['name'] = app_i18n['name']
                app_data['description_short'] = app_i18n['short']
                app_data['description_long'] = app_i18n['long']
                app_data['price'] = app_i18n['price']
                app_data['price_initial'] = app_i18n['price_initial']
            parsed_featured_apps.append(app_data)

        self.featured = parsed_featured_apps

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
