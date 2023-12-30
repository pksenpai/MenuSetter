# menu setter 3
A dynamic menu for easier customization by json.
<br>
This module is under development and will become more powerful.

## How To Use? 🍡
> you can use this with 4 easy steps

_____________________
1. ### Installation

<br>

- install with pip package manager([pypi](https://pypi.org/project/menu-setter3/)) in cmd or terminal:
```
pip install menu_setter3 
```

<br>

_____________________
2. ### Initialization

<br>

- init config files with following command:
```
python3 -m menu_setter ms-init
```

<br>

> [!TIP]
>  If the `ms_config` directory exists but the json file does not exist, use `-j` option to create a ready-made menu template in Jason format:
> <br>
> ```python3 -m menu_setter ms-init -j```

<br>

<details>
<summary><b>More Commands & Options</b></summary>

<br>

- ### Commands
| Commands | Usage |
| :--- | ---: |
| ms-init | initialize the ms_config directory <br>for configuration menu |
| ms-show | xxxxxxxx |     
| ms-call | xxxxxxxx |

- ### Optionals
| Related command | Options       | Usage |
| :---            | :---:         | ---:  |
| ms-init         | -n <br>--name     | default menu header name is "Main Menu". <br>you can use '-n' or '--name' for change header name.|
| ms-init         | -j <br>--json     | If the `ms_config` directory exists but the json file does not exist, <br>use `-j` option to create a ready-made menu template in Jason format |
| ms-call <br>ms-show | -v <br>--verbose | Show with More details |



</details>
<br>

## How To Dev?
...
