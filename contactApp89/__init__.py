from os import path
from django.apps import AppConfig
VERBOSE_APP_NAME = '道具创意征集列表'


def get_current_app_name(file):
    return path.dirname(file).replace('\\', '/').split('/')[-1]


class AppVerboseNameConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = VERBOSE_APP_NAME  # 设置别名


default_app_config = get_current_app_name(
    __file__) + '.__init__.AppVerboseNameConfig'
