import usb
import usb.backend.libusb1

backend = usb.backend.libusb1.get_backend(find_library=lambda x: "/usr/local/Homebrew/Cellar/libusb/1.0.28/lib/libusb-1.0.dylib")

if backend is None:
    print("No backend available")
else:
    devices = usb.core.find(find_all=True, backend=backend)
    if devices is None:
        print("No USB devices found")
    else:
        for dev in devices:
            print(dev)

