from app.models import App


class DetailsPage:
    appid = None
    app_data = None

    def __init__(self, appid):
        self.appid = appid
        self.set_appdata()

    def set_appdata(self):
        app = App.objects.filter(pk=self.appid).values().first()
        self.app_data = app

    def get_app_data(self):
        return dict(self.app_data)
