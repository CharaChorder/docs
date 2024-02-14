Device Manager
======================================

The CharaChorder Device Manager is the one-stop-shop for users with a CCOS-powered device. It boasts high quality graphics, animations and a simple user interface. On the device manager, you can change your device's :ref:`layout<Device Manager:Layout Editor>`, manage your :ref:`chord library<Device Manager:Chord Manager>`, adjust your :ref:`settings<Device Manager:Settings Menu>`, and even send :doc:`serial commands<SerialAPI>` to your device.

In this section, we'll talk about the device manager and how you can navigate around it to configure your device to your liking. First, we'll discuss the website and where to find useful buttons on it, then we'll cover the three main pages on the device manager and how to use them, and, lastly, we'll touch upon some other features and useful tools on the manager. 

Feel free to use the links below to skip to whatever section you would like to read or scroll to start with the first section.

.. contents:: Table of Contents of this Page
   :local:


Connecting to the Device Manager
*********************************

You can follow the steps below to connect to the device manager for the first time. 

.. Note::
	If you have previously selected :ref:`Auto-reconnect<Autoreconnect>` within that browser for the same device, you may not need to repeat these steps every time that you go to the device manager page.

.. Tip::
	If the :ref:`device button<Devicebutton>` at the top right hand corner of the screen is not pink, then the device manager is currently connected to a device. Open the :ref:`device menu<Device Manager:Device Menu>` to make sure that it's the right device.

1. On a chromium based browser, such as Chrome or Edge, go to the `CharaChorder Device Manager <https://manager.charachorder.com>`__ 

.. image:: /assets/images/ManagerFirstTimeConnect.png
  :width: 1200
  :alt: Image of the first time connecting to the Device Manager

2. Click “Connect” 

.. image:: /assets/images/ManagerCONNECT.png
  :width: 1200
  :alt: Arrow showing where on the screen to find the "connect" button

.. dropdown:: Additional Step if you don't see the "Device" box.

    If you don't see the "Device" box on your screen, find the "Device" button in the top right corner. It should be pink in color. Press it in order to see the "Device" box.

	.. _Reference Name: Red Device Button
	.. image:: /assets/images/ManagerREDCONNECTBUTTON.png
  		:width: 1200
  		:alt: Arrow showing where on the screen to find the red "Device" button

3. When the popup box comes up that reads “manager.charachorder.com wants to connect to a serial port”, choose your CharaChorder device, then click the “connect” button

.. image:: /assets/images/ManagerSELECTDEVICE.png
  :width: 400
  :alt: Image showing the dialogue box requesting permission to open a serial connection

If these steps were performed correctly, the device button will have gone from pink to transparent. You can verify that you're connected to the device manager by clicking the device button and reading your device's name and OS version.


Device Manager Website
************************

.. _Devicebutton:
The device manager comes with several useful buttons that "stick" around regardless of what page you go to. The button that really jumped out to you during your first visit was probably the "Device" button. This button is pink at first, before you connect your device, and will turn transparent once you have a device :ref:`connected<Device Manager:Connecting to the Device Manager>`.

.. image:: /assets/images/DMpinkbutton.png
  :width: 1200
  :alt: A picture showing the pink, device button

Device Menu
--------------

.. image:: /assets/images/DMFW.png
  :width: 400
  :alt: The Device Menu

The Device menu is the place where you can connect your CCOS-powered device to the device manager through a :doc:`serial connection<SerialAPI>`. Here, you can also view your device type and CCOS version, as well as disconnect your device from the website's :doc:`serial connection<SerialAPI>`.

.. _Autoreconnect:
Additionally, you'll find a helpful toggle labeled "Auto-connect". By enabling this, the device manager will automatically connect your paired device through a :doc:`serial connection<SerialAPI>` every time that you open it. In doing so, it will also read your chords to detect changes that you may have made since the last time you connected it. If you have this enabled, you won't have to manually connect your device to the manager ever again!

To the right of the connect/disconnect button, you'll find the "terminal" button. Clicking it will take you to the :ref:`terminal<Device Manager:Terminal>` page where you can send serial commands to your device. Check out the :doc:`Serial API<SerialAPI>` docs for information on what commands you can use.

One more step to the right and you'll land on the boot menu button. Here, you'll be able to reboot your device and put it into :ref:`bootloader<Bootloader>` mode.

History Menu
----------------

.. image:: /assets/images/ManagerHistoryMenu.png
  :width: 400
  :alt: The History Menu

The History Menu is home to your backups as well as a the place to go to in order to restore your device by using a backup file. There are different kinds of backups that you can create and we'll cover all of them in the :ref:`backups<Device Manager:Backups>` section.

If you toggle the "Store History" on, then the website will log all of the changes you make to your device so that you may "step back" to a previous state of the device. In other words, if you change your layout, but then decide that you want to revert back to a layout that you tested previously, you'll be able to click into that previous state and undo all of the changes done thereafter. Your history is stored in the browser that you're using at that time and remains on your computer, so only YOU can see the changes you make.


Undo and Redo
---------------

.. image:: /assets/images/ManagerUndoRedo.png
  :width: 200
  :alt: The Undo and Redo arrows

Near the top left corner, the device manager has handy undo and redo buttons which do exactly what their names describe. If you're making changes to your layout, your chords, or your layout, you can step back, one change at a time, all the way back to the very first change that you made during that session. Once you're stepped back, you can step forward to redo the change(s) that was/were undone. 

Pertinent Links
----------------

.. image:: /assets/images/ManagerLinks.png
  :width: 400
  :alt: The Pertinent Links bar

On the bottom left hand of the device manager you can find four buttons that will redirect you to helpful websites related to the manager.

Version
~~~~~~~~~
The leftmost button is the version button will always display the version of the device manager that you're currently using. You can click on it to go to the github page where the device manager is hosted from. If you'd like, you can submit "issues" on github for things you would like to see added to the device manager, such as features or bug fixes.

Issues
~~~~~~~
This button will redirect you to the "issues" page on the device manager github where you can view issues that have been submitted by other users. You can also submit new issues for things that you would like to see added to the device manager, such as features or bug fixes.

Docs
~~~~~~
The Docs button will redirect you to the Official CharaChorder documentation -- this manual that you're reading right now.

Train
~~~~~~~
The button labeled "train" will redirect you to CharaChorder's very own Dot IO. This website will help you to learn to use your device as well as take advantage of CCOS's :doc:`chording<Chords>` feature. 

Color Scheme
--------------
On the bottom right of the device manager, you'll see a circle with a solid color. Hovering over this circle will reveal the label "color scheme." You can click this circle to change the color scheme of the device manager. In the color scheme menu, you can choose your preferred color using a color pallette, an RGB color system, or by clicking the dropper icon to choose a color on your screen.

.. image:: /assets/images/ManagerColorScheme.png
  :width: 300
  :alt: The Color Scheme Menu

Light and Dark Mode
--------------------
Also in the bottom right-hand corner, you'll find a sun or moon icon where you can toggle between light and dark mode. This toggle can help those who would rather a brighter screen to see better or a darker screen to reduce eye strain.

Language
---------
Finally, the last icon in the bottom right corner will allow you to change the device manager's language. Currently, the device manager supports English and German.Changing the manager's language will NOT change your device's layout or the chords in your chord library. It will only change the language in which the device manager's text appears in.

Save Button
-------------

.. image:: /assets/images/ManagerSaveButton.png
  :width: 200
  :alt: The Save Button

If you make changes in the :ref:`chord manager<Device Manager:Chord Manager>`, the :ref:`layout editor<Device Manager:Layout Editor>` or the :ref:`settings menu<Device Manager:Settings Menu>`, a colored "save" button will pop up on your screen, towards the top left corner. 

.. Note::
	Your changes will not take effect until you click the save button.



Chord Manager
***************
.. image:: /assets/images/ChordManager.png
  :width: 1200
  :alt: A picture of the Chord Manager

At the top center of the device manager you'll find a menu with three selections: Chords, Layout, and Settings.

The Chord Manager is a powerful tool that lets you add, delete and edit chords stored in your chord library. It's easy to use and quick to load. We'll go over how to use it below.

When you :ref:`connect<Device Manager:Connecting to the Device Manager>` your device to the device manager, the webpage will start reading the chords on your device. It may take a couple of seconds — or even over a minute for very large libraries — to load the first time. If you have :ref:`auto-reconnect<Autoreconnect>` enabled, the loading times are much shorter.

Chords displayed here are shown in alphabetical order, using the list of :ref:`chord outputs<Chords:Chord Output>`. The number of chords shown on the chord manager depends on your screen size and browser zoom settings. Above the chords list, you'll see the search bar which will display the number of chords on your CCOS device until something is typed there.

.. _search bar:
You can search through your chords by searching :ref:`chord outputs<Chords:Chord Output>` (the word that displays once you've performed a chord). This textbox is not case sensitive, so you can type in capital or lowercase letters regardless of whether or not the chord has a capital letter in it. This search bar is also intuitive enough that you are also able to search partial words/phrases.

To the right of the search bar, you'll find two numbers separated by a forward slash (``/``). These numbers indicate the page number that you're on out of the total number of pages that compose your chord library. Using the angle brackets to the right of those numbers will allow you to flip through the different pages of your chord library which is sorted in alphabetical order.

Under the page-turning brackets, you'll see a tall box with the text "Try typing here". You can use this text box to test your new chords as you edit them in the manager. 

Finally, at the bottom of the chord manager, you'll notice a "Reload" button. You can click on this button to have the device manager read your device's chord library again. This process can take a few seconds.

Creating a Chord
-----------------
You can follow the steps below to create a new chord on the device manager.

.. Note::
	In order to follow these steps, you must already have your device :ref:`connected<Device Manager:Connecting to the Device Manager>` to the device manager.

1. Find the "New chord" text under the :ref:`search bar<Device Manager:search bar>` and click it.


2. When the text displays "Hold chord," press and hold all of the keys that you want to use as your :ref:`chord input<Chords:Chord Input>`. Once you have pressed all of the keys, release the keys.

    You will now see the :ref:`chord input<Chords:Chord Input>` in the left column as letters inside individual boxes. These boxed-letters will be highlighted in a color (as opposed to black or white). The color depends on your selected :ref:`color scheme<Device Manager:Color Scheme>`. You will also notice a single, floating dot highlighted in the same color off to the right of the boxed-letters.

	.. Note::
		You can add any number of chords at a time without defining the desired :ref:`chord output<Chords:Chord Output>`. 

	.. Warning::
		If you click :ref:`save<Device Manager:Save Button>`, before defining a :ref:`chord output<Chords:Chord Output>` as described in :ref:`step three<Step 3>`, any chords that you've created will save to your device with a blank output and will lead to strange behavior.

.. _Step 3:
3. Click into the text box to the right of the :ref:`chord input<Chords:Chord Input>` that you created in the previous step and type your desired :ref:`chord output<Chords:Chord Output>`. 

	.. dropdown:: Using Action Codes
		
		As you type your :ref:`chord output<Chords:Chord Output>`, you'll notice that your cursor will have a bubble with a ``+`` above it. You can click this to open the :ref:`action codes menu<Device Manager:Using Action Codes>` where you can search for specific action codes or browse through the action codes available to assign into a :ref:`chord output<Chords:Chord Output>`. Read the :ref:`action codes section<Device Manager:Using Action Codes>` for information on the different kinds of action codes.

	As you type, you'll notice that your text has changed color to match your :ref:`color scheme<Device Manager:Color Scheme>` and that the end of your text has a floating dot immediately to the right.

4. Once you are satisfied with your :ref:`output<Chords:Chord Output>`, you can proceed to modify another chord or click :ref:`save<Device Manager:Save Button>`. 


Deleting a Chord
-----------------
You can follow the steps below to delete a chord in the device manager.

.. Note::
	In order to follow these steps, you must already have your device :ref:`connected<Device Manager:Connecting to the Device Manager>` to the device manager.

1. Locate the chord that you would like to delete.

2. When you hover over the chord that you would like to delete, you will notice a small trash icon appear in line with that chord map. Click the trash icon in order to mark it for deletion.

	When you click the trash icon, the boxed-letters in the left column will have a line through them and they will turn red. You can unmark chords for deletion by clicking the "undo" arrow next to the trash icon. The chord will return to its original color and the line will disappear.

	.. Tip::
		You can mark multiple chords for deletion at a time. Flipping through the pages in your chord library will not unmark the chords that you have marked for deletion.

3. Once you have marked the undesired chords for deletion and are ready to delete them, click the :ref:`save button<Device Manager:Save Button>`. 

	Once you click save, the marked chord maps will disappear from the list.


Editing a Chord
-----------------
You can follow the steps below to edit an existing chord in the device manager.

.. Note::
	In order to follow these steps, you must already have your device :ref:`connected<Device Manager:Connecting to the Device Manager>` to the device manager.

1. Locate the chord that you would like to edit.

2. Click the textbox in the right column where the :ref:`chord output<Chords:Chord Output>` is displayed.

3. Edit the :ref:`chord output<Chords:Chord Output>` to be whatever you would like. As you type, you will notice that the text changes color to match your :ref:`color scheme<Device Manager:Color Scheme>` and that the end of your text has a floating dot immediately to the right.
	
	.. dropdown:: Using Action Codes
		
		As you type your :ref:`chord output<Chords:Chord Output>`, you'll notice that your cursor will have a bubble with a ``+`` above it. You can click this to open the :ref:`action codes menu<Device Manager:Using Action Codes>` where you can search for specific action codes or browse through the action codes available to assign into a :ref:`chord output<Chords:Chord Output>`. Read the :ref:`action codes section<Device Manager:Using Action Codes>` for information on the different kinds of action codes.

	.. Tip::
		You can edit multiple chords before :ref:`saving<Device Manager:Save Button>` your changes. Flipping through the pages in your chord library will not undo the changes that you have made to your existing chords.

4. Once you are ready to :ref:`save<Device Manager:Save Button>` your changes, click :ref:`save<Device Manager:Save Button>`.

	Once you click :ref:`save<Device Manager:Save Button>`, the chord(s) that you've modified will change color to match the rest of the list and the floating dot will disappear.

Share button
-------------
Next to every chord, you will see a share icon. You can share individual chord maps with others by pressing this button. When you do, your computer's clipboard will copy a URL that you can share with anyone who can then add that exact chord map to their own CharaChorder through the Device Manager. 

When you follow a chord map link, you'll be taken to the Chord Manager where you'll see the new chord map ready to be :ref:`saved<Device Manager:Save Button>`.


Layout Editor
**************
The Device Manager has a very intuitive layer editor. It's the second option in the main navigation bar at the top and center of the page. When you go to this tab, you'll see a diagram of your device, with each key filled in with the corresponding :ref:`action code<Device Manager:Using Action Codes>`.


Layer Selector
----------------

.. dropdown:: Explanation of Layers on CCOS Devices

	As of February of 2024, :doc:`CCOS<CharaChorder Operating System (CCOS)>` devices come with three (3) layers that you can make use of: the base layer, called the A1 (Alpha) layer, the secondary layer, referred to as A2 (Numeric), and the tertiary layer, named A3 (Function).

	In order to access layers, you need to press and hold a "layer access" button. You MUST hold the button in order to use keys mapped to layers other than the alpha layer. The alpha layer is active by default.

	.. note::
		In this section, we’ll refer only to the default layouts on CCOS devices. If you have modified your layout to something different, then the next portion might not be accurate for your device. If you have purchased your device from CharaChorder, then the following is accurate to your device.

	**A1 Layer**

	The A1 layer, also known as the alpha layer, is the main layer that is active by default. Your device will always be in the A1 layer upon boot.

	**A2 Layer**

	The A2 layer, sometimes referred to as the numeric layer, is accessible with the :doc:`A2 access key<CharaChorder Keys>`. In the :doc:`device manager<Device Manager>` this key has the name “Numeric Layer (Left)” and “Numeric Layer (Right)”, one for each hand.

	The A2 Layer is accessible by pressing and holding one layer access button. Any key that is mapped to the A2 Layer can only be accessed by pressing and holding the A2 Layer access key along with the target key. You do not need to :doc:`chord<Chords>` the keys together; it’s only required that the A2 Layer access key is pressed while the target key is pressed.

	**A3 Layer**

	The A3 layer, sometimes referred to as the “function layer”, is accessible with the :ref:`A3 access key<CharaChorder Keys>`. On the :ref:`CharaChorder Device Manager<Device Manager>`, this key is assignable by the names “Function Layer (Left)” and “Function Layer (Right)”.

	Once you've mapped the A3 layer access buttons, the A3 Layer is accessible by pressing and holding either one of them. You do not have to hold them both in order to access the A3 layer. Any key that is on the A3 Layer can only be accessed by pressing and holding the :doc:`A3 access key<CharaChorder Keys>`, along with the target key. You do not need to :doc:`chord<Chords>` the keys together; it’s only required that the A3 layer access key is pressed while the target key is pressed.

.. Note::
	The following section assumes that you have already :ref:`connected<Device Manager:Connecting to the Device Manager>` your device to the device manager.

.. image:: /assets/images/ManagerLayoutSelector.png
  :width: 300
  :alt: Image of the Layer Selector bar

Above the diagram of your device, you'll see a circle with the letters "ABC" in the middle. The circle, together with the "wings" on either side (one on the left with the numbers "123" inscribed and one on the right with "fx" stylized within), make up the layer selector. You can select any one of these to view the keys that are mapped to each location, on each layer.

Remapping
------------
On the layer editor, you can remap your layout by using :ref:`action codes<Device Manager:Using Action Codes>`. Follow the instructions below to remap your device one key at a time.

How to Remap Your Keys
~~~~~~~~~~~~~~~~~~~~~~~

.. Note::
	In order to follow these steps, you must already have your device :ref:`connected<Device Manager:Connecting to the Device Manager>` to the device manager.

1. Choose the :ref:`layer<Device Manager:Layer Selector>` where you want to change the key.

2. Click on the key that you would like to change. This will bring up the :ref:`action codes menu<Device Manager:Using Action Codes>`.

3. Use the search feature in the :ref:`action codes menu<Device Manager:Using Action Codes>` or scroll through available :ref:`action codes<Device Manager:What are Action Codes>`. Once you've found the desired :ref:`action code<Device Manager:Using Action Codes>`, click on it.

	Once you select the :ref:`action code<Device Manager:Using Action Codes>`, you will notice that the layout diagram now reflects the selected :ref:`action code<Device Manager:Using Action Codes>` highlighted according to your :ref:`color scheme<Device Manager:Color Scheme>` and it will be accompanied by a floating dot.

	.. Tip::
		You can edit multiple keys before :ref:`saving<Device Manager:Save Button>` your changes. Flipping through the :ref:`layers<Device Manager:Layer Selector>` will not undo the changes that you have made to the layout so far.

4. Once you have changed the desired key(s), click the :ref:`save button<Device Manager:Save Button>`.

	.. note::
		Your changes will not take effect until you click :ref:`save<Device Manager:Save Button>`.
	
	Once you click :ref:`save<Device Manager:Save Button>`, the highlighted key(s) will lose their highlight and the floating dot will disappear. Your layout diagram will be black and white.

Using Action Codes
~~~~~~~~~~~~~~~~~~~
You can use action codes in chord outputs as well as while :ref:`remapping<Device Manager:Remapping>` keys.

What are Action Codes
^^^^^^^^^^^^^^^^^^^^^^^
Action codes are data that :ref:`CCOS<CharaChorder Operating System (CCOS)>` interprets as characters. **Put simply, they are the characters that we see while typing.** These include letters, numbers, special characters, function keys, and others. 

Action Code Menu
^^^^^^^^^^^^^^^^^^^^^^^
You can open the action codes menu one of two ways:

1. While typing a chord :ref:`chord output<Chords:Chord Output>` in the :ref:`chord manager<Device Manager:Chord Manager>`, you’ll notice that your cursor will have a bubble with a + above it. You can click this to open the action codes menu.

2. While editing your layout in the :ref:`layout editor<Device Manager:Layout Editor>`, click on a key to bring up the action codes menu.

In this menu, you can scroll through :ref:`available action codes<Device Manager:Available Action Codes>` by :ref:`category<Action Code Categories>`, or simply search specific actions. 

If you ever need to leave the action codes menu, simply click the X at the top right of the menu. This will close out the box and not make any changes.

Action Code Categories
..........................
There are eight different categories in the action code menu. These are: ASCII Macros, ASCII, CharaChorder One, CharaChorder, CP-1252, Keyboard, Mouse, and Key Codes.



.. ASCII Macros
   ,,,,,,,,,,,,,,

   ASCII
   ,,,,,,,,,,,

   CharaChorder One
   ,,,,,,,,,,,,,,,,,,,,,,,,,

   CharaChorder
   ,,,,,,,,,,,,,,,,,,,,,,,,,

   CP-1252
   ,,,,,,,,,,,,,,,,,,,,,,,,,

   Keyboard
   ,,,,,,,,,,,,,,,,,,,,,,,,,

   Mouse
   ,,,,,,,,,,,,,,,,,,,,,,,,,

   Key Codes
   ,,,,,,,,,,,,,,,,,,,,,,,,,

Remove Button
................
You can use the "Remove" button on the top right of the action codes menu to remove the currently assigned action code from the selected key in the :ref:`layout editor<Device Manager:Layout Editor>`. 

If you select the "Remove" button while typing a :ref:`chord output<Chords:Chord Output>` in the :ref:`chord manager<Device Manager:Chord Manager>`, it will NOT remove any action. Instead, it will add a "blank" action that will be labeled ``0x0``. 



Available Action Codes
^^^^^^^^^^^^^^^^^^^^^^^
You can see the action codes below, or view them externally `here. <https://docs.google.com/spreadsheets/d/1--T9bXshCIC-OVly-CY3rK87fgb7AHgJl3IySh7cmHc/edit#gid=0>`__

.. raw:: html

    <iframe src="https://docs.google.com/spreadsheets/d/1--T9bXshCIC-OVly-CY3rK87fgb7AHgJl3IySh7cmHc/edit#gid=0" width="600" height="600"></iframe>




Settings Menu
***************
On the Settings tab in the top navigation bar of the Device Manager page, you can adjust the settings of your :ref:`connected<Device Manager:Connecting to the Device Manager>` CCOS device. Read on to see the different settings you can change. You can find more detailed explanations in the :ref:`GTM<GenerativeTextMenu>` section.

Spurring
----------

.. dropdown:: What is Spurring?

	Spurring is a ‘chording only’ mode which tells your device to output :ref:`chords<Chords:What are Chords?>` on a press event rather than a press and release event. When in spurring mode, you can press the keys of a :ref:`chord<Chords:What are Chords?>` one at a time with a much longer waiting period, which makes it a useful mode for those who want to practice chording without worrying about proper :ref:`timing<GenerativeTextMenu:Press Tolerance>`.

	Spurring mode also enables you to jump from one :ref:`chord<Chords:What are Chords?>` to another without releasing everything. It can provide significant speed gains when chording, but also takes away the flexibility of character entry. Spurring mode can truly maximize speed when chording if a user has chords for all of the words they want to use.

.. image:: /assets/images/ManagerSettingsSpurring.png
  :width: 1200
  :alt: The Spurring settings box

In this box, you can enable or disable spurring mode as well as increase or decrease the :ref:`spurring timeout setting<GenerativeTextMenu:Spurring Timeout>`.

Arpeggiates
-------------
.. dropdown:: What are arpeggiates?

	Arpeggiate actions are timed actions that can modify a :ref:`chord<Chords:What are Chords?>` after the chord is performed. A quick example of this is the use of :ref:`chord modifiers<Device Manager:Chord Modifiers>` after you perform the chord. You can read that section for information on how the chord modifiers work.

	With arpeggiates enabled, you can chord the word run and then, within the :ref:`arpeggiate timeout window<GenerativeTextMenu:Arpeggiate Timeout>`, press the :ref:`past tense modifier<Device Manager:Past Tense>` for the word to be “modified” into its past tense variant; in english, ran.

.. image:: /assets/images/ManagerSettingsArpeggiates.png
  :width: 1200
  :alt: The Arpeggiates settings box

In this box, ou can enable or disable arpeggiates as well as increase or decrease the :ref:`arpeggiate timeout setting<GenerativeTextMenu:Arpeggiate Timeout>`.

Chord Modifiers
-----------------
.. dropdown:: What are chord modifiers?

	Chord modifiers are actions that change a chord when :ref:`chorded<Chords:What are Chords?>` at the same time as the :ref:`chord input<Chords:Chord Input>`, or when pressed immediately after (arpeggiately) the :ref:`chord<Chords:What are Chords?>`, provided that :ref:`arpeggiates<GenerativeTextMenu:Arpeggiate>` are enabled.

	As of February of 2024, only the CharaChorder One and CharaChorder Lite support the use of chord modifiers. Additionally, as of that same time, chord modifiers only work in English.

	.. note::
		Chord modifiers are NOT the same as keyboard modifiers. Keyboard modifiers affect keys pressed on a keyboard. Those keys include ``CTRL``, ``ALT``, and ``FN``. Chord modifiers affect chords.

.. image:: /assets/images/ManagerSettingsModifiers.png
  :width: 1200
  :alt: The Chord Modifiers settings box

In this box, you can read a brief explanation of chord modifiers and how to access them.

Capitalization
~~~~~~~~~~~~~~~
The capitalization modifier modifies any chord so that the first letter is capitalized on :ref:`output<Chords:Chord Output>`. This :ref:`modifier<Device Manager:Chord Modifiers>` can be performed together with a :ref:`chord<Chords:What are Chords?>` or :ref:`arpeggiately<GenerativeTextMenu:Arpeggiate>`.

The capitalization modifier is located on the ``SHIFT`` key. In the :ref:`layout editor<Device Manager:Layout Editor>`, this key can be either "Shift Keyboard Modifier (Left)" or "Shift Keyboard Modifier (Right)".

.. note::
	If you have ``CAPS LOCK`` active, all letters in a chord will be capitalized except the first one when using this modifier.

Present Tense
~~~~~~~~~~~~~~
The present tense modifier modifies supported chords so that they turn into their present tense variants. The word "run" would be modified into "running" and the word "work" would be turned into "working". This :ref:`modifier<Device Manager:Chord Modifiers>` can be performed together with a :ref:`chord<Chords:What are Chords?>` or :ref:`arpeggiately<GenerativeTextMenu:Arpeggiate>`.

The present tense modifier has different locations depending on your device. On the CharaChorder One, this modifier is linked to the "AMBIDEXTROUS THROWOVER (LEFT)" key. On the CharaChorder Lite, it's linked to the "NUMERIC LAYER (LEFT)" key.

Pluralizer
~~~~~~~~~~~
The pluralizer modifier makes supported chords plural. It will add an "s" or "es" to the end of supported chords. "Box" will turn into "boxes" and "dog" will become "dogs". This :ref:`modifier<Device Manager:Chord Modifiers>` can be performed together with a :ref:`chord<Chords:What are Chords?>` or :ref:`arpeggiately<GenerativeTextMenu:Arpeggiate>`.

The pluralizer modifier has different locations depending on your device. On the CharaChorder One, it's linked to the "AMBIDEXTROUS THROWOVER (RIGHT)" key. On the CharaChorder Lite, it's linked to the "RIGHT SPACEBAR" key, not to be confused with the "SPACE" key.

Past Tense
~~~~~~~~~~~
The past tense modifier modifies supported chords so that they turn into their past tense variants. The word "run" would be modified into "ran". The word "work" would be turned into "worked". This :ref:`modifier<Device Manager:Chord Modifiers>` can be performed together with a :ref:`chord<Chords:What are Chords?>` or :ref:`arpeggiately<GenerativeTextMenu:Arpeggiate>`.

The past tense modifier has different locations depending on your device. On the CharaChorder One, it's linked to the "NUMERIC LAYER (LEFT)" key. On the CharaChorder Lite, it's linked to the "SPACE" key, not to be confused with the "RIGHT SPACEBAR" key.

Comparative
~~~~~~~~~~~~~
The comparative modifier modifies supported chords so that they turn into their comparative variant. "Big" becomes "bigger" and "small" turns into "smaller". This :ref:`modifier<Device Manager:Chord Modifiers>` can be performed together with a :ref:`chord<Chords:What are Chords?>` or :ref:`arpeggiately<GenerativeTextMenu:Arpeggiate>`.

The comparative modifier is located on the "NUMERIC LAYER (RIGHT)" key on both the CharaChorder One and the CharaChorder Lite.


Character Entry
----------------
.. dropdown:: What is Character Entry?

	Character entry, known to the CharaChorder community as "chentry," refers to typing one character at time. 

.. image:: /assets/images/ManagerSettingsChentry.png
  :width: 1200
  :alt: The Character Entry settings box

In this box, you can change a few settings that relate to using your device for character entry. 

.. dropdown:: Swap Keymap 0 and 1

	This setting will swap the behavior of the two keys on the bottom-left of the CharaChorder Lite.

	Traditional QWERTY keyboards keep the ``CTRL`` key at the bottom left corner of the keyboard with the ``GUI`` key (Command key on Mac, Windows key on Windows, Super key on Linux, etc.) to the right of the ``CTRL`` key. The CharaChorder Lite has these two keys swapped by default, which some users find odd and difficult to adjust to. A brand new CharaChorder Lite will have the ``GUI`` key at the bottom-left corner with the ``CTRL`` key to the right of the ``GUI`` key.

	With this setting, you can effectively swap the two keys’ location at the level of the CCOS so that CTRL is at the bottom-left corner.

.. dropdown:: Character Entry (chentry)

	This setting is a toggle that disables chording capabilities on CCOS devices. It is off by default and can be enabled in case we don’t want any chording at all. This setting can be useful in cases where we don’t want to accidentally trigger chords unintentionally, such as when gaming.

	If your CCOS device suddenly loses its chording ability, it’s a good idea to check if this setting is toggled off.

.. dropdown:: Key Scan Rate

	The scan rate, sometimes known as the “Key scan duration,” refers to the frequency at which the device checks the state of the input keys. For reference, 5 ms corresponds to 200 Hz, which means that :doc:`CCOS<CharaChorder Operating System (CCOS)>` checks the position of the keys once every 5 milliseconds, which equals 200 times in a second. Having a lower number is usually better as it makes CCOS more responsive, though the difference at low numbers is usually negligible. In the GTM, this setting is adjustable in millisecond (ms) units.

.. dropdown:: Key Debounce Press

	The debounce press setting refers to the time frame (measured in milliseconds) in which :doc:`CCOS<CharaChorder Operating System (CCOS)>` will filter out duplicate key activations on a press event. In other words, any duplicate activations within the given time frame will only be counted as one.

	We should adjust this setting if we are having unintentional duplicate characters while typing. Increasing this value will lower the probability that unwanted duplicate characters will appear because it tells :doc:`CCOS<CharaChorder Operating System (CCOS)>` to wait longer before typing an additional character that’s assigned to the same switch-direction. However, having this setting set too high might also cause issues with :doc:`CCOS<CharaChorder Operating System (CCOS)>` not reading intentional double-presses, so it’s recommended to try different numbers in small increments. This setting should be used in connection with the debounce release setting.

.. dropdown:: Key Debounce Release

	The debounce release setting refers to the time frame (measured in milliseconds) in which :doc:`CCOS<CharaChorder Operating System (CCOS)>` will filter out duplicate key activations on a release event. In other words, any duplicate activations within the given time frame will only be counted as one.

	We should adjust this setting if we are having unintentional duplicate characters while typing. Increasing this value will lower the probability that unwanted duplicate characters will appear because it tells :doc:`CCOS<CharaChorder Operating System (CCOS)>` to wait longer before typing an additional character that’s assigned to the same switch-direction. However, having this setting set too high might also cause issues with :doc:`CCOS<CharaChorder Operating System (CCOS)>` not reading intentional double-presses, so it’s recommended to try different numbers in small increments. This setting should be used in connection with the debounce press setting.

.. dropdown:: Output Character Delay

	This setting adds a small delay to keystroke inputs. It is measured in microseconds (μs) and is very small by default.

	You should increase this value if your computer is not accepting all of the characters output by your device, such as when using the :doc:`GTM<GenerativeTextMenu>`. If you are having this issue, your :doc:`GTM<GenerativeTextMenu>` would look weird, with missing chunks or characters.

	If you have a faster computer, then you can lower this setting to make chording and the :doc:`GTM<GenerativeTextMenu>` feel snappier and more responsive.

Mouse
-------
.. dropdown:: Mouse???

	:doc:`CCOS<CharaChorder Operating System (CCOS)>` has mouse functionality. This means that your CharaChorder, or CCOS-powered keyboard, has the ability to control your computer's mouse. These settings affect the mouse usage on your CharaChorder.

.. image:: /assets/images/ManagerSettingsMouse.png
  :width: 1200
  :alt: The Mouse settings box

In this box, you can adjust settings relating to :doc:`CCOS'<CharaChorder Operating System (CCOS)>` mouse abilities.

.. dropdown:: Mouse Speed(s)

	:doc:`CCOS<CharaChorder Operating System (CCOS)>` has two mouse speeds, a fast speed and a slow speed. The slow speed is activated when you use only one of the mouse keys in a single direction (as opposed to using 2 keys in the same direction). The fast speed is activated when you use two mouse keys in a single direction (as opposed to using only one key in the same direction).

	You can read a more in-depth explanation of mouse speeds in the :ref:`GTM section<GenerativeTextMenu:Slow Speed>`. 

.. dropdown:: Scroll Speed

	Scroll speed refers to the speed at which your :doc:`CCOS<CharaChorder Operating System (CCOS)>` scroll will scroll.

	You can read a more in-depth explanation of the scroll speed in the :ref:`GTM section<GenerativeTextMenu:Scroll Speed>`.

.. dropdown:: Active Mouse

	Active mode nudges your mouse cursor one pixel every minute or so (not a specific timing). This setting can be used to keep your computer from going to sleep. You might turn this setting off if you notice desktop apps are preventing you from getting mobile notifications (for example on Discord or Microsoft Teams).

.. dropdown:: Poll Rate

	The polling rate (poll rate) is the frequency at which data from the CharaChorder’s mouse functionality is sent to the device it’s connected to. In other words, how often it updates the cursor’s position to the computer. 

	You can read a more in-depth explanation of the polling rate in the :ref:`GTM section<GenerativeTextMenu:Poll Rate>`.

Chording
-----------
.. dropdown:: What is Chording?

	Chording is the beautiful ability of pressing multiple keys at a time to get a predefined output, whether it's a single word, an entire phrase, or important addresses. 

	A chord is a type of input/output action on a keyboard: you press two or more keys at the same time and release them at the same time, after which a predefined output will replace the originally pressed keys.

	By chording, we are able to type one word at a time instead of one letter at a time. It’s even possible to have chords for phrases and entire sentences.

.. image:: /assets/images/ManagerSettingsChording.png
  :width: 1200
  :alt: The Chording settings box

In this box, you can adjust settings relating to :doc:`CCOS'<CharaChorder Operating System (CCOS)>` :doc:`chording<Chords>` abilities as well as turn off :doc:`chording<Chords>` alltogether, should you choose to.

.. dropdown:: Auto-delete Timeout

	This setting will change how long CCOS counts time in order to replace characters that precede a chord.

	CCOS devices have a running timer that starts after every single character that is entered in traditional chentry (character entry, i.e. one letter at a time). This timer controls whether or not the next chord that you perform deletes the preceding characters.

	This feature allows users to misfire chords, yet be able to correct them by quickly performing the chord correctly, without having to backspace manually to erase the misfired chord. The result is that the timeout will automatically backspace all of the preceding characters (up to the last breaking character) and replace them with the intended chord.

.. dropdown:: Press Tolerance

	The press tolerance refers to a window of time in which a chord can be performed, measured in milliseconds (ms). This timer is initiated upon the first “press” action of the first key in a chord and ends once the last key of the chord is pressed, or until the press tolerance runs out, whichever comes first. Read the :ref:`GTM section<GenerativeTextMenu:Press Tolerance>` for a more in-depth explanation.

.. dropdown:: Release Tolerance

	he release tolerance refers to a window of time in which a chord can be performed, measured in milliseconds (ms). This timer is initiated upon the first “release” action of any key in a chord and ends once the chord is fully performed, or until the release tolerance runs out, whichever comes first. Read the :ref:`GTM section<GenerativeTextMenu:Release Tolerance>` for a more in-depth explanation.

.. dropdown:: Compound Chording

	This toggle allows you to enable or disable :ref:`compound chords<Chords:Compound Chords>`.

Device
-------
These settings pertain to your device. The :ref:`boot message<GenerativeTextMenu:Startup>` and :ref:`realtime feedback<GenerativeTextMenu:Realtime Feedback>` can be enabled or disabled in this box.

.. image:: /assets/images/ManagerSettingsDevice.png
  :width: 1200
  :alt: The Device settings box

Additionally, you can reset some parts of your device files such as your chords, your layout, and even return to factory settings.

.. image:: /assets/images/ManagerSettingsResets.png
  :width: 1200
  :alt: The Reset settings box

RGB
------
The RGB settings ONLY affect the CharaChorder Lite as of February of 2024. 

These settings adjust the color and brightness of your CharaChorder Lite.


.. image:: /assets/images/ManagerSettingsRGB.png
  :width: 1200
  :alt: The RGB settings box


Other Tools
*************



Backups
--------
On the Device Manager, you can create backups of your chords, your layout, and even your settings. Follow the steps below to create a backup and to restore saved backups to your :doc:`CCOS<CharaChorder Operating System (CCOS)>` device.

Creating a Backup
~~~~~~~~~~~~~~~~~~
.. Note::
	In order to follow these steps, you must already have your device :ref:`connected<Device Manager:Connecting to the Device Manager>` to the device manager.

1. Open the :ref:`history menu<Device Manager:History Menu>`.

2. Choose an "individual backup" to download to your computer, or select "download everything" to download a single file with all three parts. The file(s) will be downloaded in .json format.

	.. note::
		You can make individual backups of just your chords, just your layout, or just your settings. The "download everything" option will download all three of these in a single file instead of three separate files.

3. If prompted, select a location to save to on your computer and rename the file to your liking.

Congratulations! Now you have created a backup.

Restoring from a Backup
~~~~~~~~~~~~~~~~~~~~~~~~~
Additionally, you can restore your chords, your layout, and your settings on the Device Manager. Follow the steps below to do so.

.. Note::
	In order to follow these steps, you must already have your device :ref:`connected<Device Manager:Connecting to the Device Manager>` to the device manager.

1. Open the :ref:`history menu<Device Manager:History Menu>`.

2. Click on "Restore".

3. Select a file to use to restore from. This file should be in .json format.

	.. note::
		Files that you can restore from will have been created ahead of time by following the :ref:`steps to create a backup<Creating a Backup>`. 

4. If there are changes, the :ref:`save button<Device Manager:Save Button>` will appear on the top left. Note the changes in the appropriate tab. If you restored chords, check the :ref:`chords tab<Device Manager:Chord Manager>`, if you restored a layout, check the :ref:`layout tab<Device Manager:Layout Editor>`, and if you restored settings, check the :ref:`settings tab<Device Manager:Settings Menu>`.

	.. note::
		The restore feature does NOT erase data from your device. If there is a conflict (such as a changed setting, a different key in the layout, or a chord that has a different :ref:`output<Chords:Chord Output>`), that will be overwritten by the restore file. Settings and layout backups ALWAYS overwrite everything.

5. Once you see the changes that the restore file made, you can click :ref:`save<Device Manager:Save Button>` to apply the changes.

Bootloader
-----------
In the :ref:`device menu<Device Manager:Device Menu>`, you'll find the boot menu button. When you click on that, it'll bring up the option to put your device into bootloader.

In bootloader mode, your :doc:`CCOS<CharaChorder Operating System (CCOS)>` device will disconnect from the Device Manager and a new drive will appear in your File Explorer (Finder, in Mac OS). This drive contains your CharaChorder's CCOS information.

Updating Your Device
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. Note::
	In order to follow these steps, you must already have your device :ref:`connected<Device Manager:Connecting to the Device Manager>` to the device manager.

.. warning::
	Before performing the below steps, please make sure that you have a :ref:`backup of your layout<Device Manager:Backups>` as well as a :ref:`backup of your chord library<Device Manager:Backups>` and a :ref:`backup of your GTM settings<Device Manager:Backups>`. The update might reset those, so it's important that you    keep backup files handy. For instructions on how to restore backed-up files, visit the :ref:`Backups<Device Manager:Backups>` section.

.. _step 1:
1. Click “Boot Menu” (the power icon) followed by “Bootloader”. Your CharaChorder will now appear as an external storage device on your computer’s File Explorer or Finder app. It might be named one of the following: “Arduino”, “Seeduino”, or “CharaChorder One”.


.. image:: /assets/images/ManagerPowerButton-Lite.png
  :width: 1200
  :alt: The Boot button


.. image:: /assets/images/ManagerBootloaderButton-Lite.png
  :width: 1200
  :alt: The Bootloader Button

2. Download your update file from this site: `<https://www.charachorder.com/pages/update-your-firmware>`__

.. danger::
	Make sure that the file you download is named exactly like this: CURRENT.UF2 . If there are any other characters in the file name, the file will not work. “CURRENT(1).UF2” will NOT work. Additionally, the file name is case-sensitive; all letters must be capitalized.

8. Copy the CURRENT.UF2 file that you just downloaded and paste it into the CharaChorder drive that we found in :ref:`step 1<step 1>`.

9. When your computer asks you how you would like to resolve the issue of two files with the same name, select “Replace file”.

At this point, your device will automatically reboot, and the
CharaChorder drive will have disappeared. Congratulations! You have
successfully updated your device. You can check your device’s CCOS :ref:`in the device menu<Device Manager:Device Menu>`.

Terminal
----------
Also in the :ref:`device menu<Device Manager:Device Menu>`, you'll find the option to go into the terminal. This is a sandbox space where you can feed commands directly to your CCOS device.

You can read about the available commands in the :doc:`serial api section<SerialAPI>`.


.. image:: /assets/images/ManagerTerminal.png
  :width: 1200
  :alt: The Terminal page on the Device Manager



















