import os
import subprocess

import mock
import pytest

from androidlib import props
props.bootstrap('tests/fixtures/props.cfg')
props.refresh()
from androidlib import keytool, errors


def test_keytool_path():
  path = keytool.keytool_path()
  assert path == '%s/android.debug' % os.environ.get('ANDROID_HOME', props.sdk.path)


def test_keytool_gen_success():
  subprocess.call = mock.create_autospec(subprocess.call, return_value=0)
  code = keytool.gen('alias', 'name', 'unit', 'org', 'loc', 'state', 'country', 'storepass', 'keypass')
  assert code is None


def test_keytool_gen_error():
  subprocess.call = mock.create_autospec(subprocess.call, return_value=-2)
  with pytest.raises(errors.RuntimeError) as err:
    keytool.gen('alias', 'name', 'unit', 'org', 'loc', 'state', 'country', 'storepass', 'keypass')
  assert err.value.code == -2
