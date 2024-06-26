# Use a base image with the necessary build tools
FROM ubuntu:22.04

# Set environment variables to non-interactive to avoid prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    libprotobuf-dev \
    protobuf-compiler \
    gcc-arm-none-eabi \
    openocd \
    libusb-1.0-0-dev \
    python3 \
    python3-pip \
    && apt-get clean

# Install Python dependencies
RUN pip3 install onnx

# Set the working directory
WORKDIR /app

# Clone the onnx2c repository
RUN git clone https://github.com/kraiskil/onnx2c.git

# Initialize and update submodules
WORKDIR /app/onnx2c
RUN git submodule update --init

# Build onnx2c
RUN mkdir build && cd build && \
    cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_FLAGS="-Wno-error=array-bounds" .. && \
    make onnx2c

# Set the PATH environment variable to include onnx2c
ENV PATH="/app/onnx2c/build:${PATH}"

# Create a directory for the ONNX model
RUN mkdir /app/onnx_models

# Copy your ONNX model into the container
# The model file should be named "model.onnx"
# COPY model.onnx /app/onnx_models/

# # Run onnx2c on the provided ONNX model
# RUN onnx2c /app/onnx_models/model.onnx /app/model.c

# Expose any necessary ports (if required)
# Example: EXPOSE 3333 for OpenOCD
EXPOSE 3333

# Command to keep the container running
CMD ["tail", "-f", "/dev/null"]
