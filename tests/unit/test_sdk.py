import os
import subprocess

import mock
import pytest

from androidlib import props
props.bootstrap('tests/fixtures/props.cfg')
props.refresh()
from androidlib import sdk, errors


def test_manager():
  subprocess.call = mock.create_autospec(subprocess.call, return_value=0)
  res = sdk.manager('platforms;25')
  assert res is None


def test_manager_error():
  subprocess.call = mock.create_autospec(subprocess.call, return_value=-1)
  with pytest.raises(errors.RuntimeError) as err:
    sdk.manager('platforms;25')
  assert err.value.code == -1
