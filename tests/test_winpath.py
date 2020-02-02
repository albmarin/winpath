#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `WinPath` package."""

import logging
import subprocess
from pathlib import Path

import winpath

logger = logging.getLogger(__name__)


def _system_path(special_folder: str):
    cmd = subprocess.Popen(
        f"powershell.exe [Environment]::GetFolderPath('{special_folder}')",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    os_path, _ = cmd.communicate()

    return os_path.decode("utf-8").strip()


def test_local_appdata():
    path = Path(winpath.get_local_appdata())
    os_path = Path(_system_path("LocalApplicationData"))
    assert path == os_path


def test_appdata():
    path = Path(winpath.get_appdata())
    os_path = Path(_system_path("ApplicationData"))
    assert path == os_path


def test_desktop():
    path = Path(winpath.get_desktop())
    os_path = Path(_system_path("Desktop"))
    assert path == os_path


def test_programs():
    path = Path(winpath.get_programs())
    os_path = Path(_system_path("Programs"))
    assert path == os_path


def test_admin_tools():
    path = Path(winpath.get_admin_tools())
    os_path = Path(_system_path("AdminTools"))
    assert path == os_path


def test_common_admin_tools():
    path = Path(winpath.get_common_admin_tools())
    os_path = Path(_system_path("CommonAdminTools"))
    assert path == os_path


def test_common_appdata():
    path = Path(winpath.get_common_appdata())
    os_path = Path(_system_path("CommonApplicationData"))
    assert path == os_path


def test_common_documents():
    path = Path(winpath.get_common_documents())
    os_path = Path(_system_path("CommonDocuments"))
    assert path == os_path


def test_my_documents():
    path = Path(winpath.get_my_documents())
    os_path = Path(_system_path("MyDocuments"))
    assert path == os_path


def test_cookies():
    path = Path(winpath.get_cookies())
    os_path = Path(_system_path("Cookies"))
    assert path == os_path


def test_history():
    path = Path(winpath.get_history())
    os_path = Path(_system_path("History"))
    assert path == os_path


def test_internet_cache():
    path = Path(winpath.get_internet_cache())
    os_path = Path(_system_path("InternetCache"))
    assert path == os_path


def test_my_pictures():
    path = Path(winpath.get_my_pictures())
    os_path = Path(_system_path("MyPictures"))
    assert path == os_path


def test_program_files():
    path = Path(winpath.get_program_files())
    os_path = Path(_system_path("ProgramFiles"))
    assert path == os_path


def test_program_files_common():
    path = Path(winpath.get_program_files_common())
    os_path = Path(_system_path("CommonProgramFiles"))
    assert path == os_path


def test_system():
    path = Path(winpath.get_system())
    os_path = Path(_system_path("System"))
    assert path == os_path


def test_windows():
    path = Path(winpath.get_windows())
    os_path = Path(_system_path("Windows"))
    assert path == os_path


def test_favorites():
    path = Path(winpath.get_favorites())
    os_path = Path(_system_path("Favorites"))
    assert path == os_path


def test_startup():
    path = Path(winpath.get_startup())
    os_path = Path(_system_path("Startup"))
    assert path == os_path


def test_recent():
    path = Path(winpath.get_recent())
    os_path = Path(_system_path("Recent"))
    assert path == os_path
