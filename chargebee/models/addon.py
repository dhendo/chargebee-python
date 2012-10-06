from chargebee.model import Model
from chargebee import request


class Addon(Model):

    @staticmethod
    def list(params=None, env=None):
        return request.send('get', '/addons', params, env)

    @staticmethod
    def retrieve(id, env=None):
        return request.send('get', '/addons/%s' % id, {}, env)