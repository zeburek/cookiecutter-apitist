from dataclasses import dataclass, field

from apitist.hooks import (
    PrepRequestInfoLoggingHook,
    RequestDataclassConverterHook,
    ResponseDataclassConverterHook,
    ResponseInfoLoggingHook,
)
from apitist.requests import Session, session

from common import models as m


def init_session():
    s = session()
    s.add_hook(PrepRequestInfoLoggingHook)
    s.add_hook(ResponseInfoLoggingHook)
    s.add_hook(RequestDataclassConverterHook)
    s.add_hook(ResponseDataclassConverterHook)
    return s


@dataclass
class Client:
    host: str
    _s: Session = field(init=False, default_factory=init_session)
{% if cookiecutter.add_skeletons == "Yes" %}

    # Paths
    GET_USER_AGENT = "/user-agent"
    GET_IP = "/ip"

    # Endpoints access
    def get_user_agent(self):
        return self._s.get(self.host + self.GET_USER_AGENT)

    def get_ip(self):
        return self._s.get(self.host + self.GET_IP)

    # Some logic
    def get_client_info(self):
        return m.InfoModel.from_models(
            self.get_user_agent().structure(m.UAModel).data,
            self.get_ip().structure(m.IpModel).data
        )
{% endif %}
