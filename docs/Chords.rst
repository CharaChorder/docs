Chords
=============================
One of CharaChorder devices’ greatest features is their
:doc:`chording<Chords>` ability. Read this section to learn what
chording is and how you can benefit from it on your own CharaChorder. 

.. contents::
   :local:

What are Chords?
-----------------

A chord is a type of input/output action on a keyboard: you press two or
more keys at the same time and release them at the same time, after
which a predefined output will replace the originally pressed keys.

By chording, we are able to type one word at a time instead of one
letter at a time. It’s even possible to have chords for phrases and
entire sentences. 

How do I use Chords?
----------------------

A chord has an **input** and an **output**. We will describe what each
of those is and how they affect chords on your CharaChorder device
below. Throughout this guide, we might use the term “perform” when
talking about carrying out a chord. 

Chord Input
~~~~~~~~~~~~~~~~~~

A chord input is the
combination of keys used in order to get a desired, predetermined
:ref:`output<Chord Output>`. For example, we can have a chord that
requires the simultaneous press and release of the keys ``b`` and ``c``
to get the output “because”. In :ref:`chord notation<Chord Notation>`,
we would write that chord input as ``b+c``. Since chord inputs are
performed simultaneously, meaning that all of the keys needed for an
input are pressed and released at the same time, chord inputs are not
order-specific. ``b+c`` is the same as ``c+b``. 

Chord Output 
~~~~~~~~~~~~~~~~~~

A chord
output is the predetermined letters, words, phrases and/or actions that
result after performing a chord. If we use the
:ref:`chord input<Chord Input>` of ``b`` and ``c`` and the result is
the word “because”, then the word “because” would be the output. In
:ref:`chord notation<Chord Notation>`, we would write that chord (the
input and the output) as ``b+c = because``. 

Chord Notation 
~~~~~~~~~~~~~~~~~~

Chord
notation is the way that we write chords for CharaChorder devices. It is
a writing format that allows us to communicate chords to other users,
and to the CharaChorder, without using any descriptions. You can find
the different symbols used in chord notation in the table below.

+-----------------+---------+------------------------------------------+
| Character Name  | Symbol  | Usage                                    |
+=================+=========+==========================================+
| Plus Operator   |    \+   | Used for separating inputs for chorded   |
|                 |         | operations                               |
+-----------------+---------+------------------------------------------+
| Vertical Bar    |    \|   | Used for separating all sequential       |
| Operator        |         | operations                               |
+-----------------+---------+------------------------------------------+
| Equal Sign      |    =    | Used for separating a chord input from a |
|                 |         | chord output                             |
+-----------------+---------+------------------------------------------+


You can read some examples of chords written in chord notation below.
You can try these chords on your CharaChorder device! 

* ``y+u+o = you``
* ``k+b+a = back``
* ``t+o+n+d = don’t``
* ``w+o+n+d = down``
* ``c+b = because`` 
* ``p+m+i = important``

How do I make Chords? 
------------------------

You can make chords for your
CharaChorder using a few different methods which we will discuss below.
In order to make a chord, you will have to indicate your desired
:ref:`chord input<Chord Input>` as well as your desired
:ref:`chord output<Chord Output>`.

Your CharaChorder device already comes with some chords loaded onto it.
These cover some of the most common words in the English language. You
can click on the link to see that list in an external tab: `Starter Chords <https://docs.google.com/spreadsheets/d/1G_A77DsyoM2hod3by2BzM7Wcj3JGJsmNw7dAz98wS3U/edit?usp=sharing>`_.


You can create custom chords on the :ref:`Device Manager<On Dot I/O>`,
Dot I/O. Additionally, you, can create chords on the go by using
:ref:`impulse chording<Impulse Chording>`. Read on for specific
instructions on how to do that. 

On Dot I/O
~~~~~~~~~~~~~

Dot I/O is our official Device Manager designed for CharaChorder devices. On there, you can do a
variety of things. You can read all about Dot I/O in this
:doc:`section<Device Manager>`.

The process for adding chords to your CharaChorder is the same on all of
our CharaChorder devices. You can
:ref:`add new chords<Adding New Chords on Device Manager>`, or
:ref:`import an existing chord library<Importing Chord Libraries on Device Manager>`.
Read how below. 

Adding New Chords on Device Manager
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.  On a chromium based browser, such as Chrome, go to the CharaChorder :doc:`device manager<Device Manager>` `Weblink <https://www.iq-eq.io/#/manager>`__
2.  Click “Connect”
3.  When the popup box comes up that reads “www.iq-eq.io wants to
    connect to a serial port”, choose your CharaChorder device, then
    click the blue “connect” button. You’ll know that you’re properly
    connected if you can see your device ID and CCOS version, similar to
    the following text:
    ``Device ID CHARACHORDER ONE M0 --- CCOS VERSION 1.1.1``
4.  Under the “Library” section, click the button labeled “Add Chord
    Map”. You should see a new box come up similar to the image below
5.  Click the blue “Edit Chord” button. You should notice the text boxes
    under “Output” and “Input” are now available to be typed in
6.  In the “Output” section, type in your desired
    :ref:`output<Chord Output>`
7.  In the “Input” section, press the keys that you want to use for your
    :ref:`chord input<Chord Input>`. You do not need to hold all the
    keys down at the same time. The order in which the keys are pressed
    is not :ref:`important<Chord Input>`. If you make a mistake, you
    can use the backspace to erase whatever you have typed so far
8.  Once you are satisfied with the :ref:`chord input<Chord Input>`
    and the :ref:`chord output<Chord Output>`, click the green “Save”
    button
9.  If you would like to add another chord, you can press the “Add Chord
    Map” again and repeat steps 5 through 8 for each additional entry.

Importing Chord Libraries on Device Manager
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In order to import an existing chord library, you will have to have to
CSV (comma separated values) file handy, already downloaded on your
computer. If you already have that file, follow the steps below.

1. On a chromium based browser, such as Chrome, go to the CharaChorder :doc:`device manager<Device Manager>` `Weblink <https://www.iq-eq.io/#/manager>`__
2. Click “Connect”
3. When the popup box comes up that reads “www.iq-eq.io wants to connect
   to a serial port”, choose your CharaChorder device, then click the
   blue “connect” button. You’ll know that you’re properly connected if
   you can see your device ID and CCOS version, similar to the following
   text: ``Device ID CHARACHORDER ONE M0 --- CCOS VERSION 1.1.1``
4. Under the “Library” section, click the button labeled “Import
   Library”. Click it
5. A window will open asking you to choose a file from your computer.
   Select the previously downloaded CSV file and click “open”
6. You should see the :doc:`device manager<Device Manager>` populate
   with the chord entries from the library. Wait a few minutes until all
   of the chord maps are imported
7. After a review of the chord maps, if you want to add them to your
   CharaChorder, click “Save All”
8. Count about two seconds per each chord entry before using your
   CharaChorder

WARNING: It’s possible that you will see a message similar to this one:
“Commit Progress: 33% Please do not touch your device until completion.”
The percentage might get stuck and never reach 100%. This is a known
bug. As long as you count two seconds per each chord entry before using
your CharaChorder, you should have no issues. 

Impulse chording
~~~~~~~~~~~~~~~~~~~

Impulse chording is a method of adding chords that doesn’t require
anything except your CharaChorder after a space to type in. It allows
you to create ‘on the fly’, custom chords which can be spontaneously
created anywhere that you can type via the Impulse menu.

The idea of impulse chords is that whenever you come across a word that
you don’t have a chord for, you can instantly create one mid-email,
mid-discord chat, mid-whatever, without the need to switch windows,
import, connect, etc. Just punch in your input and output via the
Impulse Menu and then keep typing without skipping a beat. Read below
for instructions on how to create an impulse chord on your specific
device.

Creating an Impulse Chord on the CharaChorder One
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Standard process for creating an impulse chord on a CharaChorder One: In
short: 1. CHORD INPUT, 2. CALL IMPULSE, 3. TYPE OUTPUT, 4. CONFIRM
OUTPUT 5. CONFIRM INPUT

.. _Impulse chording one:
.. image:: /assets/images/Impulsegif.gif
  :width: 1200
  :alt: Impulse chording on the CharaChorder One

1. Anywhere that you can see a cursor, chord the input you want
   (example: ``b+u+r+s+t``). You will either see a jumble of letters
   (example: “tsubr”) or you will see a chord which is already
   programmed to that input. If you continue, any conflicts will be
   overwritten.
2. Call the impulse command with either GTM >I<mpulse OR with the hard
   coded chord ``i+DUP``.
3. Follow the prompt and type your output in character entry mode.
   (example: >I<mpulse output: burst ).
4. Press enter to confirm your output.
5. Verify that the desired input is correct (you will see a confirmation
   message similar to this: >I<mpulse input(1): b + r + u + t + s).
6. If the input is incorrect, perform your desired input at this step.
   Once the input is the desired input, press enter.

These steps should take 1-3 seconds. 

Creating an Impulse Chord on the CharaChorder Lite
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Standard process for creating an impulse chord on a CharaChorder Lite:
In short: 1. CHORD INPUT, 2. CALL IMPULSE, 3. TYPE OUTPUT, 4. CONFIRM
OUTPUT, 5. CONFIRM INPUT

.. _Impulse chording lite:
.. image:: /assets/images/Impulsegif.gif
  :width: 1200
  :alt: Impulse chording on the CharaChorder Lite

1. Anywhere that you can see a cursor, chord the input you want
   (example: ``b+u+r+s+t``). You will either see a jumble of letters
   (example: “tsubr”) or you will see a chord which is already
   programmed to that input. If you continue, any conflicts will be
   overwritten.
2. Call the impulse command with either GTM >I<mpulse OR with the hard
   coded chord ``i+DUP``.
3. Follow the prompt and type your output in character entry mode.
   (example: >I<mpulse output: burst ).
4. Press enter to confirm your output.
5. Verify that the desired input is correct (you will see a confirmation
   message similar to this: >I<mpulse input(1): b + r + u + t + s).
6. If the input is incorrect, perform your desired input at this step.
   Once the input is the desired input, press enter.

These steps should take 1-3 seconds. 

Creating an Impulse Chord on the CharaChorder X
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Standard process for creating an impulse chord on a CharaChorder X: In
short: 1. CHORD INPUT, 2. CALL IMPULSE, 3. TYPE OUTPUT, 4. CONFIRM
OUTPUT, 5. CONFIRM INPUT

.. _Impulse chording X:
.. image:: /assets/images/Impulsexgif.gif
  :width: 1200
  :alt: Impulse chording on the CharaChorder X
  
1. Anywhere that you can see a cursor, chord the input you want
   (example: ``b+u+r+s+t``). You will either see a jumble of letters
   (example: “tsubr”) or you will see a chord which is already
   programmed to that input. If you continue, any conflicts will be
   overwritten.
2. Call the impulse command with either GTM >I<mpulse OR with the hard
   coded chord ``i+ESC``.
3. Follow the prompt and type your output in character entry mode.
   (example: >I<mpulse output: burst ).
4. Press enter to confirm your output.
5. Verify that the desired output is correct (you will see a
   confirmation message similar to this: >I<mpulse input(1): b + u + r +
   s + t).
6. If the input is incorrect, perform your desired input at this step.
   Once the input is the desired input, press enter.

These steps should take 1-3 seconds
