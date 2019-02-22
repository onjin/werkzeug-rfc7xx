[![](https://img.shields.io/pypi/v/werkzeug_rfc7xx.svg)](https://img.shields.io/pypi/v/werkzeug_rfx7xx)
[![](https://travis-ci.org/onjin/werkzeug-rfc7xx.svg)](https://travis-ci.org/onjin/werkzeug-rfc7xx)
# werkzeug RFC 7XX exceptions

Additional werkzeuk/flask exceptions according to **RFX 7XX**:

* https://github.com/joho/7XX-rfc

Installation:

  pip install werkzeug-rfc7xx


Usage with **flask**:

```python
import werkzeug_rfc7xx
from flask import abort

abort(701)
```

Usage with **werkzeug**:

```python
import werkzeug_rfc7xx
from werkzeug.exceptions import abort

abort(701)
```

