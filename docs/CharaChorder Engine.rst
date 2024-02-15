CharaChorder Engine
===================

Welcome to the Official CharaChorder Engine guide. You can select the links
below to navigate to the topics that you find most relevant.

.. _CCE:
.. image:: /assets/images/CharaChorderEngine.jpg
  :width: 1200
  :alt: CharaChorder Engine

CharaChorder Engine is a multichip module that enables you to build your own 
CCOS powered text entry device. If you are interested in learning how to utilize
CharaChorder Engine, please visit the `CharaChorder Engine Discord channel <https://discord.gg/VngNWSyZJb>`_ 
and ping Riley Keen or Matt Swarts.

.. contents:: Table of Contents of this Page
   :local:

Pinout Diagram
**************

.. _CCEPinout:
.. image:: /assets/cce/pinout.png
  :width: 1200
  :alt: CharaChorder Engine pinout table

Design
******

The Engine is designed primarily to work with a MCU to receive inputs (through 
UART and later I2C or SPI), process the chording logic, query the onboard chordmap
library, and output the results back to the MCU (again over UART and later I2C or
SPI). However, the layout of the Engine exposes USB pins, which could have a future
capability for direct USB HID output. This could be limiting for some developers,
as they may want to control their HID reports themselves through their MCU.

Physical footprint
------------------

`Here is a zip file <https://drive.google.com/file/d/1B5MwTrgjcbVu-GyUrb3xXM8vcKKkh0U-/view?usp=drive_link>`__
that contains a step file as well as KiCad files for the CharaChorder Engine
that can be used to aid you in the design of your CCOS powered keyboard. 

Communicating with Engine Devices
*********************************

Like other CCOS powered devices, any device with CharaChorder Engine can use the 
full power of the :doc:`Serial API<SerialAPI>`. 