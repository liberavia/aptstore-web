from app.models import App, AppRegional


class Teaser:
    region = None
    teaser = None

    def __init__(self, region):
        self.region = region
        self.set_teaser()

    def get_data(self):
        return self.teaser

    def set_teaser(self):
        teaser_apps = App.objects.filter(teaser=True).all()
        parsed_teaser_apps = []
        for teaser_app in teaser_apps:
            app = App.objects.filter(pk=teaser_app.pk)
            app_data = app.values().first()
            app_i18n = self.get_app_i18n(app)
            if app_i18n:
                app_data['name'] = app_i18n['name']
                app_data['description_short'] = app_i18n['short']
                app_data['description_long'] = app_i18n['long']
                app_data['price'] = app_i18n['price']
                app_data['price_initial'] = app_i18n['price_initial']
            parsed_teaser_apps.append(app_data)

        self.teaser = parsed_teaser_apps

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
