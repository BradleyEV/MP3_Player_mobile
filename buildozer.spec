[app]

# (str) Title of your application
title = MP3 Player

# (str) Package name
package.name = mp3player

# (str) Package domain (must be unique, reverse domain style)
package.domain = org.bevstudio

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,mp3

# (str) Application requirements (comma-separated)
# Make sure all libraries are installable in the build environment
requirements = python3,kivy,pytube,ffmpeg,mutagen

# (list) Permissions your app needs
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
