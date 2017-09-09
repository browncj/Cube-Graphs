from django.apps import AppConfig


class TrackConfig(AppConfig):
    name = 'track'


def truncate_number(num, digits=3):
    split_num = str(num).split('.')
    return '.'.join([split_num[0], split_num[1][:digits]])
