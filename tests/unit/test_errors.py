import errno
import json

import pytest

from androidlib import errors


class CustomError(errors.BaseError):
  def __init__(self, message):
    super(CustomError, self).__init__(self)
    self.code = errno.ESRCH
    self.message = message


@pytest.fixture
def error():
  return CustomError('my custom message')


def test_error_as_dict(error):
  d = error.as_dict()
  assert d['code'] == 3


def test_error_as_json(error):
  json_string = error.as_json()
  data = json.loads(json_string)
  assert data['message'] == 'my custom message'


def test_as_str(error):
  assert str(error) == '[3] my custom message'

def test_as_repr(error):
  assert repr(error) == "<class 'tests.unit.test_errors.CustomError'>(%s)" % error.__dict__
