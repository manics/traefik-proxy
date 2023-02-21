
from traitlets import Unicode
from .fileprovider import TraefikFileProviderProxy


class TraefikTomlProxy(TraefikFileProviderProxy):
    """Deprecated alias for file provider"""
    toml_dynamic_config_file = Unicode(
        config=True,
    ).tag(
        deprecated_in="0.4",
        deprecated_for="TraefikFileProvider.dynamic_config_file",
    )
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.log.warning("TraefikTomlProxy is deprecated in jupyterhub-traefik-proxy 0.4. Use `c.JupyterHub.proxy_class = 'traefik_file'")
