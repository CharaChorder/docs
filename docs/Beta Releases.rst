Beta Releases
=============

.. contents::
	:local:

2.2.0-beta
**********
 
Features
--------

Profiles
~~~~~~~~

Three profiles can now be defined, each with three layers:

* Profile A, layout layer A1, A2, or A3
* Profile B, layout layer B1, B2, or B3
* Profile C, layout layer C1, C2, or C3

Profiles share the same chord library. Because we already have chord profiles in the form of dynamic libraries. If you want to activate a dynamic library for your profile you can use a chord to both activate the profile and the dynamic library.

Each profile has its own settings. For example, each profile can have it's own LED colors (currently only on the left half).

Profiles are backed up individually, by switching to profile A, B, or C at the top of the Managers Device page before backing up.

Layer warp
~~~~~~~~~~

For gaming profiles we added a "layer warp" setting which re-presses held keys when you switch layers.

With layer warp, you can holding a key (ex: walk forward) and temporarily hold a second key to either:

* reverse direction
* stop

Then continue walking forward by releasing the reverse or stop key.

This can be done on for example, profile B with the following key bindings: 

Layer B1::

	Left Ring
	   any
	any   any
	   B3
	
	Left Middle
	   any
	any   any
	   B2

	Left Thumb 1
	   w
	a     d
	   s


Layer B2::

	Left Middle
	   any
	any   any
	   B2

	Left Thumb 1
	   s
	d     a
	   w

Layer B3::

	Left Ring
	     any
	any       any
	     B3
	
	Left Thumb 1
	     BLANK
	BLANK     BLANK
	     BLANK

We walk forward by holding Left Thumb 1 North (``w``).
	
Reverse direction:

	* We reverse direction temporarily by also holding Left Middle South (Layer B2), because it causes a repress of Left Thumb 1 North, which is now bound to ``s``.
	* We start walking forward again by releasing Left Middle South (B2), it represses Left Thumb 1 North (``w``).

Stop:

	* We stop temporarily by holding Left Ring South (Layer B3), it represses Left Thumb 1 North, which isn't bound to anything.
	* We start walking forward again by releasing Left Ring South (B3), it represses Left Thumb 1 North (``w``).

Hyperspace
~~~~~~~~~~

Control what the concatenator between chords is using with the new HYPERSPACE and CAPTURE actions.

The CAPTURE action makes it possible to replace the space after a chord with for example, a dash (-) or an underscore (_).

At least two chords need to be created:

1. One chord that has a space between two CAPTURE actions:

	.. code-block::
	
		CAPTURE CAPTURE

	It restores the default behavior of adding a space after each chord:
	
	.. code-block::
	
		the on us 

2. Another chord that has a character between the CAPTURE actions, to replace the space:

	.. code-block::
	
		CAPTURE-CAPTURE

	This results in:

	.. code-block::
	
		the-on-us-

3. Or:

	.. code-block::
	
		CAPTURE_CAPTURE

	Which results in:

	.. code-block::
	
		the_on_us_

Prepend concatenation style
~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can now select "prepended" as a concatenation style. This mode is part of the Hyperspace feature, and recommended for text editing (like coding). Instead of placing the space after chords (default), it is prepended to the subsequent chord. This means you don't have to erase extra spaces while editing.

Vim mode (beta)
~~~~~~~~~~~~~~~

Adds universal VIM motion emulation through the VIM action. This mode makes use of standard shortcuts like CTRL (or ⌘ on Mac) + RIGHT ARROW to emulate VIM motions in a best-effort way in any textbox. While not as powerful as native VIM or even just a VIM plugin, you don't always have the option to use either of them, so this is a way to carry around your VIM muscle memory to nearly every textbox you encounter.

Quick flick
~~~~~~~~~~~

Quickly flick a switch to override its function (imagine the opposite of holding it). This was designed with the Master Forge in mind, but works on CC1/CC2 as well, but less consistent than on traditional keyboard switches.

Updated grammar rules
~~~~~~~~~~~~~~~~~~~~~

Grammar rules have been updated with community contributions. You can submit your own on our Issue Repo: https://github.com/CharaChorder/CCOS-firmware

Grammar rules are now case insensitive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Capitalize now toggles case
~~~~~~~~~~~~~~~~~~~~~~~~~~~

USB Aggressive Reporting
~~~~~~~~~~~~~~~~~~~~~~~~

Enabling this might improve stability on certain hardware combinations.

Keyboard Rollover Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~

Reducing this to 6-key might improve compatibility with older hardware.

CC One Features
~~~~~~~~~~~~~~~

Moved settings and layout flash
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Settings/layout storage have been moved from onboard flash to the external flash (the same place where the chords live). The first update will cause a factory reset, however the following updates will no longer wipe the settings or the layout.

Fixes
-----

Potential improved USB Hub compatibility
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fixed device names in the manager popup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Poll rate setting
~~~~~~~~~~~~~~~~~

Replaced the mouse/keyboard poll rate settings (which didn't actually change the poll rate) with a USB poll rate setting under a new experimental category.

Improved flash performance
~~~~~~~~~~~~~~~~~~~~~~~~~~

Capitalize action is not interrupted by chentry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

NULL is now ignored as an action
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Subsequent modifiers that use layer keys, no longer break backspacing when the target layer has no actions on part of the chord input keys.

Stuck key mitigation
~~~~~~~~~~~~~~~~~~~~

As a general fallback measure against (software-)stuck keys, we added a measure that releases all keys when you either physically release all switches or at the end of a chord.

Specific compounds caused library corruption
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There was a bug that could cause library corruption, if you got unlucky. That has now been fixed. This only happened when adding compound chords with a specific base. You can check if your library contained any of these here: https://master.dev.charachorder.io/config/chords/will-my-compound-break/

CC Lite S2 Fixes
~~~~~~~~~~~~~~~~

Fixed swapped Right Shift and Quote keys
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

CC One Fixes
~~~~~~~~~~~~

Incorrect max chord count
^^^^^^^^^^^^^^^^^^^^^^^^^

In a past update it was incorrectly stated that the maximum chord count was increased to 16k. The actual increase was to 10,240. With additional optimization the maximum chord count was now lifted to 11,720.

Memory corruption when approaching chord limit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This issue could cause memory corruption when approaching the limit of 10,240 chords, approximately starting around 9000 chords.

M4G Fixes
~~~~~~~~~

Disconnect issues
^^^^^^^^^^^^^^^^^^

We've identified a potential workaround for intermittent disconnects on primarily MacOS and Windows. It's available as the "aggressive reporting" setting. We're still continuing to investigate as we gather feedback from this change.

LEDs can now be fully turned off
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

