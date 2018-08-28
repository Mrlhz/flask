class UrlManager(object):
    @staticmethod
    def build_url(path):
        return path

    @staticmethod
    def build_static_url(path):
        path = path + "?ver=" + "201808281000"
        return UrlManager.build_url(path)
