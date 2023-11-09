根文件系统(rootfs)
========================================================================

根文件系统简介
------------------------------------------------------------------------

::

   请参阅 SDK 编译及使用说明 – Chapter 5 根文件系统(rootfs)



Busybox 支援
------------------------------------------------------------------------

目前文件系统内部使用BusyBox v1.27.1版本，如果有更新busybox的需求，可以将编
译好的busybox 放到下列路径 :

.. code-block:: console

   $ ramdisk/rootfs/common_musl_riscv64/bin/busybox  // CV181X
   $ ramdisk/rootfs/common_musl_riscv64/bin/busybox  // CV180X
