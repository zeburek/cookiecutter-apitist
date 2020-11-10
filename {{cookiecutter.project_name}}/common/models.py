from dataclasses import dataclass

from convclasses import mod
{% if cookiecutter.add_skeletons == "Yes" %}


@dataclass
class UAModel:
    user_agent: str = mod.name("user-agent")


@dataclass
class IpModel:
    origin: str


@dataclass
class InfoModel:
    user_agent: str
    ip: str

    @staticmethod
    def from_models(ua: UAModel, ip: IpModel):
        return InfoModel(
            user_agent=ua.user_agent,
            ip=ip.origin
        )
{% endif %}
