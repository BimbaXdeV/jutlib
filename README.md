jutlib  v0.1.0
=======
**Easy Python library for downloading anime episodes to user devices from service [jut.su](https://jut.su/anime/).**

Characteristics and functionality
----------------------------------
- Intuitive to use methods ;
- The ability to customize your configuration for the installer with the ability to change: title case, space separator, and resolution quality of the installing video ;
- Test files demonstrating how the library works in several directions in this folder ;
- Ease of integration of the library into your independent projects.
- 
How to start using
-------------------
- First, make sure that your device has **_Python version 3.9_** or higher (using Python several versions lower may be possible, but I can’t tell you about stability) ;
- After that you can start installing the library in your virtual environment (global or local - it doesn’t matter) :

```shell
# for linux
python3 pip install jutsu-downloader

# for windows
pip install jutsu-downloader
```

- After installing the library in the environment, you can start using it for your own purposes ;
- Although the library does not provide such a wide range of functionality compared to collaborations, it does not contain any unnecessary mechanisms and is designed exclusively for its purpose.

Examples of using
------------------
What about documentation without examples? Let's go through the basic methods of this library :

- Initialization :

```python
# import main class from library
from jutsu.downloader import JutSu

# create an instance of the class "JutSu" based on the url you provided
jut = JutSu('YOUR URL TO DESIRED EPISODE')

# load data from the page you received and write it to the class parameters
jut.load()
```

- **Extracting** the video and **installing** it on the device :

```python
jut = JutSu('URL')
jut.load()
jut.download()
```

- For convenience or debugging, if desired, **you can display the received data loaded** into the instance :

```python
jut = JutSu('URL')
jut.load()
print(f'{jut.get_original_name()} : {jut.get_direct_link()}')
```

Features and customizations
----------------------------
**_Editing install configurations_**

- As I mentioned earlier - the library has slight customization **for integration into different projects**. Although the instance already has a configuration set for processes, **you can edit and replace the default values** ;
- To **change the configuration** of settings, the following method is built into the library :

```python
# before:  "Anime Episode Name"
jut.configure(
    download_res=720,  # video quality category
    name_separator='_',  # parameter that will replace all spaces in the episode name
    register_style='upper'  # choose which register the names will be in
)
# after:   "ANIME_EPISODE_NAME"
```

- But as you understand, customization settings also **have their own limits** that you cannot go beyond ;
- I advise you to familiarize yourself with **the list of acceptable settings** for the specified parameters :

```python
download_resolutions = (
    1080,
    720,
    480,
    360
)

name_separators = (
    None  # You can use absolutely any values as separators
)

register_styles = (
    'default',
    'upper',
    'lower'
)
```

**_Editing static episode names_**
- Looking at the principle of operation of this library, one may ask: _"how, instead of the title of the episode loaded by the built-in method from the title on the page, can you give your name under which to install the video?"_ ;
- So, for such cases, there is also a method with which **you can set your name** for the episode in the class instance parameter after loading the page data :

```python
# use "jut.load()" before working with names
jut.set_name('YOUR NAME')
# done, video has heady to downloading
```

- If you need exactly the register in which you specified the new name, do not forget to set the **"default"** register style in the configuration :

```python
jut.configure(register_style='default')
```

- This will help you avoid problems with changing your name during the pre-installation processing.