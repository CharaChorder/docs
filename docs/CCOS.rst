CharaChorder Operating System (CCOS)
====================================

**CCOS (CharaChorder Operating System)** is the world’s first operating system built
for intelligent keyboards. The lines between what is a computer and what is an 
input device have been blurred, and will continue to be blurred to the point 
that terminology like 'firmware' is no longer accurate or adequate.

CCOS offers an unprecedented level of control, efficiency, and optimization, 
and will be compatible with all past, present, and future CharaChorder devices, 
as well as every device powered by :doc:`CharaChorder Engine`. CCOS guarantees 
consistent performance across all devices and enhances the ability of our team 
to introduce new features, fix bugs, as well as respond to feedback more 
efficiently with a convergent and spearheaded approach. In addition to the 
introduction of importable and exportable settings, inside your 
:doc:`Generative Text Menu (GTM)<GenerativeTextMenu>` you'll find new 
configurable settings including programmable debounce, arpeggiate tolerances, 
and even a customizable scan rate. Specialized 'hard coded' chords which were 
previously immutable can now be edited, including chords only available in 
spurring. Even modifier keys can now be repurposed as constituent inputs for 
any possible chord output by permanently overriding their derivative output 
on-the-fly via :ref:`impulse<Chords:Impulse chording>`. CCOS also brings with it the introduction of advanced 
arpeggiates, which are high staccato individual keystrokes which can enhance 
chords with modifiers, prefixes, suffixes, or punctuation.

If that's not exciting enough... this is only the tip of the iceberg. Here are 
some things you can expect to experience moving forward as we peel back the 
layers and start to unlock the full potential of CCOS with future updates:

- Compound Chording, the ability for any chord combination in any 
  layout to be compounded with up to twelve other chords, with each compounding 
  layer being tied to its own unique output.
- An interface for programming advanced keyboard/mouse macros which can be 
  assigned to either individual switches or chord outputs
- Soon, the only limitation for chord length will be the memory on your 
  device due to the new CCOS architecture's capability to link together an 
  infinite number of memory locations to a single chord output.
- Increased independence of CharaChorder devices, including the ability of 
  future generation devices to operate in the complete absence of an external computer.
- More sophisticated mouse and cursor control, and future generation devices 
  which function as a total mouse replacement, even for (and especially for) 
  activities which require high precision/high speed cursor control such as 
  gaming, modeling, & design.

CCOS was not designed for any one product, or even for a portfolio of products.
In alignment with our :doc:`mission<CharaChorder's Mission>` to get the whole 
world typing at the speed of thought, CCOS was built as a platform which anyone 
can adopt or build upon, with possibilities that are only limited by the human 
imagination. Do you want to publish your own DataHand inspired 
:doc:`CharaChorder One<CharaChorder One>` layout? Do you want to utilize fluid 
chorded/character entry in tandem with layouts/theories developed for velotype 
or stenography on your :doc:`CharaChorder Lite<CharaChorder_Lite>`? Do you want 
to introduce the world's first 1-Dimensional keyboard layout designed for both 
character entry and chorded entry? What about a creative combination of all of 
the above which utilizes 100% custom hardware? No problem. This is all possible 
with CCOS.

Thank you for your interest in CharaChorder OS.  We look forward to unleashing 
a keyboard revolution and redefining the limits of human-computer interaction!

Upgrade to CCOS
***************

.. danger::
    These instructions are only for those that had a device shipped before 2023 
    and that wish to update to CCOS. For all other CCOS updates, see 
    :ref:`the device manager page<Device Manager:Updating Your Device>`.

Part I - Back up chord library and update device
------------------------------------------------

#. Go to https://launchpad.charachorder.com/#/manager in a Google Chrome or other Chromium browser
#. Click the ‘Connect’ button, then select your device
#. You can confirm your device is properly connected if you see something like "Device: CHARACHORDER, firmware: 0.9.5"
#. Click the ‘Download Chords’ button and wait for the table to populate. This could take a few minutes.
#. Click ‘Export Library’ to export a .csv file to your machine (The file should be called: “CharaChorder_ChordLibrary.csv”)
#. Once you are absolutely sure your library is exported properly, and ALL of your chords are present in the file, click the ‘Delete All Chords’’ button.
#. Refresh the page, reconnect your device via steps 2-3, and click the ‘Bootloader’ button. A file explorer window should open on Windows. On Mac you may need to find your device as an external drive
#. Download your update file from this site: `<https://www.charachorder.com/pages/update-your-firmware>`__

    .. warning::
        You'll notice that there are two different versions of the CharaChorder 
        Lite. Please be sure to download the version that corresponds to your 
        device, whether it's M0 or S2. If you have a CharaChorder Lite that was 
        delivered before October 1st, 2022 you will need to use the file which 
        corresponds to the MO chipset. Otherwise CharaChorder Lite users should 
        use the S2 chipset.

    .. danger::
        Make sure that the file you download is named exactly
        like this: ``CURRENT.UF2``. If there are any other characters in the
        file name, the file will not work. ``CURRENT(1).UF2`` will NOT work.
        Additionally, the file name is case-sensitive; all letters must be
        capitalized.

#. Drag the UF2 file into the file explorer window and confirm that you would like to replace the existing file.
#. The file explorer window should automatically close



Part II - Migrate your chord library
------------------------------------

#. Follow the steps to restore your library on the new device manager by following the steps on the Device Manager page for :ref:`restoring from backup<Device Manager:Restoring from a Backup>`. Note, that although it says the file type should be .json, the .csv file downloaded will work.