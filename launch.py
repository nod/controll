#!/usr/bin/env python

import sys
import os.path
import logging
from optparse import OptionParser

import tornado.httpserver
import tornado.ioloop
import tornado.web

from views import routes

def start_instance(settings):
    app = tornado.web.Application(routes, **settings)
    logging.info("starting app at port", settings['httpd_port'])

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(settings.httpd_port)

    try: tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt: pass


def main():

    # setup our application options
    from settings import settings

    parser = OptionParser()
    parser.add_option("-r", "--routes", action="store_true",
            help="print list of routes and exit")
    parser.add_option("-p", "--port", type="int", help="specify httpd port")


    parser.add_option('-l', "--logging", default="info",
            help=("Set the Python log level. If 'none', tornado won't touch the "
                "logging configuration."),
            metavar="info|warning|error|none")

    parser.add_option('-s', "--log_to_stderr", action="store_false",
            default=True,
            help=("Send log output to stderr (colorized if possible). "
                "By default use stderr if --log_file_prefix is not set and "
                "no other logging is configured."))
    parser.add_option('-x', "--log_file_prefix", default='', metavar="PATH",
            help=("Path prefix for log files. "
             "Note that if you are running multiple tornado processes, "
             "log_file_prefix must be different for each of them (e.g. "
             "include the port number)"))
    parser.add_option('-m', "--log_file_max_size", type="int",
            default=100 * 1000 * 1000,
            help="max size of log files before rollover")
    parser.add_option('-n', "--log_file_num_backups", type="int", default=10,
            help="number of log files to keep")

    (options, args) = parser.parse_args()

    if options.routes:
        L = max( len(r.reverse()) for r in routes ) # len of longest path
        fmt_ = "    %%-%ds => %%s" % L
        for r in routes:
            print fmt_ % (r.reverse(), ".".join((
                r.handler_class.__module__,
                r.handler_class.__name__)))
        sys.exit(0)
    elif options.port:
        try: settings.httpd_port = int(options.port)
        except: pass
    elif args:
        try: settings.httpd_port = int(args[0])
        except: pass
    print "starting Tornado on port", settings.httpd_port
    start_instance(settings)


if __name__ == "__main__":
    main()
