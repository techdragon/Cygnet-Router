from __future__ import print_function

from twisted.internet.defer import inlineCallbacks
from autobahn import wamp
from autobahn.twisted.wamp import ApplicationSession


class ControllerBackend(ApplicationSession):

    def __init__(self, config):
        ApplicationSession.__init__(self, config)

    @inlineCallbacks
    def onJoin(self, details):
        res = yield self.register(self)
        print("ControllerBackend: {} procedures registered!".format(len(res)))
