#!/bin/bash

# Dependencies
# a) MPI
# b) VRPN
# c) Qt
# d) Python

set -ex
if cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_SHARED_LIBS:BOOL=ON \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr/local/encap/paraview-5.0.1 \
    -DPARAVIEW_AUTOLOAD_PLUGIN_VRPlugin:BOOL=ON \
    -DPARAVIEW_BUILD_PLUGIN_VRPlugin:BOOL=ON \
    -DPARAVIEW_BUILD_QT_GUI:BOOL=ON \
    -DPARAVIEW_ENABLE_PYTHON:BOOL=ON \
    -DPARAVIEW_USE_MPI:BOOL=ON \
    -DPARAVIEW_USE_VRPN:BOOL=ON \
    ../../ParaView; then
echo "ParaView compiled successfully."

make -j 8

make install

echo "Almost all done. Run encap to finalize the installation."

