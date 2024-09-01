# -*- coding: utf-8 -*-
import requests
from enum import Enum


__all__ = ['Client', 'Sound']


class Sound(Enum):
    ALARM = 'alarm'
    ANTICIPATE = 'anticipate'


class Level(Enum):
    ACTIVE = 'active'
    TIME_SENSITIVE = 'timeSensitive'
    passive = 'passive'


class Client:
    """
    Bark API 操作类
    """
    def __init__(self, token: str, url: str = 'https://api.day.app') -> None:
        self._token = token
        self._url = url


    def push(
        self, 
        content: str, 
        title: str='',
        sound: str='',
        is_archive=1,
        icon='',
        group='',
        level=Level.ACTIVE,
        link='',
        copy='',
        badge=0,
        auto_copy=False
    ):
        path = ''
        if title == '':
            path += f'/{content}'
        else:
            path += f'/{title}/{content}'
        
        print(path)

        params = {}
        if sound != '':
            params['sound']=sound
        if is_archive != 1:
            params['isArchive']=0
        if icon != '':
            params['icon']=icon
        if group != '':
            params['group']=group
        params['level']=level.value
        if link != '':
            params['url']=link
        if copy != '':
            params['copy']=copy
        if badge > 0:
            params['badge']=badge
        if not auto_copy:
            params['auto_copy']=1

        requests.get(f'{self._url}/{self._token}{path}', params=params)

