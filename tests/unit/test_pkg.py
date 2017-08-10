import os
import subprocess

import mock
import pytest

from androidlib import props
props.bootstrap()
props.refresh()
from androidlib import pkg, errors


def test_installed_pkgs_invalid_name(monkeypatch, android_home):
  monkeypatch.setitem(os.environ, 'ANDROID_HOME', android_home)
  assert pkg.installed_pkgs('') == []


def test_installed_pkgs_valid_name(monkeypatch, android_home):
  monkeypatch.setitem(os.environ, 'ANDROID_HOME', android_home)
  assert len(pkg.installed_pkgs('platforms')) == 2


def test_installed_pkgs_empty_folder(monkeypatch, android_home):
  monkeypatch.setitem(os.environ, 'ANDROID_HOME', android_home)
  assert len(pkg.installed_pkgs('build-tools')) == 0
