import os

import pytest


@pytest.fixture
def cwd():
  return os.path.dirname(os.path.realpath(__file__))


@pytest.fixture
def android_home(cwd):
  return '%s/fixtures/android-sdk-linux' % cwd


@pytest.fixture
def props_path(cwd):
  return '%s/fixtures/props.cfg' % cwd
