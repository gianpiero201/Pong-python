# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('sprits/background_start.jpg', 'sprits'), 
        ('sprits/bola_2.0.png', 'sprits'), 
        ('sprits/bola.svg', 'sprits'), 
        ('sprits/campo.png', 'sprits'),
        ('sprits/fundo_multiplayer.png', 'sprits'),
        ('sprits/fundo_sigleplayer_hard.png', 'sprits'),
        ('sprits/fundo_sigleplayer.png', 'sprits'),
        ('sprits/fundo.png', 'sprits'),
        ('sprits/logo.png', 'sprits'),
        ('sprits/logo.ico', 'sprits'),
        ('sprits/raquete_2.0.png', 'sprits'),
        ('sprits/raquete.svg', 'sprits'),
        ('Sounds/fundo_start.mp3', 'Sounds'),
        ('Sounds/game_easy_mode.mp3', 'Sounds'),
        ('Sounds/game_hard_mode.mp3', 'Sounds'),
        ('Sounds/item_ball.mp3', 'Sounds'),
        ('Sounds/item_menu.mp3', 'Sounds'),
        ('Sounds/multiplayer_score.mp3', 'Sounds'),
        ('Fonts/ARCADECLASSIC.TTF', 'Fonts'),
        ('Fonts/Giant Gnome Regular Ltd.TTF', 'Fonts'),
        ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='sprits/logo.ico'
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
