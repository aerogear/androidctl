import sdk
import os
import props
import errors

def installed_pkgs(name):
  if not name:
    return []
  sdk_path = os.environ.get('ANDROID_HOME', props.sdk.path)
  pkg_path = '%s/%s' % (sdk_path, name)
  try:
    folder_items = os.listdir(pkg_path)
    return [item for item in folder_items if os.path.isdir('%s/%s' % (pkg_path, item))]
  except OSError as err:
    return []


def install(name, version):
  sdk.manager('%s;%s' % (name.replace(':', ':'), version))


def uninstall(name, version):
  sdk.manager('%s;%s' % (name.replace(':', ':'), version), '--uninstall')


def sync(data):
  items = []
  purge_list = []
  items.extend(data.get('base', []))
  for item in [i for i in data if i != 'base']:
    k, v = item, data[item]
    pkgs = ['%s;%s' % (k.replace(':', ';'), i) for i in v]
    items.extend(pkgs)
    folder = k.replace(':', '/')
    installed = ['%s;%s' % (k.replace(':', ';'), i) for i in installed_pkgs(folder)]
    purge_list.extend([p for p in installed if not p in pkgs])
  if len(purge_list) > 0:
    purge_list.extend(['--uninstall'])
    sdk.manager(*purge_list)
  sdk.manager(*items)
