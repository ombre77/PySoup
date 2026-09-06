from dataclasses import dataclass

@dataclass(frozen=True)
class FontKey:
    namespace: str
    value: str

    @classmethod
    def of(cls, key: str) -> "FontKey":
        if ":" in key:
            ns, val = key.split(":", 1)
        else:
            ns, val = "minecraft", key
        return cls(ns, val)

    def as_string(self) -> str:
        return f"{self.namespace}:{self.value}"


class VanillaFont:
    DEFAULT = FontKey("minecraft", "default")
    UNIFORM = FontKey("minecraft", "uniform")
    ALT = FontKey("minecraft", "alt")
    ILLAGERALT = FontKey("minecraft", "illageralt")