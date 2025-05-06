# 安装依赖

```bash
pip3 install pyusb -i https://mirrors.aliyun.com/pypi/simple/
```

# 如果没有反应

将 `90-odrive.rules` 放到 `/etc/udev/rules.d` 下

然后：

```bash
sudo udevadm control --reload-rules
sudo udevadm trigger
```

# for macos

```bash
brew install libusb
```

修改 backend

```diff
diff --git a/fibre/usbbulk_transport.py b/fibre/usbbulk_transport.py
index 23015f3..ee8d602 100755
--- a/fibre/usbbulk_transport.py
+++ b/fibre/usbbulk_transport.py
@@ -9,6 +9,8 @@ import fibre.protocol
 import traceback
 import platform
 from fibre.utils import TimeoutError
+import usb^M
+import usb.backend.libusb1^M
 
 # Currently we identify fibre-enabled devices by VID,PID
 # TODO: identify by USB descriptors
@@ -188,7 +190,8 @@ def discover_channels(path, serial_number, callback, cancellation_token, channel
 
   while not cancellation_token.is_set():
     logger.debug("USB discover loop")
-    devices = usb.core.find(find_all=True, custom_match=device_matcher)
+    backend = usb.backend.libusb1.get_backend(find_library=lambda x: "/usr/local/Homebrew/Cellar/libusb/1.0.28/lib/libusb-1.0.dylib")^M
+    devices = usb.core.find(find_all=True, custom_match=device_matcher, backend=backend)^M
     for usb_device in devices:
       try:
         bulk_device = USBBulkTransport(usb_device, logger)
```
