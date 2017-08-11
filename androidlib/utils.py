from urlparse import urlparse
import os


def get_proxy_settings(proxy):
  proxy_settings = None
  if proxy:
    if not '://' in proxy:
      proxy = 'http://%s' %  proxy
    parts = urlparse(proxy)
    proxy_host = parts.hostname
    if parts.port:
      proxy_port = parts.port
    proxy_settings = (proxy_host, proxy_port)
  return proxy_settings
