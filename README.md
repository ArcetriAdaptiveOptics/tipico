# TIPICO: Test Inutile per Provare Inutilmente pliCO


 ![Python package](https://github.com/ArcetriAdaptiveOptics/tipico/workflows/Python%20package/badge.svg)
 [![codecov](https://codecov.io/gh/ArcetriAdaptiveOptics/tipico/branch/main/graph/badge.svg?token=ApWOrs49uw)](https://codecov.io/gh/ArcetriAdaptiveOptics/tipico)
 [![Documentation Status](https://readthedocs.org/projects/tipico/badge/?version=latest)](https://tipico.readthedocs.io/en/latest/?badge=latest)
 [![PyPI version](https://badge.fury.io/py/tipico.svg)](https://badge.fury.io/py/tipico)



tipico is a useless application to test the [plico][plico] environment.


[plico]: https://github.com/ArcetriAdaptiveOptics/plico


## Installation

On the client 

```
pip install tipico
```


On the server 

```
pip install tipico-server
```

The tipico-server package installs also the client package.


### Config files

The server requires to be configured 

The application uses `appdirs` to locate configurations, calibrations 
and log folders: the path varies as it is OS specific. 
Typical paths for config files are: 
   + On OS X `$HOME/Library/Application Support/inaf.arcetri.ao.tipico_server/tipico_server.conf`
   + On Ubuntu `$HOME/.config/inaf.arcetri.ao.tipico_server/tipico_server.conf`
 
The configuration files are copied when the application is first used
from their original location in the python package to the final
destination, where they are supposed to be modified by the user.
The application never touches an installed file (no delete, no overwriting)

The easiest way of checking which config file is used by the server is to start it (see below) and check for the config file name written in the standard output.

Another way of querying the system for config file location is to run python on the server and type:

```
import tipico_server
tipico_server.defaultConfigFilePath
```


The user can specify customized conf/calib/log file path for both
servers and client (how? ask!)


## Usage

### Starting Servers

Starts the 2 servers that control one device each.

```
tipico_start
```


### Using client 

In a Python / IPython shell:


Create a client of the device (suppose the server is running on localhost on port 60010)

```
In [1]: import tipico

In [2]: instr= tipico.instrument('localhost', 60010)
```

Get position and move actuator


```
In [3]: instr.getPosition()
Out[3]: 0

In [6]: instr.moveTo(np.array([42, 3.14]))

In [7]: instr.getPosition()
Out[7]: array([42.  ,  3.14])

```


Get position and move actuator


```

In [8]: status=instr.getStatus()

In [9]: status.actuatorCommands()
Out[9]: array([42.  ,  3.14])

In [10]: status.commandCounter()
Out[10]: 1

In [11]: instr.moveTo(np.array([1, 2]))

In [12]: status=instr.getStatus()

In [13]: status.commandCounter()
Out[13]: 2

In [14]: status.actuatorCommands()
Out[14]: array([1, 2])

In [15]: instr.getPosition()
Out[15]: array([1, 2])

In [16]: instr.getSnapshot('tux')
Out[16]: {'tux.COMMAND_COUNTER': 2, 'tux.SERIAL_NUMBER': '1', 'tux.STEP_COUNTER': 17065}

In [17]: instr.getSnapshot('tux')
Out[17]: {'tux.COMMAND_COUNTER': 2, 'tux.SERIAL_NUMBER': '1', 'tux.STEP_COUNTER': 21225}
```


### Stopping Tipico

To kill the servers run

```
tipico_stop
```

More hard:

```
tipico_kill_all
```



