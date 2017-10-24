# -*- coding: utf-8 -*-

import os
from eve import Eve
from blueprint_demo import blueprint as bp_demo


port = 5000
host = '127.0.0.1'

app = Eve()


if __name__ == '__main__':
    app.register_blueprint(bp_demo)
    app.run(host=host, port=port, debug=True)
