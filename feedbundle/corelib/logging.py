#!/usr/bin/env python
#-*- coding:utf-8 -*-

from __future__ import absolute_import

import logging
import logging.handlers


def make_multiline_formatter():
    """Create a logging formatter to dump all information."""
    formatter = ["-" * 78,
            "Name:               %(name)s",
            "Message type:       %(levelname)s",
            "Location:           %(pathname)s:%(lineno)d",
            "Module:             %(module)s",
            "Function:           %(funcName)s",
            "Time:               %(asctime)s",
            "Message:",
            "%(message)s",
            "-" * 78]
    return logging.Formatter("\n".join(formatter))


def make_file_handler(path, formatter_factory=make_multiline_formatter,
        level=logging.DEBUG):
    """Create a file handler to record logging information into a file."""
    file_handler = logging.handlers.WatchedFileHandler(path)
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter_factory())
    return file_handler
