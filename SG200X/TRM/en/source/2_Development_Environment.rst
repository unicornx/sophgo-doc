.. vim: syntax=rst

Development environment
=======================

Purpose
-------

This document describes the Linux development environment.
Setting up of Linux development environment, U-boot, Linux kernel, root file system (rootfs), programming of kernel and root file system burning, as
well as creating a network development environment and starting Linux development.This document provides a user terminal that can quickly build a
Linux environment and port self-developed applications to Linux above the operating system.

How to compile the kernel
-------------------------

-  To compile the SDK in the ubuntu environment on the HOST side, you need to install the following tools:

   ``Please refer to the SDK compilation and use instructions_V1.0.docx to build compilation environment``


   -  1) Set environment variables ( example: v1800b_wevb_0008a_spinor)

      .. code-block:: console

         -	$ source build/cvisetup.sh
         -	  -------------------------------------------------------------------------
         -	    Usage:
         -	    (1) menuconfig - Use menu to configure your board.
         -	        ex: $ menuconfig
         -	
         -	    (2) defconfig $CHIP_ARCH - List EVB boards($BOARD) by CHIP_ARCH.
         -	       ** cv183x ** -> ['cv1829', 'cv1832', 'cv1835', 'cv1838', 'cv9520', 'cv7581']
         -	       ** cv182x ** -> ['cv1820', 'cv1821', 'cv1822', 'cv1823', 'cv1825', 'cv1826', 'cv7327', 'cv7357']
         -	       **   cv181x ** -> ['cv181x', 'cv1823a', 'cv1821a', 'cv1820a', 'cv1811h', 'cv1811c', 'cv1810c', 'cv1812h']
         -	       ** cv180x ** -> ['cv180x', 'cv1800b', 'cv1800c', 'cv1801b', 'cv1801c']
         -	        ex: $ defconfig cv183x
         -	
         -	    (3) defconfig $BOARD - Choose EVB board settings.
         -	        ex: $ defconfig cv1835_wevb_0002a
         -	        ex: $ defconfig cv1826_wevb_0005a_spinand
         -	        ex: $ defconfig cv181x_fpga_c906
         -	  --------------------------------------------------------------------------
        
   -  2) Select EVB cv1800b_wevb_0008a_spinor

      .. code-block:: console

         $ defconfig cv1800b_wevb_0008a_spinor
         Run defconfig function 
         Loaded configuration '/workspace/build/boards/cv180x/cv1800b_wevb_0008a_spinor/cv1800b_wevb_0008a_spinor_defconfig'
         No change to configuration in '.config'
         Loaded configuration '.config'
         ====== Environment Variables ======= 
           PROJECT: cv1800b_wevb_0008a_spinor, DDR_CFG=ddr2_1333_x16
           CHIP_ARCH: cv180x, DEBUG=0
           SDK VERSION: musl_riscv64, RPC=0
           ATF options: ATF_KEY_SEL=default, BL32=1
           Linux source folder: linux_5.10, Uboot source folder: u-boot-2021.10
           CROSS_COMPILE_PREFIX: riscv64-unknown-linux-musl-
           ENABLE_BOOTLOGO: 0
           Flash layout xml: /workspace/build/boards/cv180x/ cv1800b_wevb_0008a_spinor/partition/partition_spinor.xml
           Sensor tuning bin: gcore_gc4653
           Output path: /workspace/master/install/ soc_cv1800b_wevb_0008a_spinor



   -  3) Compile linux kernel

      .. code-block:: console

         $ build_kernel
         [TARGET] kernel-dts 
         ......
         [TARGET] kernel-build
         ......


   -  4) Generate images boot.{spinor, spinand, emmc}

      .. code-block:: console

         $ ls install/soc_cv1800b_wevb_0008a_spinor/boot.spinor
         install/soc_cv1800b_wevb_0008a_spinor/boot.spinor



