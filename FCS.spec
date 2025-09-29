# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['/Users/K/Desktop/Code/Builds/QCS/GUI.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='FCS',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['works.icns'],
)
app = BUNDLE(
    exe,
    name='FCS.app',
    icon='works.icns',
    bundle_identifier=None,
    info_plist={
    'CFBundleShortVersionString': '1.0.0',
    'CFBundleVersion': '2025.9.28',
    'CFBundleName': 'FCS',
    'CFBundleDisplayName': 'FCS',
    'CFBundleGetInfoString': 'FCS version 1.0.0',
    'NSHumanReadableCopyright': '© 2025 Khalil Alkhodor',
    'CFBundleIdentifier': 'com.khalil.fcs',
    'CFBundleInfoDictionaryVersion': '6.0',
    },
)
