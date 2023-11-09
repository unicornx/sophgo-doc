.. vim: syntax=rst

Root file system (rootfs)
=========================

Introduction about root file system
-----------------------------------

``Please refer to the SDK_Compilation_and_Usage_Guide - Chapter 5 root file system (rootfs)``


Busybox support
---------------

At present, the file system uses BusyBox v1.27.1.
If you need to update busybox, you can put the compiled busybox in the following path:

.. code-block:: console

   $ ramdisk/rootfs/common_musl_riscv64/bin/busybox  // CV181X
   $ ramdisk/rootfs/common_musl_riscv64/bin/busybox  // CV180X
