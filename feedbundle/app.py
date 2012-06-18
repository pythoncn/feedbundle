#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os

from flask import Flask
from werkzeug import import_string

from feedbundle.corelib.logging import make_file_handler


class FeedBundle(Flask):
    """The web application."""

    CONFIG_ENV = "FEEDBUNDLE_CONFIG"
    BUILTIN_CONFIG = "app.cfg"

    def __init__(self, import_name=__package__, *args, **kwargs):
        super(FeedBundle, self).__init__(import_name, *args, **kwargs)

        #: load built-in and local configuration
        self.config.from_pyfile(self.get_absolute_path(self.BUILTIN_CONFIG))
        self.config.from_envvar(self.CONFIG_ENV)
        self.config.setdefault("BUILTIN_BLUEPRINTS", [])
        self.config.setdefault("BUILTIN_EXTENSIONS", [])
        self.config.setdefault("BLUEPRINTS", [])
        self.config.setdefault("EXTENSIONS", [])
        self.config.setdefault("LOGGING_FILE", None)

        #: initialize the application
        self.init_extensions()
        self.init_logger()
        self.init_blueprints()

    def init_extensions(self):
        """Initialize the extensions of the application."""
        #: make a set to contain names of the extensions
        extensions = set(self.config['BUILTIN_EXTENSIONS'])
        extensions.update(self.config['EXTENSIONS'])

        #: import and install the extensions
        for extension_name in extensions:
            extension = import_string(extension_name)
            extension.init_app(self)

    def init_logger(self):
        """Append more handlers to the application logger."""
        #: create a file handler and install it
        filepath = self.config['LOGGING_FILE']
        if filepath:
            file_handler = make_file_handler(filepath)
            self.logger.addHandler(file_handler)

    def init_blueprints(self):
        """Register all blueprints to the application."""
        #: make a set to contain names of the blueprints
        blueprints = set(self.config['BUILTIN_BLUEPRINTS'])
        blueprints.update(self.config['BLUEPRINTS'])

        #: import and install all blueprints
        for blueprint_name in blueprints:
            package_name = blueprint_name.replace(":", ".").rsplit(".", 1)
            self.register_blueprint_by_name(blueprint_name, package_name)

    def register_blueprint_by_name(self, name, package_name):
        """Register the blueprint by its name."""
        #: import the blueprint object and its package
        blueprint = import_string(name)
        package = import_string(package_name)

        #: load the all submodules
        for module_name in getattr(package, "__all__", []):
            import_string("%s.%s" % (package_name, module_name), silent=True)

        #: register the blueprint
        self.register_blueprint(blueprint)
        self.logger.info("Loaded %r" % name)

    def get_absolute_path(self, relative_path):
        """Create a absolute path from a relative path.

        Example:
        >>> app.root_path
        '/home/tonyseek/projects/myapp/myapp'
        >>> app.get_full_path("../somefile")
        '/home/tonyseek/projects/myapp/somefile'
        """
        path = os.path.join(self.root_path, relative_path)
        return os.path.abspath(path)
