# Fintech-Forecast-App
A mobile app that uses ML/DL to forecast input ticker symbols and returns a chart of the forecast.

## Install Guide
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


## {Creating Package for Android](https://kivy.org/doc/stable/guide/packaging-android.html)


```
