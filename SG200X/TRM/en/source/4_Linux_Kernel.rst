.. vim: syntax=rst

Linux Kernel
============

The kernel code can be found in the In sdk_source directory

.. code-block:: console

  sdk_source/linux    // version 4.19, cv182xA, ca53 32bit CPU 
  sdk_source/linux_5.10  // cv180x,cv181x C906B 64 bit CPU


Set Kernel DTS
--------------

If you want to increase or decrease the kernel module, you can do it by modifying DTS(\*1).
Each EVB will have a dts file to define its device tree.Such as cv1800b_wevb_0008a_spinor, its DTS file is defined in the file path as follows:

.. code-block:: console

  $ cat build/boards/cv180x/cv1800b_wevb_0008a_spinor/dts_riscv/
  cv1800b_wevb_0008a_spinor.dts
  /dts-v1/;
  #include "cv180x_base_arm.dtsi"
  #include "cv180x_asic_bga.dtsi"
  #include "cv180x_asic_spinor.dtsi"
  #include "cv180x_default_memmap.dtsi"

  / {

  // add your customized device description

  };


The above \*.
dtsi (device tree source include files) is the preset value of the chip, and it is not recommended to change it directly.
To modify the preset value, it is recommended to use the(delete node)method.

(\*1) U-boot and kernel use common DTS

Setup kernel configuration
--------------------------

If you want to modify the configuration of the kernel, you can directly modify the kernel configuration file.Such as cv1800b_wevb_0008a_spinor, The
defconfig file is defined in the file path as follows

.. code-block:: console

  $ cat build/boards/cv180x/cv1800b_wevb_0008a_spinor/linux/
  cvitek_cv1800b_wevb_0008a_spinor_defconfig
  # CONFIG_SWAP is not set
  CONFIG_SYSVIPC=y
  CONFIG_POSIX_MQUEUE=y
  CONFIG_NO_HZ_IDLE=y
  CONFIG_HIGH_RES_TIMERS=y
  CONFIG_PREEMPT=y
  CONFIG_IKCONFIG=y
  CONFIG_IKCONFIG_PROC=y
  CONFIG_LOG_BUF_SHIFT=15
  CONFIG_CC_OPTIMIZE_FOR_SIZE=y



-  Example of using the method to modify the defconfig file (add support for SPI driver)

.. code-block:: console

  #
  # SPI drivers
  #
  # CONFIG_SPI is not set
  # CONFIG_SPI_MASTER is not set
  # CONFIG_SPI_DESIGNWARE is not set
  # CONFIG_SPI_DW_MMIO is not set
  # CONFIG_SPI_SPIDEV is not set
  CONFIG_SPI=y
  CONFIG_SPI_MASTER=y
  CONFIG_SPI_DESIGNWARE=y


-  Use the way like command line----setconfig_kernel

   ::

      $ setconfig_kernel SPI=y
      $ setconfig_kernel SPI_MASTER=y
      $ setconfig_kernel SPI_DESIGNWARE=y


-  Use the way like Graphic user interface line - menuconfig_kernel

  .. image:: media/im1.png
    :width: 6in
    :height: 5in
    

