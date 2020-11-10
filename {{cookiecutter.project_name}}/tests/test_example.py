import logging

from common import models as m


def test_new(api):
    logging.info(api.host)
{% if cookiecutter.add_skeletons == "Yes" %}


def test_user_agent(api):
    data: m.UAModel = api.get_user_agent().structure(m.UAModel).data
    assert data.user_agent, "Empty user-agent in response"


def test_ip_address(api):
    data: m.IpModel = api.get_ip().structure(m.IpModel).data
    assert data.origin, "Empty origin in response"


def test_get_info(api):
    info = api.get_client_info()
    info2 = api.get_client_info()
    assert info == info2, "User-agent or ip was changed"
{% endif %}
