# Fintech-Forecast-App
A mobile app that uses ML/DL to forecast input ticker symbols and returns a chart of the forecast.

## Install Guide
To install Anaconda on linux:
```
curl https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh
bash Anaconda3-2021.11-Linux-x86_64.sh
```


```
conda create --name forecastappenv python=3.8.8 -y
conda activate forecastappenv
conda install -c anaconda ipykernel -y
ipython kernel install --user --name=forecastappenv
conda install kivy -c conda-forge -y
```
Install kivy in python shell (can run in notebook as well):
```
python
import kivy
exit()
```
Run `main.py` in repo dir:
```
python main.py
```


Run demo app:
```
python ~/anaconda3/envs/forecastappenv/share/kivy-examples/demo/showcase/main.py
```
*Use this command to find the file if you can't locate it on your local machine:
(if using gitbash, try this `/c/ProgramData/Anaconda3/envs/forecastappenv/share/kivy-examples/demo/showcase/main.py` path instead)
```
sudo find / -type d -name '*kivy-examples*'
```

## [Creating Package for Android](https://kivy.org/doc/stable/guide/packaging-android.html)

Edit this line in the `buildozer.spec` file.
```
p4a.branch = develop
```
Use the Adroid Device Bridge if needed (i.e. WSL):
(USB Debugging must be enabled in devoloper options by tapping the build number 5 times in the settings menu)
```
/mnt/c/Users/mchar/Downloads/platform-tools_r33.0.0-windows/platform-tools/adb.exe devices
````
* can add adb to environmatal variables (use `sudo apt install adb` for linux)
Compile the app using:
(this takes a long time!)
```
buildozer -v android deploy run
```
or
```
buildozer android debug deploy run
```
If it compiles successfully and doesn't upload to your device start a local host server by:
```
buildozer serve
```
It will tell you a port number and you can access it your browser by doing a `localhost:THE_PORT_NUMBER_HERE`, then download the `.apk` file and transfer it to your device.

Or you can just access it from the project dir where it should be located after successfully compiling.
