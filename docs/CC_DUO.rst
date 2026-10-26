======
CC DUO
======

Welcome to the Official **CC DUO** guide. You can select the links below to navigate to the topics that you find most relevant.

.. _CC DUO Image:
.. image:: /assets/images/CCDUO.jpg
   :width: 600
   :alt: CC DUO Dual-Cursor Companion Software

**CC DUO** is CharaChorder's dedicated desktop companion application for multi-ball, dual-wielding :doc:`Forge Trackball <Forge_Trackball>` setups. While a single Forge Trackball—or two trackballs controlling a single shared system pointer—operates 100% plug-and-play across Windows, macOS, and Linux without any additional software, **CC DUO** unlocks true **dual-cursor functionality**, independent left/right calibration, and specialized role splitting on Windows.

.. contents:: Table of Contents of this Page
   :local:

Software Overview & System Requirements
---------------------------------------

What is CC DUO?
^^^^^^^^^^^^^^^

Standard computer operating systems are designed around a single active mouse cursor. When you plug two standard pointing devices into a computer, the operating system merges their inputs into one shared pointer.

**CC DUO** is a lightweight, **native Windows desktop application** that runs in the background to give each connected :doc:`Forge Trackball <Forge_Trackball>` its own distinct on-screen cursor or specialized navigation role.

.. note::
   **When Do You Need CC DUO?**

   * **Standard Single-Cursor Use (No Software Needed)**: Hardware settings such as single-ball button mappings, DPI presets, and X/Y axis orientation are stored directly in your :doc:`Forge Trackball's <Forge_Trackball>` onboard :doc:`CCOS <CCOS>` memory and work across Windows, macOS, and Linux without CC DUO.
   * **Dual-Cursor & Multi-Ball Use (CC DUO Required)**: CC DUO must remain running in the background whenever you want **dual-cursor functionality**, independent dual-pointer colors, or multi-ball role splitting.

System Compatibility & Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: CC DUO Technical Specifications
   :widths: 35 65
   :header-rows: 1

   * - Attribute
     - Specification
   * - **Official Application Name**
     - **CC DUO**
   * - **Application Architecture**
     - Native Windows desktop application
   * - **Background Operation**
     - Must remain running in the background for dual-cursor functionality
   * - **Minimum Hardware Requirements**
     - Any Windows PC capable of supporting a standard USB HID mouse
   * - **CPU & Memory Footprint**
     - Minimal background CPU and RAM usage (engineered for zero cursor jitter or latency)
   * - **Administrator Privileges**
     - **Not required** (installs and runs without local administrator or root privileges)
   * - **Network & Privacy**
     - **100% Offline** (requires no internet connection, account login, cloud profile syncing, or telemetry)

.. note::
   **Cross-Platform Note**: While the :doc:`Forge Trackball <Forge_Trackball>` hardware works natively as a standard USB HID pointing device on all modern versions of **Windows, macOS, and Linux** (and is not designed or tested for mobile OSes), the **CC DUO** dual-cursor companion app is a **native Windows** application.

How the Dual-Pointer Engine Works
---------------------------------

Primary and Secondary Cursor Placeholders
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Because Windows restricts native system input to a single hardware pointer at the OS level, CC DUO manages concurrent dual pointers using a high-speed placeholder and warp architecture:

* **Dual Placeholders**: CC DUO renders a **primary cursor** and a **secondary cursor placeholder** on screen, tracking input from your left and right trackballs independently.
* **Instant Cursor Warping**: When you click with your secondary trackball, CC DUO rapidly warps the active OS cursor to the secondary placeholder's exact coordinates to execute the click seamlessly.

Window Focus & Multi-Window Workflows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Single Active Window Focus**: The operating system restricts active keyboard and window focus to **one window at a time**, meaning two separate windows cannot be actively dragged or typed into at the exact same millisecond.
* **Instant Click-to-Activate**: Clicking on any inactive window immediately activates and focuses it. With CC DUO, you can keep your secondary cursor floating over an inactive window—such as a reference document, communication app, or secondary monitor—ready to activate and interact with it at any time without moving your primary cursor across your display setup.

Visual Distinction & Cursor Customization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To help you immediately tell your left and right pointers apart on screen:

* **Customizable Cursor Colors**: Both pointers are customizable in color within CC DUO.
* **Default Secondary Color**: Out of the box, the secondary cursor defaults to **light blue**.

Feature Set & Configuration Options
-----------------------------------

Role Splitting
^^^^^^^^^^^^^^

In addition to using two independent point-and-click cursors, CC DUO supports **role splitting** across your two :doc:`Forge Trackballs <Forge_Trackball>`:

* **Primary Precision Pointer**: Dedicate one trackball to standard cursor movement and clicking.
* **Dedicated Navigation & Scrubbing Controller**: Configure the second trackball to act as a dedicated **2D/3D pan and scroll wheel**, **zoom controller**, or **timeline scrubber**—an ideal workflow for CAD, 3D modeling, audio/video editing, and large spreadsheets.

Dynamic Handover & Dominance Modes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When both trackballs are moved simultaneously, CC DUO lets you choose how their movements interact. All three multi-ball operating modes are supported:

1. **Priority / Dominance Handover**: One designated trackball takes priority whenever both balls are rolled at the same time.
2. **Coordinate Averaging**: Movement coordinates from both trackballs are averaged together into a combined vector.
3. **Completely Independent Operation**: Both pointers move independently across the screen at the same time without affecting one another.

Independent Speed, DPI & Acceleration Calibration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Every user has different dexterity between their left and right hands, or between thumb and fingertip grip styles. CC DUO allows you to calibrate each trackball separately:

* **Independent Sensitivity & DPI**: Set distinct cursor speeds for your left and right trackballs (for example, pairing a high-speed cursor on one hand with a low-DPI precision pointer on the other).
* **Independent Acceleration Curves**: Customize pointer acceleration curves separately for each module.

Profile Behavior
^^^^^^^^^^^^^^^^

* **Global Workspace Configuration**: CC DUO settings and mappings apply globally across your Windows environment. Automatic per-application profile switching (triggering different mappings when specific programs open) is not currently supported.
