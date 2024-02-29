Upgrade to CCOS
===============

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