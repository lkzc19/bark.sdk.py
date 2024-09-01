import os

from dotenv import load_dotenv

from bark.client import Client, Level, Sound

load_dotenv
token = os.getenv('token')


def test_client_push_content():
    """
    测试Client类Push方法
    推送内容
    """
    Client(token=token).push(content="test_client_push_content")


def test_client_push_title():
    """
    测试Client类Push方法
    推送标题和内容
    """
    Client(token=token).push(title="test_client_push_title", content="test_client_push_content")


def test_client_push_sound():
    """
    测试Client类Push方法
    推送铃声设置
    """
    Client(token=token).push(content="test_client_push_sound", sound=Sound.ALARM.value)


def test_client_push_is_archive():
    """
    测试Client类Push方法
    推送保存设置
    """
    Client(token=token).push(content="test_client_push_is_archive", is_archive=0)


def test_client_push_is_archive():
    """
    测试Client类Push方法
    推送图标设置
    """
    Client(token=token).push(content="test_client_push_is_archive")


def test_client_push_group():
    """
    测试Client类Push方法
    推送分组设置
    """
    client = Client(token=token)
    client.push(content="test_client_push_group1", group='nahida')
    client.push(content="test_client_push_group2", group='nahida')
    client.push(content="test_client_push_group3", group='hutao')
    client.push(content="test_client_push_group4", group='hutao')


def test_client_push_level():
    """
    测试Client类Push方法
    推送时效性通知
    """
    Client(token=token).push(content="test_client_push_level", level=Level.TIME_SENSITIVE)


def test_client_push_url():
    """
    测试Client类Push方法
    推送链接跳转
    """
    Client(token=token).push(content="test_client_push_url", link='https://day.app/')


def test_client_push_copy():
    """
    测试Client类Push方法
    推送复制
    """
    Client(token=token).push(content="test_client_push_copy", copy='https://day.app/')


def test_client_push_badge():
    """
    测试Client类Push方法
    推送角标设置
    """
    Client(token=token).push(content="test_client_push_badge", badge=42)


def test_client_push_auto_copy():
    """
    测试Client类Push方法
    推送角标设置
    """
    Client(token=token).push(content="test_client_push_badge", auto_copy=True, copy="https://drinkice.xyz/")