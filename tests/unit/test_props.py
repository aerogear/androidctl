import pytest

from androidlib import props


@pytest.fixture
def prop(props_path):
  props.bootstrap(props_path)
  props.refresh()
  return props


def test_sdk_path(prop):
  assert prop.sdk.path == 'my-sdk-path'


def test_keystore_path(prop):
  assert prop.keytool.name == 'android.debug.fixture'
