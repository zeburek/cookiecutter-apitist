from dataclasses import dataclass, field

from apitist import (
    PrepRequestInfoLoggingHook,
    RequestDataclassConverterHook,
    ResponseDataclassConverterHook,
    ResponseInfoLoggingHook,
    Session,
    session,
)
from apitist.decorators import get

from common import models as m


def init_session(base_url: str = None):
    s = session(base_url)
    s.add_hook(PrepRequestInfoLoggingHook)
    s.add_hook(ResponseInfoLoggingHook)
    s.add_hook(RequestDataclassConverterHook)
    s.add_hook(ResponseDataclassConverterHook)
    return s


@dataclass
class Client:
    host: str
    session: Session = field(init=False)

    def __post_init__(self):
        self.session = init_session(self.host)
{% if cookiecutter.add_skeletons == "Yes" %}

    # Paths
    GET_USER_AGENT = "/user-agent"
    GET_IP = "/ip"

    # Endpoints access
    @get(GET_USER_AGENT)
    def get_user_agent(self):
        ...

    @get(GET_IP)
    def get_ip(self):
        ...

    # Some logic
    def get_client_info(self):
        return m.InfoModel.from_models(
            self.get_user_agent().structure(m.UAModel).data,
            self.get_ip().structure(m.IpModel).data
        )
{% endif %}
