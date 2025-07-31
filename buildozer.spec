[app]
title = MyKivyApp
package.name = mykivyapp
package.domain = org.example
source = main.py
source.dir = .
version = 1.0
requirements = python3,kivy
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/presplash.png

[buildozer]
log_level = 2
warn_on_root = 1

[python]
# برای استفاده از فایل‌های پایتون اضافی
# اضافه کردن پوشه‌هایی که کد داخلشونه
# مثلا:
# android.add.source = mylibs

[android]
# تنظیمات اندروید اضافی
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 24
android.ndk_path = $ANDROID_NDK
android.sdk_path = $ANDROID_HOME