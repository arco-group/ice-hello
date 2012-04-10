#!/usr/bin/python -u
# -*- coding: utf-8 -*-

import sys
import Ice

Ice.loadSlice('./factorial.ice')
import Example


def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)


class MathI(Example.Math):
    def factorial(self, n, current=None):
        return factorial(n)


class Server(Ice.Application):
    def run(self, argv):
        ic = self.communicator()

        adapter = ic.createObjectAdapter("HelloAdapter")
        base = adapter.add(MathI(), ic.stringToIdentity("hello1"))

        print base

        adapter.activate()
        self.shutdownOnInterrupt()
        ic.waitForShutdown()

        return 0


sys.exit(Server().main(sys.argv))
