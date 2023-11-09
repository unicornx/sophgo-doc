.. vim: syntax=rst

DPC
===

Function Overview
-----------------

DPC, the abbreviation for Defect Pixel Correction, can fix the bad points of problems on Sensor.

There are two methods of correction, static correction and dynamic correction.

- Static correction:The correction can fall into two categories, dark spot correction and bright spot correction.
  In the bright spot correction, the lens is blacked out and the bad point calibration procedure is started.
  In the dark spot correction, when the background is flat, such as before the gray box, adjust the exposure to make the overall brightness of the
  image about 50%.
  The static bad points allow no more than 4095 bad points.

- Dynamic correction: Under this method, the bad points are judged dynamically and corrected rather than using the correction data.
  In low noise situation, it is helpful for color deviation, but if the intensity is too strong, the details of the picture may be reduced.

API Reference
-------------

-  `CVI_ISP_SetDPDynamicAttr`_: Set dynamic bad point correction attributes

-  `CVI_ISP_GetDPDynamicAttr`_: Get dynamic bad point correction attributes

-  `CVI_ISP_SetDPCalibrate`_: Set static bad point calibration parameters

-  `CVI_ISP_GetDPCalibrate`_: Get static bad point calibration parameters

-  `CVI_ISP_SetDPStaticAttr`_: Set static bad point correction attributes

-  `CVI_ISP_GetDPStaticAttr`_: Get static bad point correction attributes

CVI_ISP_SetDPDynamicAttr
~~~~~~~~~~~~~~~~~~~~~~~~

[Description]

   Set dynamic bad point correction attributes.

[Syntax]

.. code-block:: c

   CVI_S32 CVI_ISP_SetDPDynamicAttr(VI_PIPE ViPipe, const ISP_DP_DYNAMIC_ATTR_S *pstDPCDynamicAttr);

[Parameter]

.. list-table::
   :widths: 1 2 1
   :header-rows: 1


   * - Parameter
     - Description
     - Input / Output

   * - ViPipe
     - VI_PIPE number 
     - Input

   * - pstDPCDynamicAttr
     - Dynamic bad point correction attribute
     - Input

[Return Value]

.. list-table:: 
  :widths: 1 2
  :header-rows: 1

  * - Return Value
    - Description

  * - 0
    - Success

  * - Non 0
    - Failure. An error code is returned. For details, see chapter `Error_Codes <Error_Codes.html#Error_Codes>`__ .


[Requirement]

-  Header files: cvi_isp.h, cvi_comm_isp.h

-  Library files: libisp.so

[Note]

   None

[Example]

   None

[Related Topic]

- `CVI_ISP_GetDPDynamicAttr`_

CVI_ISP_GetDPDynamicAttr
~~~~~~~~~~~~~~~~~~~~~~~~

[Description]

   Get dynamic bad point correction attributes

[Syntax]

.. code-block:: c

   CVI_S32 CVI_ISP_GetDPDynamicAttr(VI_PIPE ViPipe, ISP_DP_DYNAMIC_ATTR_S *pstDPCDynamicAttr);

[Parameter]

.. list-table::
   :widths: 1 2 1
   :header-rows: 1


   * - Parameter
     - Description
     - Input / Output

   * - ViPipe
     - VI_PIPE number                   
     - Input 

   * - pstDPDynamicAttr
     - Static bad point calibration parameters
     - Output

[Return Value]

.. list-table:: 
  :widths: 1 2
  :header-rows: 1

  * - Return Value
    - Description

  * - 0
    - Success

  * - Non 0
    - Failure. An error code is returned. For details, see chapter `Error_Codes <Error_Codes.html#Error_Codes>`__ .



[Requirement]

-  Header files: cvi_isp.h, cvi_comm_isp.h

-  Library files: libisp.so

[Note]

   None

[Example]

   None

[Related Topic]

- `CVI_ISP_SetDPDynamicAttr`_

CVI_ISP_SetDPCalibrate
~~~~~~~~~~~~~~~~~~~~~~

[Description]

   Set static bad point calibration parameters

[Syntax]

.. code-block:: c

   CVI_S32 CVI_ISP_SetDPCalibrate(VI_PIPE ViPipe, const ISP_DP_CALIB_ATTR_S *pstDPCalibAttr);

[Parameter]

.. list-table::
   :widths: 1 2 1
   :header-rows: 1


   * - Parameter
     - Description
     - Input / Output

   * - ViPipe
     - VI_PIPE number                   
     - Input 

   * - pstDPCalibrateAttr
     - Static bad point calibration parameters
     - Input


[Return Value]

.. list-table:: 
  :widths: 1 2
  :header-rows: 1

  * - Return Value
    - Description

  * - 0
    - Success

  * - Non 0
    - Failure. An error code is returned. For details, see chapter `Error_Codes <Error_Codes.html#Error_Codes>`__ .



[Requirement]

-  Header files: cvi_isp.h, cvi_comm_isp.h

-  Library files: libisp.so

[Note]

   None

[Example]

   None

[Related Topic]

- `CVI_ISP_GetDPCalibrate`_

CVI_ISP_GetDPCalibrate
~~~~~~~~~~~~~~~~~~~~~~

[Description]

   Get calibration parameters of static bad points

[Syntax]

.. code-block:: c

   CVI_S32 CVI_ISP_GetDPCalibrate(VI_PIPE ViPipe, ISP_DP_CALIB_ATTR_S *pstDPCalibAttr);

[Parameter]

.. list-table::
   :widths: 1 2 1
   :header-rows: 1


   * - Parameter
     - Description
     - Input / Output

   * - ViPipe
     - VI_PIPE number 
     - Input

   * - pstDPCalibrateAttr
     - Static bad point calibration parameters  
     - Output


[Return Value]

.. list-table:: 
  :widths: 1 2
  :header-rows: 1

  * - Return Value
    - Description

  * - 0
    - Success

  * - Non 0
    - Failure. An error code is returned. For details, see chapter `Error_Codes <Error_Codes.html#Error_Codes>`__ .


[Requirement]

-  Header files: cvi_isp.h, cvi_comm_isp.h

-  Library files: libisp.so

[Note]

   None

[Example]

   None

[Related Topic]

- `CVI_ISP_SetDPCalibrate`_

CVI_ISP_SetDPStaticAttr
~~~~~~~~~~~~~~~~~~~~~~~

[Description]

Set static bad point correction attribute.

[Syntax]

.. code-block:: c

   CVI_S32 CVI_ISP_SetDPStaticAttr(VI_PIPE ViPipe, const ISP_DP_STATIC_ATTR_S *pstDPStaticAttr);

[Parameter]

.. list-table::
   :widths: 1 2 1
   :header-rows: 1


   * - Parameter
     - Description
     - Input / Output

   * - ViPipe
     - VI_PIPE number 
     - Input

   * - pstDPStaticAttr
     - Static bad point calibration parameters
     - Input


[Return Value]

.. list-table:: 
  :widths: 1 2
  :header-rows: 1

  * - Return Value
    - Description

  * - 0
    - Success

  * - Non 0
    - Failure. An error code is returned. For details, see chapter `Error_Codes <Error_Codes.html#Error_Codes>`__ .


[Requirement]

-  Header files: cvi_isp.h, cvi_comm_isp.h

-  Library files: libisp.so

[Note]

   None.

[Example]

   None.

[Related Topic]

- `CVI_ISP_GetDPStaticAttr`_

CVI_ISP_GetDPStaticAttr
~~~~~~~~~~~~~~~~~~~~~~~

[Description]

Get static bad point correction attribute.

[Syntax]

.. code-block:: c

   CVI_S32 CVI_ISP_GetDPStaticAttr(VI_PIPE ViPipe, ISP_DP_STATIC_ATTR_S *pstDPStaticAttr);

[Parameter]

.. list-table::
   :widths: 1 2 1
   :header-rows: 1


   * - Parameter
     - Description
     - Input / Output

   * - ViPipe
     - VI_PIPE number 
     - Input

   * - pstDPStaticAttr
     - Static bad point calibration parameters  
     - Output


[Return Value]

.. list-table:: 
  :widths: 1 2
  :header-rows: 1

  * - Return Value
    - Description

  * - 0
    - Success

  * - Non 0
    - Failure. An error code is returned. For details, see chapter `Error_Codes <Error_Codes.html#Error_Codes>`__ .



[Requirement]

-  Header files: cvi_isp.h, cvi_comm_isp.h

-  Library files: libisp.so

[Note]

   None.

[Example]

   None.

[Related Topic]

- `CVI_ISP_SetDPStaticAttr`_

Data Types
-------------

-  `ISP_DP_DYNAMIC_MANUAL_ATTR_S`_: Manual attribute of dynamic bad point correction

-  `ISP_DP_DYNAMIC_AUTO_ATTR_S`_: Automatic attributes of dynamic bad point correction

-  `ISP_DP_DYNAMIC_ATTR_S`_: Dynamic bad point correction attribute

-  `ISP_DP_CALIB_ATTR_S`_: Static bad point calibration parameters

-  `ISP_DP_STATIC_ATTR_S`_: Static bad point correction attribute

ISP_DP_DYNAMIC_MANUAL_ATTR_S
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

[Description]

   Manual attribute of dynamic bad point correction.

[Syntax]

.. code-block:: c

  typedef struct _ISP_DP_DYNAMIC_MANUAL_ATTR_S {
    CVI_U8 ClusterSize;
    CVI_U8 BrightDefectToNormalPixRatio;
    CVI_U8 DarkDefectToNormalPixRatio;
    CVI_U8 FlatThreR;
    CVI_U8 FlatThreG;
    CVI_U8 FlatThreB;
    CVI_U8 FlatThreMinG;
    CVI_U8 FlatThreMinRB;
  } ISP_DP_DYNAMIC_MANUAL_ATTR_S;



[Member]

.. list-table::
   :widths: 1 2
   :header-rows: 1


   * - Member
     - Description

   * - ClusterSize
     - the upper limit of the area of clustering bad points;  the higher the value is, the better the correction effect is, but it may cause the attenuation of resolution in high frequency region

 
       
       
       Value range: [0x0, 0x3]


       
       
       Data type: CVI_U8
         

   * - BrightDefectToNormalPixRatio
     - The ratio between the value of visible bright and bad points and the surrounding pixels (Q4.4)

 
       
       
       Value range: [0x0, 0xff]


       
       
       Data type: CVI_U8
         

   * - DarkDefectToNormalPixRatio
     - The ratio between the value of visible dark and bad points and the surrounding pixels (Q4.4)

 
       
       
       Value range: [0x0, 0xff]


       
       
       Data type: CVI_U8
        

   * - FlatThreR
     - critical value of R-channel in flat area;the smaller the critical value, the more edge information can be preserved

 
       
       
       Value range: [0x0, 0xff]


       
       
       Data type: CVI_U8
         

   * - FlatThreG
     - critical value of G-channel in flat area;the smaller the critical value, the more edge information can be preserved

 
       
       
       Value range: [0x0, 0xff]


       
       
       Data type: CVI_U8
          

   * - FlatThreB
     - critical value of B-channel in flat area;the smaller the critical value, the more edge information can be preserved

 
       
       
       Value range: [0x0, 0xff]


       
       
       Data type: CVI_U8
          

   * - FlatThreMinG
     - the minimum critical value of g-channel judging flat area

 
       
       
       Value range: [0x0, 0xff]


       
       
       Data type: CVI_U8

    

   * - FlatThreMinRB
     - the minimum critical value of RB-channel judging flat area

 
       
       
       Value range: [0x0, 0xff]


       
       
       Data type: CVI_U8
     


[Note]

   None.

[Related Data Type and Interface]

- `CVI_ISP_SetDPDynamicAttr`_

- `CVI_ISP_GetDPDynamicAttr`_



ISP_DP_DYNAMIC_AUTO_ATTR_S
~~~~~~~~~~~~~~~~~~~~~~~~~~

[Description]

   Automatic attributes of dynamic bad point correction.

[Syntax]

.. code-block:: c

  typedef struct _ISP_DP_DYNAMIC_AUTO_ATTR_S {
    CVI_U8 ClusterSize[ISP_AUTO_ISO_STRENGTH_NUM];
    CVI_U8 BrightDefectToNormalPixRatio[ISP_AUTO_ISO_STRENGTH_NUM];
    CVI_U8 DarkDefectToNormalPixRatio[ISP_AUTO_ISO_STRENGTH_NUM];
    CVI_U8 FlatThreR[ISP_AUTO_ISO_STRENGTH_NUM];
    CVI_U8 FlatThreG[ISP_AUTO_ISO_STRENGTH_NUM];
    CVI_U8 FlatThreB[ISP_AUTO_ISO_STRENGTH_NUM];
    CVI_U8 FlatThreMinG[ISP_AUTO_ISO_STRENGTH_NUM];
    CVI_U8 FlatThreMinRB[ISP_AUTO_ISO_STRENGTH_NUM];
  } ISP_DP_DYNAMIC_AUTO_ATTR_S;


[Member]

.. list-table::
   :widths: 1 2
   :header-rows: 1


   * - Member
     - Description

   * - ClusterSize
     - the upper limit of the area of clustering bad points;  the higher the value is, the better the correction effect is, but it may cause the attenuation of resolution in high frequency region

       
       Value range: [0x0, 0x3]

       
       Data type: CVI_U8

           

   * - BrightDefectToNormalPixRatio
     - The ratio between the value of visible bright and bad points and the surrounding pixels (Q4.4)

       
       Value range: [0x0, 0xff]

       
       Data type: CVI_U8

      

   * - DarkDefectToNormalPixRatio
     - The ratio between the value of visible dark and bad points and the surrounding pixels (Q4.4)

       
       Value range: [0x0, 0xff]

       
       Data type: CVI_U8

          

   * - FlatThreR
     - critical value of R-channel in flat area;the smaller the critical value, the more edge information can be preserved

       
       Value range: [0x0, 0xff]

       
       Data type: CVI_U8

          

   * - FlatThreG
     - critical value of G-channel in flat area;the smaller the critical value, the more edge information can be preserved

       
       Value range: [0x0, 0xff]

       
       Data type: CVI_U8

    

   * - FlatThreB
     - critical value of B-channel in flat area;the smaller the critical value, the more edge information can be preserved

       
       Value range: [0x0, 0xff]

       
       Data type: CVI_U8

         

   * - FlatThreMinG
     - the minimum critical value of g-channel judging flat area

       
       Value range: [0x0, 0xff]

       
       Data type: CVI_U8

       

   * - FlatThreMinRB
     - the minimum critical value of RB-channel judging flat area

       
       Value range: [0x0, 0xff]

       
       Data type: CVI_U8

     

[Note]

   None.

[Related Data Type and Interface]

- `CVI_ISP_SetDPDynamicAttr`_

- `CVI_ISP_GetDPDynamicAttr`_

ISP_DP_DYNAMIC_ATTR_S
~~~~~~~~~~~~~~~~~~~~~

[Description]

   Dynamic bad point correction attribute.

[Syntax]

.. code-block:: c

  typedef struct _ISP_DP_DYNAMIC_ATTR_S {
    CVI_BOOL Enable;
    CVI_U32 DynamicDPCEnable;
    ISP_OP_TYPE_E enOpType;
    CVI_U8 UpdateInterval;
    ISP_DP_DYNAMIC_MANUAL_ATTR_S stManual;
    ISP_DP_DYNAMIC_AUTO_ATTR_S stAuto;
  } ISP_DP_DYNAMIC_ATTR_S;


[Member]

.. list-table::
   :widths: 1 2
   :header-rows: 1


   * - Member
     - Description

   * - Enable
     - The DPC module enable

       0: off

       1: enable

       
       Value range: [0, 1]

       Data type: CVI_BOOL
        

   * - DynamicDPCEnable
     - Enable dynamic dead point correction function

       Data type: CVI_U32
           

   * - enOpType
     - Operation type

       OP_TYPE_AUTO: automatic mode

       OP_TYPE_MANUAL: manual mode
     

   * - UpdateInterval
     - Affects the parameter update interval, the larger the value, the slower the screen changes and the better the performance.

       
       Value range: [0x0, 0xff]

       Data type: CVI_U8
         

   * - stManual
     - Parameters in manual mode                

   * - stAuto
     - Parameters in automatic mode           


[Note]

   None.

[Related Data Type and Interface]

- `CVI_ISP_SetDPDynamicAttr`_

- `CVI_ISP_GetDPDynamicAttr`_



ISP_DP_CALIB_ATTR_S
~~~~~~~~~~~~~~~~~~~

[Description]

   Static bad point calibration parameters.

[Syntax]

.. code-block:: c

  typedef struct _ISP_DP_CALIB_ATTR_S {
    CVI_BOOL EnableDetect;
    CVI_STATIC_DP_TYPE_E StaticDPType;
    CVI_U8 StartThresh;
    CVI_U16 CountMax;
    CVI_U16 CountMin;
    CVI_U16 TimeLimit;
    CVI_BOOL saveFileEn;

    // read only
    CVI_U32 Table[STATIC_DP_COUNT_MAX];
    CVI_U8 FinishThresh;
    CVI_U16 Count;
    ISP_STATUS_E Status;
  } ISP_DP_CALIB_ATTR_S;


[Member]

.. list-table::
   :widths: 1 2
   :header-rows: 1


   * - Member
     - Description

   * - EnableDetect
     - Static bad point calibration enablement;

       Value range: [0, 1]

       Data type: CVI_BOOL
        

   * - StaticDPType
     - Static bad point calibration type;

       Value range: [0x0, 0x1]

       Data type: CVI_STATIC_DP_TYPE_E


   * - StartThresh
     - Detection threshold at the beginning of static bad point calibration;

       Value range: [0x0, 0xff]

       Data type: CVI_U8
       

   * - CountMax
     - Maximum number of allowed static bad points;

       Value range: [0x0, 0xfff]

       Data type: CVI_U16
          

   * - CountMin
     - Minimum number of allowed static bad points;

       Value range: [0x0, 0xfff]

       Data type: CVI_U16
          

   * - TimeLimit
     - Allowable calibration timeout threshold;

       Value range: [0x0, 0x640]

       Data type: CVI_U16
          

   * - saveFileEn
     - Whether to save the raw image

       Value range: [0, 1]

       Data type: CVI_BOOL
         

   * - Table[4096]
     - Read only, look-up table of bright and dark bad point coordinate values; low 29bit is valid, [12:0] bit is the horizontal coordinate of the bad point, and [28:16] bit is the vertical coordinate of the bad point;

       Value range: [0x0, 0x1ff1fff]

       Data type: CVI_U32



   * - FinishThresh
     - Read only, the detection threshold at the end of static bad point calibration;

       Value range: [0x0, 0xff]

       Data type: CVI_U8
             

   * - Count
     - Read only, the number of calibrated static bad points;

       Value range: [0x0, 0xfff]

       Data type: CVI_U16
           

   * - Status
     - Read only, static bad point calibration result status information;

       Value range: [0x0, 0x2]

       Data type: ISP_STATUS_E
     

[Note]

   None.

[Related Data Type and Interface]

- `CVI_ISP_SetDPCalibrate`_

- `CVI_ISP_GetDPCalibrate`_



ISP_DP_STATIC_ATTR_S
~~~~~~~~~~~~~~~~~~~~

[Description]

   Static bad point calibration attributes.

[Syntax]

.. code-block:: c

  typedef struct _ISP_DP_STATIC_ATTR_S {
    CVI_BOOL Enable;
    CVI_U16 BrightCount;
    CVI_U16 DarkCount;
    CVI_U32 BrightTable[STATIC_DP_COUNT_MAX];
    CVI_U32 DarkTable[STATIC_DP_COUNT_MAX];
    CVI_BOOL Show;	// not support yet
  } ISP_DP_STATIC_ATTR_S;


[Member]

.. list-table::
   :widths: 1 2
   :header-rows: 1


   * - Member
     - Description

   * - Enable
     - DPC module enablement; 

       0: close 
       1: enable

       Value range: [0, 1]

       Data type: CVI_BOOL

         

   * - BrightCount
     - Number of bright and bad points;

       Value range: [0x0, 0xfff]

       Data type: CVI_U16
          

   * - DarkCount
     - Number of dark and bad point;

       Value range: [0x0, 0xfff]

       Data type: CVI_U16
         

   * - BrightTable[4095]
     - Coordinate information of bright and bad points; the low 29bit is valid, the [12:0] bit is the horizontal coordinate of the bad point, and the [28:16] bit is the vertical coordinate of the bad point.

       Value range: [0x0, 0x1ff1fff]

       Data type: CVI_U32



   * - DarkTable[4095]
     - the coordinate value of dark point; the low 29bit is effective, [12:0] bit is the horizontal coordinates of the bad point, and [28:16] bit is the vertical coordinates of the bad point.

       Value range: [0x0, 0x1ff1fff]

       Data type: CVI_U32



   * - Show
     - Static bad point display enablement is not supported yet.

       Value range: [0, 1]

       Data type: CVI_BOOL
         


[Note]

   None.




- `CVI_ISP_SetDPStaticAttr`_

- `CVI_ISP_GetDPStaticAttr`_
