# sh4d0u-sploit

**sh4d0u-sploit** is an interactive Python toolkit for Android device management, ADB automation, and Metasploit payload workflows.

> Use this project only for authorized security testing, device administration, or research. Do not use it on systems without permission.

## Features

- Discover, connect, and manage Android devices over ADB
- Forward and reverse host/device TCP ports using ADB
- Capture screenshots, record screen video, and pull media files
- Push and pull files, install/uninstall apps, and extract APK packages
- Generate Android Meterpreter APKs with `msfvenom`
- Launch a Metasploit handler with `msfconsole`
- Scan LAN hosts for ADB targets using `nmap`
- Automatic dependency helpers for `adb`, `scrcpy`, `nmap`, and Metasploit
- Rich terminal UI with styled menus and prompts

## Requirements

- Python 3.10+
- `adb`
- `scrcpy`
- `nmap`
- Metasploit Framework (`msfvenom`, `msfconsole`)
- Git (optional, for updates)

## Setup

```bash
cd sh4d0uSploit
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows, use PowerShell:

```powershell
cd C:\path\to\sh4d0uSploit
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Install Dependencies

If required tools are missing, you can use the built-in installers:

- Unix/macOS: `bash install.sh --yes --components adb,scrcpy,nmap,metasploit`
- Windows: `powershell -NoProfile -ExecutionPolicy Bypass -File install.ps1 -Components adb,scrcpy,nmap,metasploit -NonInteractive`

The application also prompts to install missing tools automatically on startup.

## Run

```bash
python sh4d0usploit.py
```

## Usage

- The app starts with a terminal menu.
- Navigate pages with the on-screen controls.
- Choose actions for ADB, file management, media capture, port forwarding, and Metasploit workflows.
- If a tool is missing, the app reports it and can help install it.

## Project Layout

- `sh4d0usploit.py` — application entrypoint
- `modules/cli.py` — startup, dependency checks, menu rendering
- `modules/console.py` — styled terminal I/O and ADB helper functions
- `modules/tools.py` — external tool detection and requirement guards
- `modules/connection.py` — ADB device connect/disconnect and network discovery
- `modules/security.py` — Metasploit payload generation and handler flow
- `modules/port_forward.py` — host-device port forwarding and reverse forwarding
- `modules/media.py` — screenshot, screen recording, and media extraction
- `modules/file_manager.py` — push/pull files and APK extraction
- `modules/banner.py` — terminal banners and menu art


## Notes

- `Downloaded-Files/` is used for output and temporary file storage.

## License

See `LICENSE` for license details.
