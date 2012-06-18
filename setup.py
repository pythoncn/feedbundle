#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
kwargs = {}
major, minor = sys.version_info[:2]
if major >= 3:
    kwargs['use_2to3'] = True
