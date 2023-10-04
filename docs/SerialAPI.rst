Serial API
==========

The Serial API allows users and developers to interact with their CCOS powered device over a serial connection.  This can be used to add and remove chords, change advanced parameters, and perform common commands such as resetting keymaps or resetting the device to factory settings. You can utilize this serial API by using any serial terminal such as `serialterminal.com <https://www.serialterminal.com/>`_ on a `serial enabled web browser <https://caniuse.com/web-serial>`_. The serial connection operates at a baud rate of 115200 bps. In general, a success returns a 0 at the end, while a failure returns a number greater than zero, which represents an error code. When sending Serial API commands to a CharaChorder device, allow for at least 100 microseconds (us) between commands to allow time for the commands to be processed on the device. If there is no time allowed to process commands on the device, then the serial input buffer on the device can fill up and overflow, causing a system crash. Ideally, sequential Serial API commands should be called in a restful manner by waiting for a response from the previous command.

.. figure:: /assets/serial/serialterminal.png
  :alt: Running some simple commands on serialterminal.com

  Running some simple commands on serialterminal.com

.. warning::
   Parameter and keymaps changes, when **committed**, will degrade the flash chip over time (generally a minimum of 10,000 to 25,000 commits are expected to be stable). If you use the commands below, keep in mind that if you accidentally write a program that unnecessarily commits parameters to your device you can wear it out prematurely.  If you plan to programmatically change layouts, for example, you shouldn’t commit the changes unless you need them to persist after power loss. 

   Chords are stored on external flash and have a minimum of 100,000 commits before any degradation could be expected; however, we have a custom wear leveling algorithm that targets specific sectors so this should extend much farther and is less of a concern.

.. note::
   Throughout this document, lines prefixed with a ">" symbol represent user input in the examples shown.

.. contents::
   :local:

Commands Overview
-----------------

Commands are all caps ASCII characters. The return is always one line and includes the command in the return line along with some of the relevant input arguments as well. This makes it more restful and stateless as compared to previous versions of the Serial API. 

.. csv-table::
   :header: "Command", "Description"

   ":ref:`CMD<SerialAPI:CMD>`", "Lists available commands."
   ":ref:`ID<SerialAPI:ID>`", "Identifies device, such as `CHARACHORDER ONE M0`."
   ":ref:`VERSION<SerialAPI:VERSION>`", "Returns the current firmware version, such as `1.1.1`"
   ":ref:`CML<SerialAPI:CML>`", "Used for getting, setting (adding or overwriting), and deleting chordmaps."
   ":ref:`VAR<SerialAPI:VAR>`", "Used for getting and settings parameters; this includes setting custom chordmaps."
   ":ref:`RST<SerialAPI:RST>`", "Restarts/reboots the microcontroller hardware. It has additional arguments for Factory and Bootloader."
   ":ref:`RAM<SerialAPI:RAM>`", "Prints the current amount of SRAM available; this is primarily used for debugging."
   ":ref:`SIM<SerialAPI:SIM>`", "Simulates/injects a chord and outputs the chord output if the chord exists in the chord library; this is primarily used for debugging."

Commands
-----------------
This section covers the various commands, what they expect, what they return, and has examples of how to use them. 

CMD
~~~

The `CMD` command lists out all of the commands in the Serial API. All of the commands are returned in one comma-delimited line. All commands are uppercase ASCII characters.

.. csv-table::
   :header: "I/O","Index","Name","Type","Example","Notes"

   "INPUT",  "0", "Command", "Chars", "CMD"
   "OUTPUT", "0", "Command", "Chars", "CMD"
   "OUTPUT", "1", "Command List", "Chars", "CMD,ID,VERSION,CML,VAR,RST,RAM,SIM","Comma delimited"

Example(s): 

.. code-block:: none

   > CMD
   CMD CMD,ID,VERSION,CML,VAR,RST,RAM,SIM

ID
~~~

The `ID` command returns the ASCII name of the device, including the chipset code. This can be used to identify the correct serial device
attached to the computer.

.. csv-table::
   :header: "I/O","Index","Name","Type","Example","Notes"

   "INPUT","0","Command","Chars","ID",""
   "OUTPUT","0","Command","Chars","ID",""
   "OUTPUT","1","Company","Chars","CHARACHORDER",""
   "OUTPUT","2","Device","Chars","ONE","ONE, LITE, or X"
   "OUTPUT","3","Chipset","Chars","M0","M0 or S2" 

Example(s):

.. code-block:: none

   > ID
   ID CHARACHORDER ONE M0


VERSION
~~~~~~~

The `VERSION` command returns the current version of the CCOS firmware.

.. csv-table::
   :header: "I/O","Index","Name","Type","Example","Notes"

   "INPUT","0","Command","Chars","VERSION",""
   "OUTPUT","0","Command","Chars","VERSION",""
   "OUTPUT","1","Command List","Chars","1.1.1","Period delimited of MAJOR.MINOR.BUILD"

Example(s): 

.. code-block:: none

   > VERSION
   VERSION 1.1.1

CML
~~~

The `CML` command provides access to the Chordmap Library.

.. csv-table::
   :header: "CML SubCommand","Code","Description"

   ":ref:`GET_CHORDMAP_COUNT<SerialAPI:GET_CHORDMAP_COUNT>`","C0","Gets the (decimal) number of chordmaps."
   ":ref:`GET_CHORDMAP_BY_INDEX<SerialAPI:GET_CHORDMAP_BY_INDEX>`","C1","Gets a chordmap by the index number (hexadecimal uint16) if within range."
   ":ref:`GET_CHORDMAP_BY_CHORD<SerialAPI:GET_CHORDMAP_BY_CHORD>`","C2","Gets a chordmap by the chord (hexadecimal) value if it is found in the library."
   ":ref:`SET_CHORDMAP_BY_CHORD<SerialAPI:SET_CHORDMAP_BY_CHORD>`","C3","Sets a chordmap with a chord and output bytes (hexadecimal)."
   ":ref:`DEL_CHORDMAP_BY_CHORD<SerialAPI:DEL_CHORDMAP_BY_CHORD>`","C4","Deletes a chordmap from the library if the chord exists."

GET_CHORDMAP_COUNT
^^^^^^^^^^^^^^^^^^

.. csv-table::
   :header: "I/O","Index","Name","Type","Example","Notes"

   "INPUT","0","Command","Chars","CML",""
   "INPUT","1","SubCommand","Hexadecimal CML Code","C0","Get chordmap count"
   "OUTPUT","0","Command","Chars","CML",""
   "OUTPUT","1","SubCommand","Hexadecimal CML Code","C0",""
   "OUTPUT","2","Data Out","Decimal Number","1347",""

Example(s):

.. code-block:: none

   > CML C0
   CML C0 1347

GET_CHORDMAP_BY_INDEX
^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :header: "I/O","Index","Name","Type","Example","Notes"

   "INPUT","0","Command","Chars","CML",""
   "INPUT","1","SubCommand","Hexadecimal CML Code","C1","Get chordmap by index"
   "INPUT","2","Index","Decimal","522",""
   "OUTPUT","0","Command","Chars","CML",""
   "OUTPUT","1","SubCommand","Hexadecimal CML Code","C1",""
   "OUTPUT","2","Index","Decimal","522",""
   "OUTPUT","3","Chord","Hexadecimal Number","001946418C0000000000000000000000","This will be 0 if index is out of bounds"
   "OUTPUT","4","Phrase","Hexadecimal CCActionCodes List","6361727065206469656D","`carpe diem`; this will be 0 if index is out of bounds"

Example(s):

.. code-block:: none

   > CML C1 522
   CML C1 001946418C0000000000000000000000 6361727065206469656D

GET_CHORDMAP_BY_CHORD
^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :header: "I/O","Index","Name","Type","Example","Notes"

   "INPUT","0","Command","Chars","CML",""
   "INPUT","1","SubCommand","Hexadecimal CML Code","C2","get chordmap by chord"
   "INPUT","2","Chord","Hexadecimal Number","001946418C0000000000000000000000",""
   "OUTPUT","0","Command","Chars","CML",""
   "OUTPUT","1","SubCommand","Hexadecimal CML Code","C2",""
   "OUTPUT","2","Chord","Hexadecimal Number","001946418C0000000000000000000000",""
   "OUTPUT","3","Phrase","Hexadecimal CCActionCodes List","6361727065206469656D","`carpe diem`; this will be 0 if chordmap is not in the library"

Example(s):

.. code-block:: none

   > CML C2 00000000E4E2B0160F84B20ACE7638C0
   CML C2 00000000E4E2B0160F84B20ACE7638C0 6361727065206469656D

SET_CHORDMAP_BY_CHORD
^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :header: "I/O","Index","Name","Type","Example","Notes"

   "INPUT","0","Command","Chars","CML",""
   "INPUT","1","SubCommand","Hexadecimal CML Code","C3","set chordmap by chord"
   "INPUT","2","Chord","Hexadecimal Number","001946418C0000000000000000000000",""
   "INPUT","3","Phrase","Hexadecimal CCActionCodes List","6361727065206469656D","`carpe diem`"
   "OUTPUT","0","Command","Chars","CML",""
   "OUTPUT","1","SubCommand","Hexadecimal CML Code","C3",""
   "OUTPUT","2","Chord","Hexadecimal Number","001946418C0000000000000000000000",""
   "OUTPUT","3","Phrase","Hexadecimal CCActionCodes List","6361727065206469656D","`carpe diem`; this will be 0 if there was a problem adding this chordmap to the library"
   "OUTPUT","4","Success","Boolean Number","0","This will be 0 on success, or greater than zero for an error if the chordmap did not exist or the deletion was unsuccessful"

Example(s):

.. code-block:: none

   > CML C3 00000000E4E2B0160F84B20ACE7638C0 6361727065206469656D
   CML C3 00000000E4E2B0160F84B20ACE7638C0 6361727065206469656D 0

DEL_CHORDMAP_BY_CHORD
^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :header: "I/O","Index","Name","Type","Example","Notes"

   "INPUT","0","Command","Chars","CML",""
   "INPUT","1","SubCommand","Hexadecimal CML Code","C4","delete chordmap by chord"
   "INPUT","2","Chord","Hexadecimal Number","001946418C0000000000000000000000",""
   "OUTPUT","0","Command","Chars","CML",""
   "OUTPUT","1","SubCommand","Hexadecimal CML Code","C4",""
   "OUTPUT","2","Chord","Hexadecimal Number","001946418C0000000000000000000000","This will be 0 if the chordmap did not exist or the deletion was unsuccessful"
   "OUTPUT","3","Success","Boolean Number","0","This will be 0 on success, or greater than zero for an error if the chordmap did not exist or the deletion was unsuccessful"

Example(s):

.. code-block:: none

   > CML C4 00000000E4E2B0160F84B20ACE7638C0
   CML C4 00000000E4E2B0160F84B20ACE7638C0 0

VAR
~~~

The `VAR` command provides access to customizable parameters. This includes access to custom keymaps.

VAR Subcommands
^^^^^^^^^^^^^^^

.. csv-table::
   :header: "VAR SubCommand","Code","Description"

   ":ref:`CMD_VAR_COMMIT<SerialAPI:CMD_VAR_COMMIT>`","B0","Commits any parameter changes to persistent memory."
   ":ref:`CMD_VAR_GET_PARAMETER<SerialAPI:CMD_VAR_GET_PARAMETER>`","B1","Gets the value of a parameter."
   ":ref:`CMD_VAR_SET_PARAMETER<SerialAPI:CMD_VAR_SET_PARAMETER>`","B2","Sets the value of a parameter."
   ":ref:`CMD_VAR_GET_KEYMAP<SerialAPI:CMD_VAR_GET_KEYMAP>`","B3","Gets the value of a key in a keymap."
   ":ref:`CMD_VAR_SET_KEYMAP<SerialAPI:CMD_VAR_SET_KEYMAP>`","B4","Sets the value of a key in a keymap."

Keymap codes
^^^^^^^^^^^^

.. csv-table::
   :header: "Keymap Codes","Code","Description"

   "Primary","A1","The default primary keymap. In the CharaChorder One this is called the Alpha keymap, while on the CharaChorder Lite this defaults to a Qwerty layout."
   "Secondary","A2","The default secondary keymap. In the CharaChorder One this is called the Num-shift keymap, while on the CharaChorder Lite this provides some additional function and numpad keys."
   "Tertiary","A3","The default tertiary keymap. In the CharaChorder One this is called the Function keymap, while on the CharaChorder Lite this is a copy of the secondary keymap."

Parameter codes
^^^^^^^^^^^^^^^

.. csv-table::
   :header: "Parameter Codes","Code","Description"

   "Enable Serial Header","1","boolean 0 or 1, default is 0"
   "Enable Serial Logging","2","boolean 0 or 1, default is 0"
   "Enable Serial Debugging","3","boolean 0 or 1, default is 0"
   "Enable Serial Raw","4","boolean 0 or 1, default is 0"
   "Enable Serial Chord","5","boolean 0 or 1, default is 0"
   "Enable Serial Keyboard","6","boolean 0 or 1, default is 0"
   "Enable Serial Mouse","7","boolean 0 or 1, default is 0"
   "Enable USB HID Keyboard","11","boolean 0 or 1, default is 1"
   "Enable Character Entry","12","boolean 0 or 1"
   "GUI-CTRL Swap Mode","13","boolean 0 or 1; 1 swaps keymap 0 and 1. (CCL only)"
   "Key Scan Duration","14","scan rate described in milliseconds; default is 2ms = 500Hz"
   "Key Debounce Press Duration","15","debounce time in milliseconds; default is 7ms on the One and 20ms on the Lite"
   "Key Debounce Release Duration","16","debounce time in milliseconds; default is 7ms on the One and 20ms on the Lite"
   "Keyboard Output Character Microsecond Delays","17","delay time in microseconds (one delay for press and again for release); default is 480us; max is 10240us; increments of 40us"
   "Enable USB HID Mouse","21","boolean 0 or 1; default is 1"
   "Slow Mouse Speed","22","pixels to move at the mouse poll rate; default for CC1 is 5 = 250px/s"
   "Fast Mouse Speed","23","pixels to move at the mouse poll rate; default for CC1 is 25 = 1250px/s"
   "Enable Active Mouse","24","boolean 0 or 1; moves mouse back and forth every 60s"
   "Mouse Scroll Speed","25","default is 1; polls at 1/4th the rate of the mouse move updates"
   "Mouse Poll Duration","26","poll rate described in milliseconds; default is 20ms = 50Hz"
   "Enable Chording","31","boolean 0 or 1"
   "Enable Chording Character Counter Timeout","32","boolean 0 or 1; default is 1"
   "Chording Character Counter Timeout Timer","33","0-255 deciseconds; default is 40 or 4.0 seconds"
   "Chord Detection Press Tolerance(ms)","34","1-50 milliseconds"
   "Chord Detection Release Tolerance(ms)","35","1-50 milliseconds"
   "Enable Spurring","41","boolean 0 or 1; default is 1"
   "Enable Spurring Character Counter Timeout","42","boolean 0 or 1; default is 1"
   "Spurring Character Counter Timeout Timer","43","0-255 seconds; default is 240"
   "Enable Arpeggiates","51","boolean 0 or 1; default is 1"
   "Arpeggiate Tolerance","54","in milliseconds; default 800ms"
   "Enable Compound Chording (coming soon)","61","boolean 0 or 1; default is 0"
   "Compound Tolerance","64","in milliseconds; default 1500ms"
   "LED Brightness","81","0-50 (CCL only); default is 5, which draws around 100 mA of current"
   "LED Color Code","82","Color Codes to be listed (CCL only)"
   "Enable LED Key Highlight (coming soon)","83","boolean 0 or 1 (CCL only)"
   "Enable LEDs","84","boolean 0 or 1; default is 1 (CCL only)"
   "Operating System","91",":ref:`Operating system codes<SerialAPI:Operating system codes>` listed below"
   "Enable Realtime Feedback","92","boolean 0 or 1; default is 1"
   "Enable CharaChorder Ready on startup","93","boolean 0 or 1; default is 1"


Operating system codes
^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :header: "Operating System Codes","Code"

   "Windows","0"
   "Mac","1"
   "Linux","2"
   "iOS","3"
   "Android","4"
   "Unknown","255"

CMD_VAR_COMMIT
^^^^^^^^^^^^^^

.. csv-table::
   :header: "I/O","Index","Name","Type","Example","Notes"

   "INPUT","0","Command","Chars","VAR",""
   "INPUT","1","SubCommand","Hexadecimal VAR Code","B0","Commit parameters to memory"
   "OUTPUT","0","Command","Chars","VAR",""
   "OUTPUT","1","SubCommand","Hexadecimal VAR Code","B0",""
   "OUTPUT","2","Success","Boolean Number","0","This will be 0 on success, or greater than zero for an error if there was a problem commiting"

Example(s):

.. code-block:: none

   > VAR B0
   VAR B0 1

CMD_VAR_GET_PARAMETER
^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :header: "I/O","Index","Name","Type","Example","Notes"

   "INPUT","0","Command","Chars","VAR",""
   "INPUT","1","SubCommand","Hexadecimal VAR Code","B1","Get parameter value"
   "INPUT","2","Parameter Code","Hexadecimal Parameter Code","2E",""
   "OUTPUT","0","Command","Chars","VAR",""
   "OUTPUT","1","SubCommand","Hexadecimal VAR Code","B1",""
   "OUTPUT","2","Parameter Code","Hexadecimal Parameter Code","2E",""
   "OUTPUT","3","Data Out","Decimal Number","38",""
   "OUTPUT","4","Success","Boolean Number","0","This will be 0 on success, or greater than zero for an error if the VAR Code or Parameter Code doesnt exist"

Example(s):

.. code-block:: none

   > VAR B1 2E
   VAR B1 2E 38 0

CMD_VAR_SET_PARAMETER
^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :header: "I/O","Index","Name","Type","Example","Notes"

   "INPUT","0","Command","Chars","VAR",""
   "INPUT","1","SubCommand","Hexadecimal VAR Code","B2","Set parameter value"
   "INPUT","2","Parameter Code","Hexadecimal Parameter Code","2E",""
   "INPUT","3","Data In","Decimal Number","46",""
   "OUTPUT","0","Command","Chars","VAR",""
   "OUTPUT","1","SubCommand","Hexadecimal VAR Code","B2",""
   "OUTPUT","2","Parameter Code","Hexadecimal Parameter Code","2E",""
   "OUTPUT","3","Data Out","Decimal Number","46","This will be a 00 (double zero) if the VAR Code or Parameter Code doesn't exist or the input value is out of range"
   "OUTPUT","4","Success","Boolean Number","0","This will be 0 on success, or greater than zero for an error if there was a problem"

Example(s):

.. code-block:: none

   > VAR B2 2E 46
   VAR B2 2E 46 0

CMD_VAR_GET_KEYMAP
^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :header: "I/O","Index","Name","Type","Example","Notes"

   "INPUT","0","Command","Chars","VAR",""
   "INPUT","1","SubCommand","Hexadecimal VAR Code","B3","Get keymap parameter value"
   "INPUT","2","Keymap","Hexadecimal Keymap Code","A0",""
   "INPUT","3","Index","Decimal Number","24","For CC1, 0-89 are valid. For CCL, 0-66 are valid."
   "OUTPUT","0","Command","Chars","VAR",""
   "OUTPUT","1","SubCommand","Hexadecimal VAR Code","B3",""
   "OUTPUT","2","Keymap","Hexadecimal Keymap Code","A0",""
   "OUTPUT","3","Index","Decimal Number","24",""
   "OUTPUT","4","Action Id","Decimal Number","111","Valid action Ids range from 8 thru 2047."
   "OUTPUT","5","Success","Boolean Number","0","This will be 0 on success, or greater than zero for an error if either the Keymap Code or Index are out of range."

Example(s):

.. code-block:: none

   > VAR B3 A0 24
   VAR B3 A0 24 111 0

CMD_VAR_SET_KEYMAP
^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :header: "I/O","Index","Name","Type","Example","Notes"
   
   "INPUT","0","Command","Chars","VAR",""
   "INPUT","1","SubCommand","Hexadecimal VAR Code","B4","Set keymap parameter value"
   "INPUT","2","Keymap","Hexadecimal Keymap Code","A0",""
   "INPUT","3","Index","Decimal Number","24","For CC1, 0-89 are valid. For CCL, 0-66 are"
   "INPUT","4","Action Id","Decimal Number","112","Valid action Ids range from 8 thru 2047."
   "OUTPUT","0","Command","Chars","VAR",""
   "OUTPUT","1","SubCommand","Hexadecimal VAR Code","B3",""
   "OUTPUT","2","Keymap","Hexadecimal Keymap Code","A0",""
   "OUTPUT","3","Index","Decimal Number","24",""
   "OUTPUT","4","Action Id","Decimal Number","112","Valid action Ids range from 8 thru 2047. Returns a 00 if either the Keymap Code or Index or Action Id are out of range."
   "OUTPUT","5","Success","Boolean Number","1","This will be 0 on success, or greater than zero for an error if the chordmap did not exist or the deletion was unsuccessful"

Example(s):

.. code-block:: none

   > VAR B2 A0 24 112
   VAR B2 A0 24 112 0

RST
~~~

The `RST` command restarts the CCOS device. This will most likely also break the current Serial connection, and a new connection will need to be made. If the `COMMIT` command has not been called before a `RESTART` command, then the device will revert to the last settings stored in the non-volatile memory.

.. csv-table::
   :header: "I/O","Index","Name","Type","Example","Notes"

   "INPUT","0","Command","Chars","RST",""
   "OUTPUT","0","Command","Chars","RST","Without optional command, this just restarts the device"
   "OUTPUT","1","SubCommand","Chars","BOOTLOADER","See full list of subcommands below"

RST SubCommands
^^^^^^^^^^^^^^^

.. csv-table::
   :header: "RST SubCommand","Notes"

   "RESTART","Restarts the microcontroller."
   "FACTORY","Performs a factory reset of the flash and emulated eeprom. During the process, the flash chip is erased."
   "BOOTLOADER","Restarts the device into a bootloader mode. On a CC1 or CCL M0, the device may be stuck in UF2 bootloader mode until a UF2 file is pasted into the mass storage device. You can copy and paste the UF2 file already in the mass storage device."
   "PARAMS","Resets the parameters to factory defaults and commits."
   "KEYMAPS","Resets the keymaps to the factory defaults and commits."
   "STARTER","Adds starter chordmaps. This does not clear the chordmap library, but adds to it, replacing those that have the same chord."
   "CLEARCML","Permanently deletes all the chordmaps stored in the device memory."
   "UPGRADECML","Attempts to upgrade chordmaps that the system detects are older. This is under development."
   "FUNC","Adds back in functional chords such as CAPSLOCKS and Backspace-X chords."


RAM
~~~

The `RAM` command returns the current number of bytes availabe in SRAM. This is useful for debugging when there is a suspected heap or stack issue.

.. csv-table::
   :header: "I/O","Index","Name","Type","Example","Notes"

   "INPUT","0","Command","Chars","RAM",""
   "OUTPUT","0","Command","Chars","RAM",""
   "OUTPUT","1","Bytes Available","Decimal","425",""


Example(s):

.. code-block:: none

   > RAM
   RAM 425

SIM
~~~

The `SIM` command provides a way to inject a chord or key states to be processed by the device. This is primarily used for debugging.

.. csv-table::
   :header: "I/O","Index","Name","Type","Example","Notes"

   "INPUT","0","Command","Chars","SIM",""
   "INPUT","1","SubCommand","Chars","CHORD","CHORD or KEYSTATE; may change this to Hexadecimal codes"
   "INPUT","2","Data In","Hexadecimal Number","001946418C0000000000000000000000","Chords should be 32 characters"
   "OUTPUT","0","Command","Chars","SIM",""
   "OUTPUT","1","SubCommand","Chars","CHORD",""
   "OUTPUT","2","Data In","Hexadecimal Number","001946418C0000000000000000000000",""
   "OUTPUT","3","Data Out","Hexadecimal CCActionCodes List","6361727065206469656D","`carpe diem`"


Example(s): 

.. code-block:: none

   > SIM CHORD 001946418C0000000000000000000000
   SIM CHORD 001946418C0000000000000000000000 6361727065206469656D

.. code-block:: none

   > SIM CHORD 00000000E4E2B0160F84B20ACE7638C0
   SIM CHORD 00000000E4E2B0160F84B20ACE7638C0 0 # Returns a 0 if there is no chordmap in the library



Chord Construction
------------------

There are 128-bits in a chord. The first 8 bits will typically be 0x00, as this byte value is used to store an index value for chordmaps where the chord output is longer than what can be stored in memory in a single chordmap, which has 192 bytes allocated per memory entry.

The next 120-bit bits are segmented into twelve 10-bit chunks. Each 10-bit value is a 10-bit CC action code. While CC action codes can reference up to 13-bits, only up to 10-bit values can be used for key inputs. The key inputs for a chord are sorted in descending order from greatest in value to least in value.

.. csv-table::
   :header: "","Chain Index", "Key 1", "Key 2", "Key 3", "Key 4", "Key 5", "Key 6", "Key 7", "Key 8", "Key 9", "Key 10", "Key 11", "Key 12"
   :widths: 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10

   "bits", "8 bits", "10 bits", "10 bits", "10 bits", "10 bits", "10 bits", "10 bits", "10 bits", "10 bits", "10 bits", "10 bits", "10 bits", "10 bits"
   "example 1", "0", "w", "r", "o", "l", "d", "", "", "", "", "", "", ""
   "decimal 1", "0", "119", "114", "111", "108", "100", "0", "0", "0", "0", "0", "0", "0"
   "example 2", "0", "DUP", "t", "m", "", "", "", "", "", "", "", "", ""
   "decimal 2", "0", "536", "116", "109", "0", "0", "0", "0", "0", "0", "0", "0", "0"

Note that yes it is possible to use the same CC action code multiple times for keys in a chord, but these chords cannot be activated unless the device's keymap has more than one instance of the same CC action code assigned to more than one of the keys on the A1 keymap layer.

If a chord is attempted to be formed by more than 12 keys, then the smallest key values after being sorted should be truncated to just 12 values. This chord bit structure can not support more than twelve 10-bit keys.
Most chords will have trailing zeros.

To use these chords with the Serial API, they should be converted to a 16-character hexadecimal representation.
