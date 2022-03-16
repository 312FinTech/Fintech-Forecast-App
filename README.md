# Fintech-Forecast-App
A [Kivy](https://kivy.org/#home) app that uses ML/DL to forecast input ticker symbols and returns a chart of the forecast. Kivy can be deployed on Android, iOS, MacOS, Windows, & Linux OS's.

Beta v1.0

![](images/v1_chart_return_1.gif)

BTC Forecast Using FB Prophet
![](images/newplot.png)

# Plan
![](images/Project_Plan.png)

## Install Guide
To [install Anaconda](https://www.anaconda.com/products/individual) on linux:
```
wget https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh
bash Anaconda3-2021.11-Linux-x86_64.sh
```
Feel free to use [mamba](https://anaconda.org/conda-forge/mamba) instead of conda.
```
conda install mamba -n base -c conda-forge
```
### Full Install
If you are using a Linux system make sure you have `gcc`, `g++`, `build-essential`, `python-dev`, and `python3-dev` installed using a package manager or other means.  
```
conda activate base
conda create --name forecastappenv python=3.8.8 -y
conda activate forecastappenv
conda install kivy -c conda-forge -y
yes | pip install yfinance 
conda install -c conda-forge gcc -y
conda install -c plotly plotly -y
conda install -c conda-forge prophet -y
conda install -c anaconda django -y
conda install -c conda-forge jupyterlab -y
```
If you get and error for the `install gcc` use these commands then:
```
conda activate base
conda create --name forecastappenv python=3.8.8 -y
conda activate forecastappenv
conda install kivy -c conda-forge -y
yes | pip install yfinance numpy matplotlib pandas
pip install pystan==2.19.1.1 
conda install -c plotly plotly -y
conda install -c conda-forge prophet -y
conda install -c anaconda django -y
conda install -c conda-forge jupyterlab -y
```
### Kivy Install
```
conda activate base
conda create --name forecastappenv python=3.8.8 -y
conda activate forecastappenv
conda install -c anaconda ipykernel -y
ipython kernel install --user --name=forecastappenv
conda install kivy -c conda-forge -y
```
Run `main.py` in repo dir:
```
python main.py
```
To run Kivy demo app:
```
python ~/anaconda3/envs/forecastappenv/share/kivy-examples/demo/showcase/main.py
```
*Use this command to find the file if you can't locate it on your local machine:
(if using gitbash, try this `/c/ProgramData/Anaconda3/envs/forecastappenv/share/kivy-examples/demo/showcase/main.py` path instead)
```
sudo find / -type d -name '*kivy-examples*'
```

## Ezekial Pack (FB Prophet)
### Installation
If you are using a Linux system make sure you have `gcc`, `g++`, `build-essential`, `python-dev`, and `python3-dev` installed using a package manager or other means.  
```
conda activate base
conda create --name forecastappenv python=3.8.8 -y
conda activate forecastappenv
yes | pip install yfinance 
conda install -c conda-forge gcc -y
conda install -c plotly plotly -y
conda install -c conda-forge prophet -y
conda install -c anaconda django -y
conda install -c conda-forge jupyterlab -y
```
```
mamba activate base
mamba create --name forecastappenv python=3.8.8 -y
conda activate forecastappenv
yes | pip install yfinance 
mamnda install -c conda-forge gcc -y
mamba install -c plotly plotly -y
mamba install -c conda-forge prophet -y
mamba install -c anaconda django -y
mamba install -c conda-forge jupyterlab -y
```
## Django REST API Endpoints
[To be used with 312Server.](https://medium.com/swlh/build-your-first-rest-api-with-django-rest-framework-e394e39a482c
)


### Methods [(see `yahooprophet.py`)](ezekial/yahooprophet.py)
```
class YahooProphet:
    """Class that accepts a yahoo finance `yf_ticker`, `start_date` (yyyy-dd-mm), `forecast_ahead`
    Used with `forecast_df()`, `plot()`, `plotly_plot()`, & `forecast_all()` methods. For more info on FB Prophet visit.
    https://facebook.github.io/prophet/docs/quick_start.html#python-api"""
```
```
def forecast_all(self):
    """Returns a Facebook Prophet dataframe and forecast charts."""
```
```
def forecast_df(self):
    """Returns a Facebook Prophet dataframe."""
```
```
def plot(self):
    """Returns 4 charts on forecast of input pandas series."""
```
```
def plotly_plot(self):
    """Returns plotly plot of forecasted pandas series."""
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

## [Creating Package for Windows](https://kivy.org/doc/stable/guide/packaging-windows.html)
### Installation
```
conda activate forecastappenv
conda install -c conda-forge pyinstaller -y
```
