# TIPICO: Test Inutile per Provare Inutilmente pliCO

tipico is a useless application to test the [plico][plico] environment.



[plico]: https://github.com/lbusoni/plico


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

```
In [1]: import tipico

In [2]: dm1= tipico.DeformableMirror('AlpaoDM277')

In [3]: dm2= tipico.DeformableMirror('MemsMultiDM')

In [4]: dm1.getSnapshot('boo')
Out[4]: {'boo.COMMAND_COUNTER': 0, 'boo.SERIAL_NUMBER': '1', 'boo.STEP_COUNTER': 45956}

In [5]: dm1.applyZonalCommand(np.ones(277))

In [6]: dm1.getZonalCommand()
Out[6]:
array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
       1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
       1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
       1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
       1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
       1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
       1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
       1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
       1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
       1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
       1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
       1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
       1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
       1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
       1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
       1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
       1., 1., 1., 1., 1.])

In [7]: dm1.getSnapshot('boo')
Out[7]: {'boo.COMMAND_COUNTER': 1, 'boo.SERIAL_NUMBER': '1', 'boo.STEP_COUNTER': 83589}

In [8]: dm2.getSnapshot('tux')
Out[8]:
{'tux.COMMAND_COUNTER': 0,
 'tux.SERIAL_NUMBER': '234',
 'tux.STEP_COUNTER': 95980}
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



