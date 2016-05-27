[![](https://img.shields.io/pypi/v/werkzeug_rfc7xx.svg)](https://img.shields.io/pypi/v/werkzeug_rfx7xx)
[![](https://travis-ci.org/onjin/werkzeug-rfc7xx.svg)](https://travis-ci.org/onjin/werkzeug-rfc7xx)
# werkzeug RFC 7XX exceptions

Additional werkzeuk/flask exception according to RFX 7XX:

* https://github.com/joho/7XX-rfc


Usage:

  import werkzeug_rfc7xx
  from werkzeug.exceptions import abort

  abort(701)
