# coding=utf-8
from flask import Flask, g
from .db import RedisClient

'''
[接口模块]
'''

# initial setting
__all__ = ['app']
app = Flask(__name__)


def get_conn():
    # attention this way +--
    if not hasattr(g, 'redis'):
        g.redis = RedisClient()
    return g.redis


# 首页
@app.route('/')
def index():
    return '<h2>Welcome to Proxy Pool System</h2>'


# 代理页面
@app.route('/random')
def get_proxy():
    """
    Get a proxy
    :return: 随机代理
    """
    conn = get_conn()
    return conn.random()


# 统计代理数量页面
@app.route('/count')
def get_counts():
    """
    Get the count of proxies
    :return: 代理池总量
    """
    conn = get_conn()
    return str(conn.count())


if __name__ == '__main__':
    app.run()
