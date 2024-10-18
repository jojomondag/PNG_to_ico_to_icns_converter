# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['PNG_to_ico_to_icns_converter.py'],
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
    name='PNG_to_ico_to_icns_converter',
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
    icon=['PngIcnsConv.icns'],
)
app = BUNDLE(
    exe,
    name='PNG_to_ico_to_icns_converter.app',
    icon='PngIcnsConv.icns',
    bundle_identifier=None,
)
