.. _Layout:

Layout
======

Design of the layout
--------------------

The keys were by far the most time and iteration intensive part of designing the CharaChorder.
Riley Keen, CEO of CharaChorder, said that it was 80% science, 20% art.

However, trying to validate or prove that any layout is better than others,
like we have seen with the QWERTY keyboard,
is very complex and it is not a simple answer.

One of the big benefits of the CC1, CC2, or the M4G (Master Forge), is that you are actually using your thumbs.
On the smartphone, your thumbs can type almost as fast as all of your other fingers together combined,
and yet on a normal keyboard layout they are both tethered to a single button.

So, a design goal was to maximize left vs right hand and finger vs thumb alterations as well as
to pair the frequent keys with the ease of press-ability. This was a highly iterative process which filled up notebooks and notebooks of design sketches.

In general the process that Riley used and recommends using if you would like to make your own layout is as follows:

1. Make a list of individual inputs for your language weighted by their frequency of use in your favorite corpus
2. Make a list of most common bigrams and trigrams (groups of 2 and 3 letters) for your language weighted by their frequency of use in your favorite corpus
3. Make a list of most common words for your language weighted by their frequency of use in your favorite corpus
4. Create a list prioritizing each switch on your device based on how easy they are to access. This should consider both finger, direction, and handedness
5. To create a seed, sync your switch list with the individual input list, placing your most common input on the easiest switch to access, while doing your best to balance the total utilization of all left versus right hand inputs
6. Based on your seed, analyze the lists of bigrams and trigrams and note which ones require rolling inputs, antipodal inputs, same finger inputs, same hand non-rolling inputs, as well as same hand/finger trajectory inputs. Assign a scale to tokenize each of these input types and create a cumulative ranking for each bigram and trigram
7. Based on your seed, create a chord library. Now give each chord a rating based on how easy it is to physically accomplish, and how easy it is to remember or memorize
8. Analyze the weaknesses and strengths of your layout, then create a hypothesis of what could be changed within your seed to improve the total rating of all your bigrams, trigrams, and chords.
9. Shuffle your seed based on your hypothesis and repeat steps 5-9 until you are no longer able to improve upon your score

Layout quirks
-------------

TL;DR, so what does this mean for me?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First of all, here are some pitfalls

* If you set for example `$`, the CCOS types this as "hold shift press 4 release shift".
  Meaning if you press `$` and `3` together, **you'll actually type "$#" instead of "$3"**
  because the CCOS needs to hold shift for typing the `$` sign
  - *Avoid putting characters that need shift and normal characters on the same layer*
* Using for example a German layout on the OS will swap z and y, just like on a normal keyboard.
* Using any non-ASCII, non-Chara, non-keyboard characters will *only* work on Windows.
* The hacks used by Chara can have unexpected consequences in some programs which intercept raw input

.. tip::
  The easiest solution is
  use `US-Intl <https://en.m.wikipedia.org/wiki/QWERTY#US-International>`_ on your OS.
  You can use right-alt to access special characters.
  Holding right-alt and pressing `q` will give you an `ä`.

The other solution is to use your local layout and mentally remap. So if you wanted to type the Cyrillic `Ф`, you set the Russian layout on your OS, and map the key to `a` (which will send the key-code that corresponds to Ф on a Russian layout)

What's even going on?
^^^^^^^^^^^^^^^^^^^^^

Intuitively you'd expect keyboards to send the letter that's printed on the key pressed to the system. However, unfortunately that's not the case. There is *no way* for any device to tell the OS which letter should be typed, on any operating system.

Keyboards send what's called a **key-code** to the operating system, which is the ID of the key pressed. This key-code stands in no relation to the actual letter typed, it's up to the OS to turn it into an actual character. This mapping is described by a keyboard layout, which *cannot* be set by the device itself, it *must* be applied on your operating system.

The only convention here is *where* the keys are located - *on a standard layout keyboard*. There are a few standardized locations based on the US keyboard layout, like the ASCII character set, the GUI/Windows key, CTRL, SHIFT etc. However all or most of these assume a US-Layout.

There is no standard for other typing input devices,  nor is there a way for the device to know what layout is selected by the OS.

How does CharaChorder deal with this?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you set a layout on the CCOS, it moves the key-code locations around.

.. warning::
  Setting the letter `a` on a switch doesn't actually send "print a" to the computer - it sends a "key where the a would be on the us layout pressed" to the OS**.

So how can I add äöüß etc. when it's not on the US layout?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There is a special feature on Windows that allows you to directly type *any* Unicode character with your keyboard, by holding `alt` and typing a numeric code.

.. warning::
  Setting the letter `ä` on a switch means the device sends "hold alt press 0 press 2 press 2 press 8 release alt".

Because this is a Windows feature, this only works on Windows. However even this is *not* layout agnostic. Using a layout that moves letters around, like Programmer Dvorak, will completely mess up this hack as well.

There are similar workarounds for Linux and Mac, but as of now not supported by CCOS.

The "real" solution
^^^^^^^^^^^^^^^^^^^

The best solution is always to rely on the OS mapping.

Windows, Mac and Linux all offer options to create custom layouts.

* Windows: `MSKCL <https://www.microsoft.com/en-us/download/details.aspx?id=102134>`_
* Mac: `Ukelele <https://software.sil.org/ukelele/>`_
* Linux: `xkb <https://wiki.archlinux.org/index.php/X_keyboard_extension>`_
