class Homepage:
    categories = None
    teaser = None
    featured = None

    def __init__(self):
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
        self.teaser = {
            'appident1': {
                'ident': 'gnome-clocks',
                'name': 'Gnome Clocks',
                'platforms': ['debian'],
                'description'
                'categories': ['categoryid1', 'categoryid2'],
                'images': {
                    'banner': 'https://dashboard.snapcraft.io/site_media/appmedia/2017/07/org.gnome.clocks.png',
                    'thumb': '',
                    'zoom': '',
                    'screenshots': [],
                },
                'tags': ['tag1', 'tag2'],
                'publisher': 'somePublisher',
                'external_rating': '',
            },
            'appident2': {
                'ident': '544730',
                'name': 'Catan Universe',
                'platforms': ['proton'],
                'description'
                'categories': ['categoryid1', 'categoryid2'],
                'images': {
                    'banner': 'https://steamcdn-a.akamaihd.net/steam/apps/544730/header.jpg',
                    'thumb': '',
                    'zoom': '',
                    'screenshots': [],
                },
                'tags': ['tag1', 'tag2'],
                'publisher': 'somePublisher',
                'external_rating': '',
            },
            'appident3': {
                'ident': 'appident3',
                'name': 'App3',
                'platforms': ['proton'],
                'description'
                'categories': ['categoryid1', 'categoryid2'],
                'images': {
                    'banner': 'https://www.stuttgarter-nachrichten.de/media.media.5d6dcbb5-e13b-4d81-8b5b-e74d45f3d237.original1024.jpg',
                    'thumb': '',
                    'zoom': '',
                    'screenshots': [],
                },
                'tags': ['tag1', 'tag2'],
                'publisher': 'somePublisher',
                'external_rating': '',
            },
        }
        self.featured = {
            'appident1': {
                'ident': 'gnome-clocks',
                'name': 'Gnome Clocks',
                'platforms': ['debian'],
                'description'
                'categories': ['categoryid1', 'categoryid2'],
                'images': {
                    'banner': 'https://dashboard.snapcraft.io/site_media/appmedia/2017/07/org.gnome.clocks.png',
                    'thumb': '',
                    'zoom': '',
                    'screenshots': [],
                },
                'tags': ['tag1', 'tag2'],
                'publisher': 'somePublisher',
                'external_rating': '',
            },
            'appident2': {
                'ident': '544730',
                'name': 'Catan Universe',
                'platforms': ['proton'],
                'description'
                'categories': ['categoryid1', 'categoryid2'],
                'images': {
                    'banner': 'https://steamcdn-a.akamaihd.net/steam/apps/544730/header.jpg',
                    'thumb': '',
                    'zoom': '',
                    'screenshots': [],
                },
                'tags': ['tag1', 'tag2'],
                'publisher': 'somePublisher',
                'external_rating': '',
            },
            'appident3': {
                'ident': 'appident3',
                'name': 'App3',
                'platforms': ['proton'],
                'description'
                'categories': ['categoryid1', 'categoryid2'],
                'images': {
                    'banner': 'https://www.stuttgarter-nachrichten.de/media.media.5d6dcbb5-e13b-4d81-8b5b-e74d45f3d237.original1024.jpg',
                    'thumb': '',
                    'zoom': '',
                    'screenshots': [],
                },
                'tags': ['tag1', 'tag2'],
                'publisher': 'somePublisher',
                'external_rating': '',
            },
        }
        pass

    def get_data(self):
        data = {
            'categories': self.categories,
            'teaser': self.teaser,
            'featured': self.featured,
        }

        return data
