import komgaApi
import bangumiApi
from config import *
from log import logger


class InitEnv:
    def __init__(self):
        self.bgm = bangumiApi.BangumiApi(BANGUMI_ACCESS_TOKEN)
        # Initialize the komga API
        self.komga = komgaApi.KomgaApi(
            KOMGA_BASE_URL, KOMGA_EMAIL, KOMGA_EMAIL_PASSWORD)
        self.all_series = []

        if KOMGA_LIBRARY_LIST and KOMGA_COLLECTION_LIST:
            logger.error(
                "Use only one of KOMGA_LIBRARY_LIST or KOMGA_COLLECTION_LIST")
        elif KOMGA_LIBRARY_LIST:
            for library in KOMGA_LIBRARY_LIST:
                self.all_series.extend(
                    self.komga.get_series_with_libaryid(library)['content'])
        elif KOMGA_COLLECTION_LIST:
            for collection in KOMGA_COLLECTION_LIST:
                self.all_series.extend(
                    self.komga.get_series_with_collection(collection)['content'])
        else:
            self.all_series = self.komga.get_all_series()['content']
