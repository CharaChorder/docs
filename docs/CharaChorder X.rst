CharaChorder X
=======================================

Welcome to the Official CharaChorder X guide.

.. _CCX:
.. image:: /assets/images/CCX.png
  :width: 1200
  :alt: CharaChorder X

The CharaChorder X is a plug-and-play device that serves as a middle-man between your keyboard and your computer. It allows any keyboard to have :doc:`chording<Chords>` capabilities. Essentially, the CharaChorder X is a supersuit for your keyboard that will give it the power of :doc:`chording<Chords>`. 

What is :doc:`chording<Chords>`? Put simply, :doc:`chording<Chords>` is the action of pressing and releasing multiple keys at once to get a predetermined output. For example, we can press `b` and `c` simultaneously, and quickly release them, also simultaneously, to get the word "because". This enables you to type one word at a time, instead of one letter at a time.

Although the CharaChorder X is a very powerful device, it is limited by the keyboard that you use it with. One example of this is that :doc:`chording<Chords>` relies on your keyboard's :doc:`rollover<Glossary>` limits. A keyboard with 3-key rollover (3KRO) will not be able to make use of :doc:`chords<Chords>` that use more than 3 keys in their :doc:`input<Chords>`. We recommend using a keyboard with N-key rollover (NKRO) for best results. Feel free to choose from the list below to read the topics that you find relevant.

.. contents::
   :local:

Out of the Box
**************

Parts
-----

When you first receive your CharaChorder X, it will come in a black
box with the CharaChorder logo on the outside. Once you open the box,
you’ll find your brand new CharaChorder X inside, safely tucked inside a cardboard cutout.
You will also find an insert that gives instructions on how to connect the CharaChorder X to your computer. On that reference guide, you will also find a link to our site which contains valuable resources to help you get started.

.. _CCX in the box:
.. image:: /assets/images/CCXinBox.png
  :width: 1200
  :alt: CharaChorder X in its Box


The Body
~~~~~~~~

The CharaChorder X is a single piece comprised of a circuit board which is enclosed in an injection molded plastic shell. It has a single female USB-A port, and a single male USB-A connector. You can find the dimensions of the CharaChorder X in the table below.

.. list-table:: CharaChorder X Dimensions
   :widths: 25 25 25 25
   :header-rows: 1

   * - 
     - Length
     - Width
     - Height
   * - **Shell**
     - 59 mm (5/16 in)
     - 23.25 mm (15/16 in)
     - 16.15 mm (5/8 in)
   * - **Shell + Connector**
     - 71.5 mm (2 7/8 in)
     - 23.25 mm (15/16 in)
     - 16.15 mm (5/8 in)


Connections
------------

Your new CharaChorder X comes with two connections: a female USB-A port, and a male USB-A connector. The CharaChorder X draws power from your computer via the USB-A male connector and passes on power as well as communicates with your keyboard through the female USB-A port.


Plugging In
-----------

The CharaChorder X is plug-and-play, so it doesn’t require any
additional software to work. 

.. warning::
   IMPORTANT: During your first time plugging your CharaChorder in,
   and every time thereafter when you have :ref:`realtime feedback<GenerativeTextMenu:Realtime Feedback>`
   enabled, it’s recommended
   that you have your cursor in a blank typing space. The CharaChorder
   has a welcome message that can send instructions to your computer
   that are not intended by the user. This feature can be disabled in
   the :doc:`GTM<GenerativeTextMenu>`. 

Take the male USB-A connector from your keyboard and plug it into the CharaChorder X's female USB-A port. After that, take the male USB'A connector on the CharaChorder X and plug it into a female USB-A port on your computer. 

Upon connecting, you may notice the
following things:

- If your cursor is somewhere where text can be entered: You will first see the text “Loading ### Chordmaps” highlighted, and a few moments later, “CCOS is ready.”
 
- Regardless of whether or not your cursor is somewhere where text can be entered: You will be able to see a small, red colored light inside the shell of the CharaChorder X.

If you have :ref:`realtime feedback<GenerativeTextMenu:Realtime Feedback>` enabled, once you can see the highlighted text that reads
“CCOS is ready”, your device is ready to be used.

.. note::
   IMPORTANT: :ref:`Realtime feedback<GenerativeTextMenu:Realtime Feedback>` is enabled by default on new CharaChorder devices.

Getting Started
***************

There are a few steps that you’ll likely want to take if this is your
first time using your CharaChorder device. In the following section, we
will update your device, explain navigation in the :doc:`GTM<GenerativeTextMenu>`, and demonstrate the default layout on your new
device. 

Updating your Device
--------------------

Checking your Device’s Firmware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can check your device’s current firmware by following the steps
below: 

#. On a chromium based browser, such as Chrome, go to the CharaChorder `Device Manager <https://charachorder.io/config/layout/>`__ 
#. Click “Connect” 
#. When the popup box comes up that reads “charachorder.io wants to connect to a serial port”, choose your CharaChorder device, then click the blue “connect” button

After following the above steps, you can find your
firmware version right above the “Connect” button. It will read
something like this:

``CHARACHORDER X S2 --- Version 1.1.3``

.. _CCX Firmware Check:
.. image:: /assets/images/DMFW-CCX.png
  :width: 295
  :alt: Checking the firmware on Device Manager

Updating the Firmware
~~~~~~~~~~~~~~~~~~~~~

If you find that your device is not running the latest firmware version,
you can follow the steps below to update your device. You can check
which is the latest firmware release by visiting `this
site <https://www.charachorder.com/pages/update-your-firmware>`__. 

.. warning::
   **IMPORTANT**: Before performing the below steps, please make sure that you have a :ref:`backup of your layout<Device Manager:Backups>`      as well as a :ref:`backup of your chord library<Device Manager:Backups>`. The update might reset those, so it's important that you    keep backup files handy. For instructions on how to restore backed up files, visit the :ref:`Backups<Device Manager:Restoring from a Backup>`    section. The update might also reset some of your :doc:`GTM<GenerativeTextMenu>` settings. Be sure to write    down settings before you update.

#. On a chromium based browser, such as Chrome, go to the CharaChorder `Device Manager <https://charachorder.io/config/layout/>`__ 
#. Click “Connect”
#. When the popup box comes up that reads “charachorder.io wants to connect to a serial port”, choose your CharaChorder device, then click the blue “connect” button
#. _`Click` “Boot Menu” (the power icon) followed by “Bootloader”. Your CharaChorder will now appear as an external storage device on your computer’s file explorer or Finder app. It might be named one of the following: “TinyUSB”, “TinyUSB CDC”, or “CharaChorder X”.
#. Download your update file from this site: `<https://www.charachorder.com/pages/update-your-firmware>`__

.. warning::
   **IMPORTANT**: Make sure that the file you download is named exactly
   like this: CURRENT.UF2 . If there are any other characters in the
   file name, the file will not work. “CURRENT.UF2(1)” will NOT work.
   Additionally, the file name is case sensitive; all letters must be
   capitalized.

6. Copy the CURRENT.UF2 file that you just downloaded and paste it into the CharaChorder drive that we found in :ref:`step 4<Click>`
7. When your computer asks you how you would like to resolve the issue of two files with the same name, select “Replace file”.

At this point, your CharaChorder X will automatically reboot and the
CharaChorder drive will have disappeared. Congratulations! You have
successfully updated your device. You can check your device’s firmware
version by following the steps :ref:`here<CharaChorder X:Checking your Device’s Firmware>`.

Understanding the Settings
--------------------------

The CharaChorder X has settings that are user-configurable. Since the
device is plug-and-play, you don’t need any software to edit the
device’s settings; all you need is a place to type text. We call these
settings the Generative Text Menu, or GTM for short.

You can access the :doc:`GTM<GenerativeTextMenu>` by
:doc:`chording<Chords>` the `ESC` key and the letter `g` **(G + ESC)** in any space that
allows text entry such as a notepad app. For an explanation on chords
and how to perform them, visit the :doc:`Chords<Chords>` section.

.. warning::
   **A bug currently exists on Windows 11 default Notepad app where chording doesn't load correctly. We are looking into this, but, for now, we recommend using a different app.** 

Once you perform the chord to call up the :doc:`GTM<GenerativeTextMenu>`, your CharaChorder will type out the menu and its options.
It will look something like this:


``CharaChorder GTM [ >K<eyboard || >M<ouse || >C<hording || >D<isplay || >R<esources ]``

Navigation around this menu is based on letter-presses. In the example
above, you can select the desired submenu by pressing the letter between
the angle brackets (for example: ``>K<``) in your target submenu on your
CharaChorder One. In the example above, you would press ``K`` for
Keyboard, ``M`` for Mouse, ``C`` for Chording, ``D`` for Display, and
``R`` for Resources.

In some submenus, you will see numeric values. In order to increase or
decrease these, you can use the up and down arrow keys on your keyboard.

``CharaChorder > Chording > Press Tolerance [ Use up/down arrow keys to adjust: 25ms ]``

You can read an explanation on all of the settings on your CharaChorder device :doc:`here<GenerativeTextMenu>`.

The Layout
-------------

The CharaChorder X uses your keyboard's layout, so you don't have to learn a new one. The CharaChorder X reads the keycodes that your keyboard sends and makes use of them to produce outputs on your computer. The only drawback to this is that the CharaChorder X is unable to read keypresses that do not send a code. One common key that doesn't send a code is the Fn key. This key serves as a layer-access key, locally on your keyboard, that allows you to reach the F-keys. Although the CharaChorder X is unable to read the Fn keypress, the F-keys (F1-F24) will send out a keycode, and, thus, the CharaChorder X will send out that signal to the computer. 

Additionally, the CharaChorder X enables you to make use of two extra layers as well. In order to reach those layers, you will have to :ref:`remap<Device Manager:Remapping>` your keyboard to include the layer access keys. Nonetheless, you can continue reading below to learn how the layers work on the CharaChorder X.

Layers
~~~~~~

The CharaChorder X has 3 layers: the base layer called the A1 layer,
the secondary layer referred to as A2, and the tertiary layer named A3.
Since the CharaChorder makes use of your keyboard's layout, the layer feature makes it so that you can potentially triple the number of keys you have access to.

A1 Layer
^^^^^^^^

The A1 layer is the main layer that is active by default. You can access all of the keys on your keyboard without having to hold or press anything
else. This is the main layer. Your CharaChorder-connected keyboard will always be in the A1 layer upon boot.

While the A1 layer is active on the CharaChorder X by default, you can
map the A1 access key, which bears the name “Primary Keymap (Left)” or “Primary Keymap (Right)”, on the
`Device Manager <https://charachorder.io/config/layout/>`__.

A2 Layer
^^^^^^^^

The A2 layer, sometimes referred to as the “number layer”, is accessible
with the :doc:`A2 access key<CharaChorder Keys>`. This key is NOT mapped on your CharaChorder X by default, because the CharaChorder X uses your keyboard's layout. In the `Device Manager <https://charachorder.io/config/layout/>`__,
this key has the name “Numeric Layer (Left)” and “Numeric Layer (Right)”.

Any key that is on the A2 Layer can only be accessed by pressing and
holding the A2 Layer access key along with the target key. You do not
need to :doc:`chord<Chords>` the keys together; it’s only required that the
A2 Layer access key is pressed while the target key is pressed.

A3 Layer
^^^^^^^^

The A3 layer, sometimes referred to as the “function layer”, is
accessible with the :ref:`A3 access key<CharaChorder Keys>`. This key is NOT mapped on your CharaChorder X by default, because the CharaChorder X uses your keyboard's layout. In the `Device Manager <https://charachorder.io/config/layout/>`__,
this key has the name “Function Layer (Left)” and “Function Layer (Right)”.

Any key that is on the A3 Layer can only be accessed by
pressing and holding the :doc:`A3 access key<CharaChorder Keys>`,
along with the target key. You do not need to :doc:`chord<Chords>` the keys
together; it’s only required that the A3 layer access key is pressed
while the target key is pressed.

Shift Modifier
^^^^^^^^^^^^^^

On top of the three aforementioned layers, the :doc:`Shift key<CharaChorder Keys>`, which is a :doc:`modifier<Glossary>`, can be used to access some extra keys. The Shift keypress works just like it
would on a traditional keyboard. You can capitalize letters and access
symbols attached to numbers. This works with any key on any layer, just
like other modifiers (such as CTRL and ALT). The Shift modifier output
is currently controlled by the Operating System that your CharaChorder is
plugged to, and it is not possible to customize their outputs.

In the `Device Manager <https://charachorder.io/config/layout/>`__,
this key has the name “Shift Keyboard Modifier (Left)” and “Shift Keyboard Modifier (Right)”, one for each side
of the keyboard. 

The Shift is accessible by pressing the key labeled "Shift" on your keyboard. Any key
that requires the Shift Modifier can only be accessed by pressing and
holding the Shift key along with the target key. You do not need to
:doc:`chord<Chords>` the keys together; it’s only required that the Shift
key is pressed while the target key is pressed.

Configurability
~~~~~~~~~~~~~~~

You can change the layout of your keyboard while it's connected to the CharaChorder X, which means that you can
:doc:`remap<Glossary>` almost all keys. Some users may
choose to :doc:`remap<Glossary>` their device’s layout to accommodate missing keys, such as the :doc:`DUP key<CharaChorder Keys>`. For a thorough explanation on how remapping
works and how to remap your device, visit the :ref:`remapping section<Device Manager:Remapping>` 

Practice
~~~~~~~~

Now that you’re familiar with your new CharaChorder device, it’s time to
use it! Head over the the :doc:`training section<Tools>` for instructions
on how to get started with learning your device. If you want to just
jump in without having to read a minute longer, head on over to our
training website; https://www.iq-eq.io/#/

.. _Dot I/O:
.. image:: /assets/images/DOTIOL.png
  :width: 1200
  :alt: Practicing on DOT I/O
