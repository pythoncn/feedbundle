#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os

from flask.ext.script import Manager

from feedbundle.app import FeedBundle


#: be more convenient for developer,
#: automatic to set configuration environment variable.
if os.path.exists("feedbundle.dev.cfg"):
    os.environ['FEEDBUNDLE_CONFIG'] = os.path.abspath("feedbundle.dev.cfg")


app = FeedBundle()
manager = Manager(app)


if __name__ == "__main__":
    manager.run()
