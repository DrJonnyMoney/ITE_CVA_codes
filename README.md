# Computer Vision Application Module Supplementary Information
* Some python scripts to help students understand how to control external hardware (LEDs, Buttons, Servos, Distance Sensors, and Motors) using the LEGO Build Hat and Raspberry Pi's GPIO pins.
* Feel free to adpat these codes to build your CVA project.
* When connecting the components to GPIO, please refer to the wiring diagram below:

![circsdfsuit](https://github.com/user-attachments/assets/0527fdda-63a7-4880-b66f-16abd54f72dc)


# Setting up YOLO on your Raspberry Pi 5

### 1. Update and Upgrade Raspberry Pi OS

```bash
sudo apt update
sudo apt full-upgrade
```

### 2. Prepare Your Raspberry Pi

Start with a fresh Raspberry Pi installation and run the following commands to install the required dependencies:

```bash
sudo apt install python3-opencv
sudo apt install libhdf5-dev
```

### 3. Set Up the Virtual Environment  

Create and activate a virtual environment to isolate your project dependencies:  

```bash
python3 -m venv --system-site-packages yolo_project
source yolo_project/bin/activate
```

### 4. Install Python Packages  

With your virtual environment activated, update pip and install the necessary YOLO packages:

```bash
pip install --upgrade pip
pip install ultralytics[export]
pip install ncnn
```
