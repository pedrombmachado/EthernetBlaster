IM software

### Application ###

* IM version: 1.3
* XML2HexLib version: 1.2
* Recommended OS: Ubuntu 16.04 LTS 64 bits
* Python 3.5


### How do I get set up? ###

* sudo apt-get update
* sudo apt-get install build-essential default-jre spyder3
* Download the repository into the target folder
* $ python3 SimulationManager.py

### Contribution guidelines ###

* SimulationManager.py- launch the IM software
* XML2HexApp.py - Perform the convertions from XML to Hex and vice-versa
* downloadManager.py - manages HTTP/TCP clients/servers
* manageCommands.py - manages commands
* ThreadsDef.py - provides the services from the IM server and IMFPGA
* ErrorLog.xml - records the results of all the convertions made usinf the XML2HexApp
* IM.log - logs all the outputs provided by the IM
* fakeData.log - Logs all the fake Neuron (spikes and rtw) and Muscle (forces) results packets that were generated.

### Contacts ###

* Pedro Machado <pedro.baptistamachado@ntu.ac.uk>
* Alicia Costalago Meruelo <alicia.costalagomeruelo@ntu.ac.uk>
* Kofi Appiah <kofi.appiah@ntu.ac.uk>
* Martin McGinnity <martin.mcginnity@ntu.ac.uk>
