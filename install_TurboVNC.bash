#!/bin/bash

# To install TurboVNC, we need to install some dependencies first
# The first one is libjpeg-turbo SDK - https://github.com/libjpeg-turbo/libjpeg-turbo

# Clone the libjpeg-turbo SDK repo from GitHub
git clone https://github.com/libjpeg-turbo/libjpeg-turbo.git

echo "Make sure you have autoconf 2.56 or later, automake 1.7 or later,
nasm or yasm, JDK or OpenJDK"

# Check if yasm or nasm installed
NASM=
if 
sudo apt-get install yasm

# Building libjpeg-turbo
# Go to the source files
cd libjpeg-turbo
autoreconf -fiv
# Make a build directory
mkdir build01 && cd build01
# Find the path of JNI_CFLAGS
JNI_H="$(locate include/jni.h)"
JNI_DIR=$(dirname "${JNI_H}")
sh ../../libjpeg-turbo/configure JNI_CFLAGS='-I$JNI_DIR -I$JNI_DIR/linux' --with-pic --with-java
# Make the file
if make -j 4; then
    echo "Successfully built libjpeg-turbo"
else
    echo "Build failed. Look for errors."
fi

