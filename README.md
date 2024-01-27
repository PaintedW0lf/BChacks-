# Hello ARRC People

## Pls downlod this seprately before

1) **Install python 3.11 or less than**
   * We need it to be 3.11 or lower because that is what is compatable pythorch.

2) **Cuda 12.1 (https://developer.nvidia.com/cuda-downloads)**

   * you will face problems because Nvidia sucks so look at this (https://forums.developer.nvidia.com/t/windows-10-cuda-installation-failure-solved/64389)
   * Run the follwing commands in the Vs code terminal assuming it is run as an administration
     * conda install numba
     * conda install cudatoolkit

3) **Creat python virtual enviorment**
   * Run the follwing command:
     * python3 -m venv [insert name you want to give it]
     * close the terminal and then re-opne it to activate or run [name of your venv]\Scripts\activate
  
4) **Install Pytorch using the following link in the venv**
    * https://pytorch.org/
    * choose the follwing options:
      * Stable
      * Your OS
      * pip
      * python
      * Cuda latest version
    * Then copy the command and run in in your VS code terminal (assuming VS code is running as administration)

5) **Run the following command to install all the things that are needed for YOLO V8.**
   * pip install ultralytics


## Pls run the follwing programs before running the code

* checkifGUP.py
  * it should out put the following
    * True
    * 0
    * The GPU you have

- run the following the code to run the code to detect the code
  - python detect_video_stream.py --weights runs/train/yolo_pad_det/weights/best.pt --conf 0.25 -img-size 640 --source 0