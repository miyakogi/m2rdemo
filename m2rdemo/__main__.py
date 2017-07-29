#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
from multiprocessing import Process

from wdom import options, server
from wdom.document import set_app

from m2rdemo import sample_page


def open_webview() -> None:
    from webview import create_window
    server.start_server()
    p = Process(target=create_window,
                args=('M2R DEMO', 'http://localhost:8888'))
    p.start()
    try:
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        server.stop_server()


def open_browser() -> None:
    options.config.open_browser = True
    server.start()


if __name__ == '__main__':
    options.config.auto_shutdown = True  # Enable wdom auto shutdown
    set_app(sample_page())
    try:
        open_webview()
    except ImportError:
        open_browser()
