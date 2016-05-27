# -*- coding: utf-8 -*-
import pytest

import werkzeug_rfc7xx


from werkzeug.exceptions import HTTPException, abort


@pytest.mark.parametrize(("msg", "class_name"), [
    ('Cached for too long', 'CachedForTooLong'),
    ('#heartbleed (see 705)', 'HeartbleedSee705'),
    ("Designer's final designs weren't", 'DesignersFinalDesignsWerent'),
    ("Why was this cached?", "WhyWasThisCached"),
    ("Over-Caffeinated", 'OverCaffeinated'),
    ("Unexpected T_PAAMAYIM_NEKUDOTAYIM", 'UnexpectedTPaamayimNekudotayim'),
    ("Fucking Unic:hankey:de", 'FuckingUnicHankeyDe'),
    (
        "This is the last page of the Internet. Go back",
        "ThisIsTheLastPageOfTheInternetGoBack"
    ),
])
def test_msg_to_class_name(msg, class_name):
    assert werkzeug_rfc7xx._msg_to_class_name(msg) == class_name


@pytest.mark.parametrize(('code', 'name'), werkzeug_rfc7xx.ERRORS)
def test_exceptions_classes_available(code, name):
    class_name = werkzeug_rfc7xx._msg_to_class_name(name)
    class_obj = getattr(werkzeug_rfc7xx, class_name)
    class_instance = class_obj()
    assert isinstance(class_instance, HTTPException)
    assert class_instance.code == code
    assert class_instance.description == name


@pytest.mark.parametrize(('code', 'name'), werkzeug_rfc7xx.ERRORS)
def test_abort(code, name):
    class_name = werkzeug_rfc7xx._msg_to_class_name(name)
    class_obj = getattr(werkzeug_rfc7xx, class_name)

    with pytest.raises(class_obj) as exc_info:
        abort(code)
    assert type(exc_info.value) is class_obj
