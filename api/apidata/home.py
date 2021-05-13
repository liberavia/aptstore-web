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
                'ident': 'appident1',
                'name': '',
                'platforms': ['proton'],
                'description'
                'categories': ['categoryid1', 'categoryid2'],
                'images': {
                    'banner': '',
                    'thumb': '',
                    'zoom': '',
                    'screenshots': [],
                },
                'tags': ['tag1', 'tag2'],
                'publisher': 'somePublisher',
                'external_rating': '',
            },
            'appident2': {
                'ident': 'appident2',
                'name': '',
                'platforms': ['proton'],
                'description'
                'categories': ['categoryid1', 'categoryid2'],
                'images': {
                    'banner': '',
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
                'name': '',
                'platforms': ['proton'],
                'description'
                'categories': ['categoryid1', 'categoryid2'],
                'images': {
                    'banner': '',
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
                'ident': 'appident1',
                'name': '',
                'platforms': ['proton'],
                'description'
                'categories': ['categoryid1', 'categoryid2'],
                'images': {
                    'banner': '',
                    'thumb': '',
                    'zoom': '',
                    'screenshots': [],
                },
                'tags': ['tag1', 'tag2'],
                'publisher': 'somePublisher',
                'external_rating': '',
            },
            'appident2': {
                'ident': 'appident2',
                'name': '',
                'platforms': ['proton'],
                'description'
                'categories': ['categoryid1', 'categoryid2'],
                'images': {
                    'banner': '',
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
                'name': '',
                'platforms': ['proton'],
                'description'
                'categories': ['categoryid1', 'categoryid2'],
                'images': {
                    'banner': '',
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
