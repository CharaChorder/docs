.. _Generative Text Menu (GTM):

Generative Text Menu (GTM)
=============================

The Generative Text Menu (GTM) is a text based menu which can be accessed 
anywhere you type. It allows you to access various device settings and features 
without the need for software.  It's a core feature of CCOS that you will want to 
learn how to use to make the device your own.

.. contents::
   :local:

How to access
*************

First, move your cursor into any area where you can type.  You may want to choose 
somewhere that is innocuous because some programs may respond to the keys of the 
GTM menu. 

.. csv-table::
    :header: "Device", "How to access"

    "CharaChorder One", "Chord both pinky keys north (Alt keys)"
    "CharaChorder Lite", "Chord G and Dup key"
    "CharaChorder X", "Chord G and Esc key"
    "CharaChorder Engine", "Chord G and Esc key"

How to navigate
***************

Once you see the menu (example shown below), you will be able to navigate the menu 
by pressing letters on your device. 

``CharaChorder GTM [ >K<eyboard || >M<ouse || >C<hording || >D<isplay || >R<esources ]``

For example, to access the `Keyboard` submenu you will press the letter `K` as indicated 
by the `>` and `<` that surrounds the `K`.

How to change values
********************

In general, if you find a setting that has a numeric value that you can change 
you will be able to modify this by using the arrow keys on your device. The ``Up arrow`` 
key will increase the value whereas the ``Down arrow`` key will decrease it. Once you are happy 
with a value, you can use the ``Enter`` key to confirm your choice. 

If at any time you want to get out of the menu or discard changes you can press the 
``Esc`` key.  

If you are on a submenu and would like to go back to the previous menu you can 
use the ``Left arrow`` key on your keyboard. 

Available Menus
******************

.. csv-table::
    :header: "Menu", "Description"

    ":ref:`Keyboard<GenerativeTextMenu:Keyboard>`", "Settings related to using your device in character entry"
    ":ref:`Mouse<GenerativeTextMenu:Mouse>`", "Settings related to using your device as a mouse"
    ":ref:`Chording<GenerativeTextMenu:Chording>`", "Settings related to chording on your device"
    ":ref:`Display<GenerativeTextMenu:Display>`","Settings related to your device version and other CCOS texts"
    ":ref:`Resources<GenerativeTextMenu:Resources>`", "A menu of resources, mostly links"

Keyboard
--------

Scan Rate
~~~~~~~~~

The scan rate refers to the frequency at which the device checks the state of the input keys. 
5 ms corresponds to 200 Hz or checking the position of the keys 200 times a second.

Debounce Press / Release
~~~~~~~~~~~~~~~~~~~~~~~~

The debounce press/release settings refer to the time frame (measured in milliseconds) in which to filter out duplicate key activations on a press/release event. In 
other words, any duplicate activations within the given time frame will only be counted once.
The default value on a CharaChorder One is 7 ms while the default on CharaChorder Lite/X is 20 ms.

.. note::
    You might use this setting (by increasing its value) if you are seeing duplicate 
    characters while typing.


Keystroke Delay
~~~~~~~~~~~~~~~

This setting adds a small delay to keystroke inputs. It is measured in microseconds 
and is very small by default. If you have a very fast device, you can decrease this 
value to make chording and GTM menu feel snappier and more responsive.

.. note::
    You might use this setting (by increasing its value) if you are having issues 
    with the GTM menus not working properly on your device. 

Capslock
~~~~~~~~

This setting should be familiar. It toggles the state of the caps lock. When on, all 
characters output by the device will be capitalized.

Operating system
~~~~~~~~~~~~~~~~

This setting can have the value of Windows, Mac, Linux, iOS, or Android.
The intent of this is to provide more accurate key mapping so it is best to set 
this to whatever device you are using.


GUI-CTRL Soft Swap (Lite only)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This setting will swap the behavior of the bottom two keys on the CharaChorder Lite, 
making it so that Ctrl is the bottom left most key and Windows/GUI key is the second one.
Users who are used to normal keyboard layouts will want to take advantage of this 
setting so they don't have to relearn the position of the keys.

Mouse
-----

Poll rate
~~~~~~~~~

The poll rate of the mouse. This is used in conjunction with the slow/fast mouse speed.

Slow speed/fast speed
~~~~~~~~~~~~~~~~~~~~~

The number of pixels to move at the mouse poll rate. In other words, the mouse 
can move 2 pixels every poll rate and if your default poll rate of 20ms (50 Hz) 
then you will move 100 pixels every 1 second.
Slow speed is activated when you use only one of the mouse keys. The fast speed 
is activated when you use both of the mouse keys in the same direction.

Scroll speed
~~~~~~~~~~~~

The scroll is the number of times to scroll at the mouse poll rate. In other words, if the poll rate is 20 ms (50 Hz) then you will scroll 50 times in a second.
If you adjust this value higher you will be able to scroll faster

Active mode
~~~~~~~~~~~

Active mode nudges your mouse cursor one pixel every minute or so (not a specific timing).
This setting can be used to keep your computer from going to sleep. You might turn this setting off if you notice desktop apps are preventing you from getting mobile notifications (for example on Discord or Microsoft Teams).

Chording
--------

Character only mode
~~~~~~~~~~~~~~~~~~~

This setting is a toggle that when turned on will disable chording mode completely.

.. note::
    You might use this setting if you don't expect to want to use chording (perhaps like during gaming) and you want to ensure that you don't accidentally activate any chords.

Press tolerance / Release tolerance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::
    If you only pay attention to one setting in this guide, you should read this one. It is probably the most customized setting on a CharaChorder device.

This is a very important setting to pay attention to and perhaps configure as you use your device and get more experienced. The press and release tolerance refers to a threshold between the first and last press or release of the letters of a chord in order for it to activate.

What this practically means is that if you want to make the window of time larger that you can activate chords in (ie easier) then you will increase these values. This is often helpful for beginners who are just starting to learn how to chord.

The downside to having these values larger is that you will perhaps accidentally trigger chords during normal character entry, so if you are noticing that, you might want to decrease the values.

One thing to point out is that chords with more keys by default get a longer window of time. This means chords with many keys can be a bit easier to trigger because the timing doesn't have to be as exact.

Timeout
~~~~~~~

The time from the last character entry to stop counting characters to replace
You might want to change this if you often find yourself typing a word with chentry (character entry) and then chording after and the word is getting replaced.

Spurring
~~~~~~~~
A 'chording only' mode which tells your device to output chords on a press rather than a press & release. It also enables you to jump from one chord to another without releasing everything. It can provide significant speed gains with chording, but also takes away the flexibility of character entry. Spurring also helps new users learn how to chord by eliminating the need to focus on timing.

Spurring On/Off
^^^^^^^^^^^^^^^

This will turn on or off spurring mode.

Spurring Timeout
^^^^^^^^^^^^^^^^

The time of inactivity to default back to fluid chorded/character entry mode (aka spurring off).

Arpeggiate
~~~~~~~~~~

Arpeggiate inputs are a special set of inputs that can follow chords, such as "I" or "a" and if pressed rapidly after a normal chord they will output the word and a space automatically.

Arpeggiate On/Off
^^^^^^^^^^^^^^^^^

This will turn on or off arpeggiate inputs? or also modifiers

Arpeggiate Timeout
^^^^^^^^^^^^^^^^^^

The time from the last chord, measured in ms, that the device will check for arpeggiates. This includes pressing a modifier after the word to change it.

Display
-------

Version
~~~~~~~

This will show you the current version of the GTM. You can use this to quickly check what version you are running anyhere you can type.

Realtime feedback
~~~~~~~~~~~~~~~~~

Turning this on will show the helpful text like SPURRING_ON, SPURRING_OFF etc.
Most users prefer to leave this on but you can turn it off if you would like.

On startup
~~~~~~~~~~

Turning this on will show the text "CCOS is ready." after you have plugged in your device.
In some cases, you may want to not have it automatically type stuff when plugged in because it can interfere with your system so you can toggle this off.

Color (Lite only)
~~~~~~~~~~~~~~~~~

Use this to change the color of the LEDs on your CharaChorder Lite

Brightness (Lite only)
~~~~~~~~~~~~~~~~~~~~~~

Adjusts the brightness of the LEDs

.. note::
    If you are using a low power usb bank you may draw too much current if you have a high setting and the device might not properly function


Resources
---------

This section contains links which may be helpful to you. These links include: 

.. csv-table::
    :header: "Item", "Description"

    "About", "Opens https://www.charachorder.com/pages/about"
    "Get started", "Opens https://www.charachorder.com/pages/get-started"
    "Discord", "Opens CharaChorder Discord Server"
    "Training", "Opens https://iq-eq.io"
    "Message Riley", "Copies Riley Keen (CharaChorder CEO)'s email address to your clipboard"
    "Learn chords", "Opens The Starter Chord List"
    "System updates", "Opens the CCOS firmware updates page"