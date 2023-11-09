.. vim: syntax=rst

DPC
===

功能描述
---------------------

DPC 全称为  Defect Pixel Correction，可以修正 Sensor 上有问题的坏点。

修正方法有两种，分别为静态校正与动态校正。

- 静态校正:校正时分为暗点校正与亮点校正。

  亮点校正时，把镜头遮黑，启动坏点标定程序。

  暗点校正时，不遮黑在平坦背景时如灰度箱前，调整曝光让图像整体亮度约为 50%.

  静态坏点最多允许 4095 个坏点。

- 动态校正:使用此方法时，不使用校正数据而是直接动态判断坏点，并且加以修正。在低噪时对画面偏色有帮助，但若强度太强可能会致画面细节降低。

API 参考
-------------------------

- `CVI_ISP_SetDPDynamicAttr`_： 设置动态坏点校正属性

- `CVI_ISP_GetDPDynamicAttr`_： 获取动态坏点校正属性

- `CVI_ISP_SetDPCalibrate`_： 设置静态坏点标定参数

- `CVI_ISP_GetDPCalibrate`_： 获取静态坏点标定参数

- `CVI_ISP_SetDPStaticAttr`_： 设置静态坏点校正属性

- `CVI_ISP_GetDPStaticAttr`_： 获取静态坏点校正属性

CVI_ISP_SetDPDynamicAttr
^^^^^^^^^^^^^^^^^^^^^^^^

【描述】

设置动态坏点校正属性

【语法】

.. code-block:: c

   CVI_S32 CVI_ISP_SetDPDynamicAttr(VI_PIPE ViPipe, const ISP_DP_DYNAMIC_ATTR_S *pstDPCDynamicAttr);

【参数】

.. list-table::
   :widths: 1 2 1
   :header-rows: 1

   * - 参数名称
     - 描述
     - 输入/输出

   * - ViPipe
     - VI_PIPE 号
     - 输入

   * - pstDPCDynamicAttr
     - 动态坏点校正属性
     - 输入

【返回值】

.. list-table::
  :widths: 1 2
  :header-rows: 1

  * - 返回值
    - 描述

  * - 0
    - 成功。

  * - 非 0
    - 失败，其值为 `错误码 <43_Error_Code.html#错误码>`__ 。

【需求】

-  头文件: cvi_isp.h, cvi_comm_isp.h

-  库文件: libisp.so

【注意】

无。

【举例】

无。

【相关主题】

- `CVI_ISP_GetDPDynamicAttr`_

CVI_ISP_GetDPDynamicAttr
^^^^^^^^^^^^^^^^^^^^^^^^

【描述】

获取动态坏点校正属性参数

【语法】

.. code-block:: c

   CVI_S32 CVI_ISP_GetDPDynamicAttr(VI_PIPE ViPipe, ISP_DP_DYNAMIC_ATTR_S *pstDPCDynamicAttr);

【参数】

.. list-table::
   :widths: 1 2 1
   :header-rows: 1

   * - 参数名称
     - 描述
     - 输入/输出

   * - ViPipe
     - VI_PIPE 号
     - 输入

   * - pstDPDynamicAttr
     - 静态坏点标定参数
     - 输出

【返回值】

.. list-table::
  :widths: 1 2
  :header-rows: 1

  * - 返回值
    - 描述

  * - 0
    - 成功。

  * - 非 0
    - 失败，其值为 `错误码 <43_Error_Code.html#错误码>`__ 。

【需求】

-  头文件: cvi_isp.h, cvi_comm_isp.h

-  库文件: libisp.so

【注意】

无。

【举例】

无。

【相关主题】

- `CVI_ISP_SetDPDynamicAttr`_

CVI_ISP_SetDPCalibrate
^^^^^^^^^^^^^^^^^^^^^^

【描述】

   设置静态坏点校正属性

【语法】

.. code-block:: c

   CVI_S32 CVI_ISP_SetDPCalibrate(VI_PIPE ViPipe, const ISP_DP_CALIB_ATTR_S *pstDPCalibAttr);

【参数】

.. list-table::
   :widths: 1 2 1
   :header-rows: 1

   * - 参数名称
     - 描述
     - 输入/输出

   * - ViPipe
     - VI_PIPE 号
     - 输入

   * - pstDPCalibrateAttr
     - 静态坏点校正属性
     - 输入

【返回值】

.. list-table::
  :widths: 1 2
  :header-rows: 1

  * - 返回值
    - 描述

  * - 0
    - 成功。

  * - 非 0
    - 失败，其值为 `错误码 <43_Error_Code.html#错误码>`__ 。

【需求】

-  头文件: cvi_isp.h, cvi_comm_isp.h

-  库文件: libisp.so

【注意】

无。

【举例】

无。

【相关主题】

- `CVI_ISP_GetDPCalibrate`_

CVI_ISP_GetDPCalibrate
^^^^^^^^^^^^^^^^^^^^^^

【描述】

获取静态坏点标定参数

【语法】

.. code-block:: c

   CVI_S32 CVI_ISP_GetDPCalibrate(VI_PIPE ViPipe, ISP_DP_CALIB_ATTR_S *pstDPCalibAttr);

【参数】

.. list-table::
   :widths: 1 2 1
   :header-rows: 1

   * - 参数名称
     - 描述
     - 输入/输出

   * - ViPipe
     - VI_PIPE 号
     - 输入

   * - pstDPCalibrateAttr
     - 静态坏点标定参数
     - 输出

【返回值】

.. list-table::
  :widths: 1 2
  :header-rows: 1

  * - 返回值
    - 描述

  * - 0
    - 成功。

  * - 非 0
    - 失败，其值为 `错误码 <43_Error_Code.html#错误码>`__ 。

【需求】

-  头文件: cvi_isp.h, cvi_comm_isp.h

-  库文件: libisp.so

【注意】

无。

【举例】

无。

【相关主题】

- `CVI_ISP_SetDPCalibrate`_

CVI_ISP_SetDPStaticAttr
^^^^^^^^^^^^^^^^^^^^^^^

【描述】

设置静态坏点校正属性

【语法】

.. code-block:: c

   CVI_S32 CVI_ISP_SetDPStaticAttr(VI_PIPE ViPipe, const ISP_DP_STATIC_ATTR_S *pstDPStaticAttr);

【参数】

.. list-table::
   :widths: 1 2 1
   :header-rows: 1

   * - 参数名称 描述
     - 描述
     - 输入/输出

   * - ViPipe
     - VI_PIPE 号
     - 输入

   * - pstDPStaticAttr
     - 静态坏点校正属性
     - 输入

【返回值】

.. list-table::
  :widths: 1 2
  :header-rows: 1

  * - 返回值
    - 描述

  * - 0
    - 成功。

  * - 非 0
    - 失败，其值为 `错误码 <43_Error_Code.html#错误码>`__ 。

【需求】

-  头文件: cvi_isp.h, cvi_comm_isp.h

-  库文件: libisp.so

【注意】

无。

【举例】

无。

【相关主题】

- `CVI_ISP_GetDPStaticAttr`_

CVI_ISP_GetDPStaticAttr
^^^^^^^^^^^^^^^^^^^^^^^

【描述】

   获取静态坏点校正属性

【语法】

.. code-block:: c

   CVI_S32 CVI_ISP_GetDPStaticAttr(VI_PIPE ViPipe, ISP_DP_STATIC_ATTR_S *pstDPStaticAttr);

【参数】

.. list-table::
   :widths: 1 2 1
   :header-rows: 1

   * - 参数名称
     - 描述
     - 输入/输出

   * - ViPipe
     - VI_PIPE 号
     - 输入

   * - pstDPStaticAttr
     - 静态坏点校正属性
     - 输出

【返回值】

.. list-table::
  :widths: 1 2
  :header-rows: 1

  * - 返回值
    - 描述

  * - 0
    - 成功。

  * - 非 0
    - 失败，其值为 `错误码 <43_Error_Code.html#错误码>`__ 。

【需求】

-  头文件: cvi_isp.h, cvi_comm_isp.h

-  库文件: libisp.so

【注意】

无。

【举例】

无。

【相关主题】

`CVI_ISP_SetDPStaticAttr`_

数据类型
----------------------------

- `ISP_DP_DYNAMIC_MANUAL_ATTR_S`_： 动态坏点校正手动属性

- `ISP_DP_DYNAMIC_AUTO_ATTR_S`_： 动态坏点校正自动属性

- `ISP_DP_DYNAMIC_ATTR_S`_： 动态坏点校正属性

- `ISP_DP_CALIB_ATTR_S`_： 静态坏点标定参数

- `ISP_DP_STATIC_ATTR_S`_： 静态坏点校正属性

ISP_DP_DYNAMIC_MANUAL_ATTR_S
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

【说明】

动态坏点校正手动属性

【定义】

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

【成员】

.. list-table::
   :widths: 1 2
   :header-rows: 1

   * - 成员名称
     - 描述

   * - ClusterSize
     - 群         聚坏点面积上限，值越高越能修正群聚坏点，但可能会造成高频区域解像力的衰减

       取值范围： [0x0, 0x3]

       数据类型： CVI_U8

   * - BrightDefectToNormalPixRatio
     - 可视亮坏点值与周围像素的倍率 (Q4.4)

       取值范围： [0x0, 0xff]

       数据类型： CVI_U8

   * - DarkDefectToNormalPixRatio
     - 可视暗坏点值与周围像素的倍率 (Q4.4)

       取值范围： [0x0, 0xff]

       数据类型： CVI_U8

   * - FlatThreR
     - R通道判别  平坦区临界值，值越小越能保留边缘信息

       取值范围： [0x0, 0xff]

       数据类型： CVI_U8

   * - FlatThreG
     - G通道判别  平坦区临界值，值越小越能保留边缘信息

       取值范围： [0x0, 0xff]

       数据类型： CVI_U8

   * - FlatThreB
     - B通道判别  平坦区临界值，值越小越能保留边缘信息

       取值范围： [0x0, 0xff]

       数据类型： CVI_U8

   * - FlatThreMinG
     - G通道判别平坦区最小临界值

       取值范围： [0x0, 0xff]

       数据类型： CVI_U8

   * - FlatThreMinRB
     - RB通道判别平坦区最小临界值

       取值范围： [0x0, 0xff]

       数据类型： CVI_U8

【注意事项】

无。

【相关数据类型及接口】

- `CVI_ISP_SetDPDynamicAttr`_

- `CVI_ISP_GetDPDynamicAttr`_

ISP_DP_DYNAMIC_AUTO_ATTR_S
^^^^^^^^^^^^^^^^^^^^^^^^^^

【说明】

动态坏点校正自动属性

【定义】

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

【成员】

.. list-table::
   :widths: 1 2
   :header-rows: 1

   * - 成员名称
     - 描述

   * - ClusterSize
     - 群         聚坏点面积上限，值越高越能修正群聚坏点，但可能会造成高频区域解像力的衰减

       取值范围： [0x0, 0x3]

       数据类型： CVI_U8

   * - BrightDefectToNormalPixRatio
     - 可视亮坏点值与周围像素的倍率 (Q4.4)

       取值范围： [0x0, 0xff]

       数据类型： CVI_U8

   * - DarkDefectToNormalPixRatio
     - 可视暗坏点值与周围像素的倍率 (Q4.4)

       取值范围： [0x0, 0xff]

       数据类型： CVI_U8

   * - FlatThreR
     - R通道判别  平坦区临界值，值越小越能保留边缘信息

       取值范围： [0x0, 0xff]

       数据类型： CVI_U8

   * - FlatThreG
     - G通道判别  平坦区临界值，值越小越能保留边缘信息

       取值范围： [0x0, 0xff]

       数据类型： CVI_U8

   * - FlatThreB
     - B通道判别  平坦区临界值，值越小越能保留边缘信息

       取值范围： [0x0, 0xff]

       数据类型： CVI_U8

   * - FlatThreMinG
     - G通道判别平坦区最小临界值

       取值范围： [0x0, 0xff]

       数据类型： CVI_U8

   * - FlatThreMinRB
     - RB通道判别平坦区最小临界值

       取值范围： [0x0, 0xff]

       数据类型： CVI_U8

【注意事项】

无。

【相关数据类型及接口】

- `CVI_ISP_SetDPDynamicAttr`_

- `CVI_ISP_GetDPDynamicAttr`_

ISP_DP_DYNAMIC_ATTR_S
^^^^^^^^^^^^^^^^^^^^^

【说明】

动态坏点校正属性

【定义】

.. code-block:: c

  typedef struct _ISP_DP_DYNAMIC_ATTR_S {
    CVI_BOOL Enable;
    CVI_U32 DynamicDPCEnable;
    ISP_OP_TYPE_E enOpType;
    CVI_U8 UpdateInterval;
    ISP_DP_DYNAMIC_MANUAL_ATTR_S stManual;
    ISP_DP_DYNAMIC_AUTO_ATTR_S stAuto;
  } ISP_DP_DYNAMIC_ATTR_S;

【成员】

.. list-table::
   :widths: 1 2
   :header-rows: 1

   * - 成员名称
     - 描述

   * - Enable
     - DPC模块使能

       0： 关闭

       1： 使能

       取值范围： [0, 1]

       数据类型： CVI_BOOL

   * - DynamicDPCEnable
     - 动态坏点校正功能使能

       数据类型： CVI_U32

   * - enOpType
     - 工作类型

       OP_TYPE_AUTO: 自动模式

       OP_TYPE_MANUAL: 手动模式

   * - UpdateInterval
     - 影响参数更新间隔,              值越大画面变化越慢, 效能越好。

       取值范围： [0x0, 0xff]

       数据类型： CVI_U8

   * - stManual
     - 手动模式下参数

   * - stAuto
     - 自动模式下参数

【注意事项】

无。

【相关数据类型及接口】

- `CVI_ISP_SetDPDynamicAttr`_

- `CVI_ISP_GetDPDynamicAttr`_

ISP_DP_CALIB_ATTR_S
^^^^^^^^^^^^^^^^^^^

【说明】

静态坏点标定参数

【定义】

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

【成员】

.. list-table::
   :widths: 1 2
   :header-rows: 1

   * - 成员名称
     - 描述

   * - EnableDetect
     - 静态坏点标定使能

       取值范围： [0, 1]

       数据类型： CVI_BOOL

   * - StaticDPType
     - 静态坏点标定类型

       取值范围： [0x0, 0x1]

       数据类型： CVI_STATIC_DP_TYPE_E

   * - StartThresh
     - 静态坏点标定开始时的检测门限值

       取值范围： [0x0, 0xff]

       数据类型： CVI_U8

   * - CountMax
     - 允许静态坏点的最大个数

       取值范围： [0x0, 0xfff]

       数据类型： CVI_U16

   * - CountMin
     - 允许静态坏点的最小个数

       取值范围： [0x0, 0xfff]

       数据类型： CVI_U16

   * - TimeLimit
     - 允许标定超时门限值

       取值范围： [0x0, 0x640]

       数据类型： CVI_U16

   * - saveFileEn
     - 是否保存raw图

       取值范围： [0, 1]

       数据类型： CVI_BOOL

   * - Table[4096]
     - 只读， 亮暗坏点坐标值查找表，低 29bit有效， [12:0]bit 为坏点的水平坐标，  [28:16]bit 为坏点的垂直坐标

       取值范围： [0x0, 0x1fff1fff]

       数据类型： CVI_U32

   * - FinishThresh
     - 只读， 静态坏点标定结束时的检测门限值

       取值范围： [0x0, 0xff]

       数据类型： CVI_U8

   * - Count
     - 只读， 标定出的静态坏点的个数

       取值范围： [0x0, 0xfff]

       数据类型： CVI_U16

   * - Status
     - 只读， 静态坏点标定结果状态信息

       取值范围： [0x0, 0x2]

       数据类型： ISP_STATUS_E

【注意事项】

无。

【相关数据类型及接口】

- `CVI_ISP_SetDPCalibrate`_

- `CVI_ISP_GetDPCalibrate`_

ISP_DP_STATIC_ATTR_S
^^^^^^^^^^^^^^^^^^^^

【说明】

静态坏点校正属性

【定义】

.. code-block:: c

  typedef struct _ISP_DP_STATIC_ATTR_S {
    CVI_BOOL Enable;
    CVI_U16 BrightCount;
    CVI_U16 DarkCount;
    CVI_U32 BrightTable[STATIC_DP_COUNT_MAX];
    CVI_U32 DarkTable[STATIC_DP_COUNT_MAX];
    CVI_BOOL Show;	// not support yet
  } ISP_DP_STATIC_ATTR_S;

【成员】

.. list-table::
   :widths: 1 2
   :header-rows: 1

   * - 成员名称
     - 描述

   * - Enable
     - 静态坏点DPC使能

       0： 关闭

       1： 使能

       取值范围： [0, 1]

       数据类型： CVI_BOOL

   * - BrightCount
     - 亮坏点个数

       取值范围： [0x0, 0xfff]

       数据类型： CVI_U16

   * - DarkCount
     - 暗坏点个数

       取值范围： [0x0, 0xfff]

       数据类型： CVI_U16

   * - BrightTable[4095]
     - 亮坏点坐标信息，低 29bit 有效，     [12:0]bit 为坏点水平坐标，[28:16]bit为坏点垂直坐标。

       取值范围： [0x0, 0x1fff1fff]

       数据类型： CVI_U32

   * - DarkTable[4095]
     - 暗的坏点坐标值，低 29bit 有效，     [12:0]bit 为坏点水平坐标，[28:16]bit为坏点垂直坐标。

       取值范围： [0x0, 0x1fff1fff]

       数据类型： CVI_U32

   * - Show
     - 静态坏点显示使能 not support yet

       取值范围： [0, 1]

       数据类型： CVI_BOOL

【注意事项】

无。

【相关数据类型及接口】

- `CVI_ISP_SetDPStaticAttr`_

- `CVI_ISP_GetDPStaticAttr`_
