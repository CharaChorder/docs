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

Profiles share the same chord library because we already have chord profiles in the form of dynamic libraries. If you want to activate a dynamic library for your profile you can use a chord to both activate the profile and the dynamic library.

Each profile has its own settings. For example, on the Master Forge, each profile can have its own LED colors (currently only on the left half).

Profiles are backed up individually, by switching to profile A, B, or C at the top of the Device Manager's Device/Settings page before backing up.

During the beta period, the profiles can be configured on: https://master.dev.charachorder.io/

Layer warp
~~~~~~~~~~

For gaming profiles, we added a "layer warp" setting which re-presses held keys when you switch layers.

With layer warp, by temporarily holding down another key, you can reverse direction of movement or stop all together without ever releasing the walk forward key.

With Profile B set up for gaming, the key bindings could look like this:

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

The CAPTURE action makes it possible to replace the space after a chord with another character such as a dash (-) or an underscore (_).

For this to work, we need to create at least two chords:

* One chord that has a space between two CAPTURE actions:

    .. code-block::

        CAPTURE CAPTURE

    It restores the default behavior of adding a space after each chord:

    .. code-block::

        the on us

* Another chord that has a character between the CAPTURE actions, to replace the space:

    .. code-block::

        CAPTURE-CAPTURE

    This results in:

    .. code-block::

        the-on-us-

* Or:

    .. code-block::

        CAPTURE_CAPTURE

    Which results in:

    .. code-block::

        the_on_us_

Prepend concatenation style
~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can now select "prepended" as a concatenation style. This mode is part of the Hyperspace feature and recommended for text editing (like coding). Instead of placing a space after a chord (default), the chord is prepended to the subsequent chord. This means that you don't have to erase extra spaces while editing.

Vim mode
~~~~~~~~

.. note::

    Mac users. Set the Operating System setting to: Mac
    https://charachorder.io/config/settings/#misc

Adds universal VIM motion emulation through the VIM action. This mode makes use of standard shortcuts like CTRL (or ⌘ on Mac) + RIGHT ARROW to emulate VIM motions in a best-effort way in any textbox. While not as powerful as native VIM or even just a VIM plugin, you don't always have the option to use either of them, so this is a way to carry around your VIM muscle memory to nearly every textbox you encounter.

Quick flick
~~~~~~~~~~~

Quickly flick a switch to override its function (imagine the opposite of holding it). This was designed with the Master Forge in mind, but works on CC1/CC2 as well, but less consistent than on traditional keyboard switches.

Updated grammar rules
~~~~~~~~~~~~~~~~~~~~~

Grammar rules have been updated with community contributions. You can submit your own on our Issue Repo: https://github.com/CharaChorder/CCOS-firmware

Grammar rules are now case insensitive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Chord modifiers now also work on capitalized words.

Capitalize now toggles case
~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can now use an arpeggiated capitalize modifier to toggle capitalization (i.e. undo the auto-capitalize after an arpeggiated period)

USB Aggressive Reporting
~~~~~~~~~~~~~~~~~~~~~~~~

Enabling this might improve stability on certain hardware combinations.

Keyboard Rollover Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~

Reducing this to 6-key might improve compatibility with older hardware.

The choices are:

* 6-key
* 12-key (default)
* 18-key


CC One Features
~~~~~~~~~~~~~~~

Moved settings and layout flash
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Settings/layout storage have been moved from onboard flash to the external flash (the same place where the chords live). The first update will cause a factory reset, however the following updates will no longer wipe the settings or the layout.

Fixes
-----

Potentially improved USB Hub compatibility
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Potentially improved USB Hub compatibility

Fixed device names in the manager popup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the Device Manager's serial port dialog, the Master Forge used to appear as: TinyUSB
Now it has the device name: Master Forge Anchor

Poll rate setting
~~~~~~~~~~~~~~~~~

Replaced the mouse/keyboard poll rate settings (which didn't actually change the poll rate) with a USB poll rate setting under a new experimental category.

Improved flash performance
~~~~~~~~~~~~~~~~~~~~~~~~~~

Primarily noticeable with chord importing.

Capitalize action was not interrupted by chentry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following examples result from pressing:

chord, period, character, space, chord

Before::

    the. t The

The last chord became capitalized even though it wasn't the first character or chord after the period.

Now::

    the. t the

The last chord's capitalization was interrupted by the chentry.

NULL is now ignored as an action
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Subsequent modifiers that use layer keys, no longer break backspacing when the target layer has no actions on part of the chord input keys.

Stuck key mitigation
~~~~~~~~~~~~~~~~~~~~

As a general fallback measure against (software-)stuck keys, we added a measure that releases all keys when you either physically release all switches or at the end of a chord.

Specific compounds that caused library corruption
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There was a bug that could cause library corruption which has now been fixed. This only happened when adding :ref:`compound chords<Chords:Compound Chords>` with a specific base. You can check if your library contained any of these here: https://master.dev.charachorder.io/config/chords/will-my-compound-break/

CC Lite S2 Fixes
~~~~~~~~~~~~~~~~

Fixed swapped Right Shift and Quote keys
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Right Shift typed a single quote, and the single quote key behaved as Right Shift.

CC One Fixes
~~~~~~~~~~~~

Incorrect max chord count
^^^^^^^^^^^^^^^^^^^^^^^^^

In a past update, we incorrectly stated that the maximum chord count was increased to 16.000 (sixteen thousand). However, the actual increase was to 10.240 (ten thousand, two hundred forty), but with additional optimization, the maximum chord count has now been raised to 11.720 (eleven thousand, seven hundred twenty).

Memory corruption when approaching chord limit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This issue could cause memory corruption when approaching the limit of 10,240 chords, approximately starting around 9000 chords.

M4G Fixes
~~~~~~~~~

Disconnect issues
^^^^^^^^^^^^^^^^^

We added a new "aggressive reporting" setting in the hope that it would help improve intermittent disconnects, particularly on MacOS and Windows. However, user feedback indicates that this change has had no effect on the issue. Our team is continuing to investigate and work on solutions.

LEDs can now be fully turned off
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The M4G's LEDs couldn't dim below their minimum brightness.
