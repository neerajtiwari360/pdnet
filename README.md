# pdnet

## Visualization and Analysis Tools
- **Netron**: Visualize neural network models. [Netron Website](https://netron.app/)

## Docker Usage
Build the ONNX to C converter image:
```bash
docker build -t onnx2c-converter .
```

For Windows, run the converter in a Docker container:
```bash
docker run -it -v ${PWD}:/local_directory onnx2c-converter:latest /bin/bash
```

Convert an ONNX model (`mnist.simplified.onnx`) to C code:
```bash
docker run -it -v ${PWD}:/local_directory onnx2c-converter:latest onnx2c mnist.simplified.onnx > test.c
```

## Reference
- [PIDNet](https://github.com/XuJiacong/PIDNet/tree/main)
- [ONNX2C](https://github.com/kraiskil/onnx2c)