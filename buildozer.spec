[app]

# نام اپلیکیشن
title = MyKivyApp

# نام فایل اصلی برنامه‌ات
source = main.py

# بسته منحصربه‌فرد برای اپلیکیشن (مثل آدرس ایمیل برعکس)
package.name = mykivyapp
package.domain = org.example

# نسخه اپلیکیشن
version = 1.0

# آیا از فایل .kv استفاده می‌کنی؟
use_kivy_settings = False
include_exts = py,kv,png,jpg,json

# آیکون اپلیکیشن (اختیاری)
icon.filename = %(source.dir)s/icon.png

# دایرکتوری‌هایی که داخل APK قرار می‌گیرند
source.include_exts = py,kv,png,jpg,json
presplash.filename = %(source.dir)s/splash.png

# زبان‌ها و ورژن‌های مورد استفاده
requirements = kivy

[buildozer]

# پلتفرم هدف (برای اندروید)
target = android

# مقدار خروجی
log_level = 2
