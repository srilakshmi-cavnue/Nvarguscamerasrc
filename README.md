# Nvarguscamerasrc

- To obtain this source code, download and extract the L4T 35.4.1 BSP sources folder. Inside /Linux_for_Tegra/source/public folder, extract the `gst-nvarguscamera_src.tbz2` tarball.
- Follow [README.txt](https://github.com/srilakshmi-cavnue/Nvarguscamerasrc/blob/main/gst-nvarguscamera/README.txt) to install the required debians.
- Quick steps for installation -
```
sudo apt-mark unhold libgstreamer-plugins-good1.0-0 libgstreamer-plugins-good1.0-dev gstreamer1.0-plugins-good gir1.2-gst-plugins-base-1.0 liborc-0.4-0
sudo apt-get install libgstreamer1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good liborc-0.4-dev libgstreamer-plugins-base1.0-dev libegl1-mesa-dev
```
- Run `make` to build and compile the new source code and `make install` to install the new libgstnvarguscamerasrc.so file. 
- Reference [here](https://github.com/Cavnue/jetson-l4t-kernel/commit/2d70be13383455e0c0f66e9cf4d1a3db60d77eac) for previous timestamp investigation results.
