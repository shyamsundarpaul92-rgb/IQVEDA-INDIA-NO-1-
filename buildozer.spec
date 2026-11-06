[app]
title = IQVEDA INDIA NO 1
package.name = iqvedano1
package.domain = org.iqveda
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0,kivymd,certifi
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a
android.allow_backup = True
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
