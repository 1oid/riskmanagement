from django.db import models


class UserDevice(models.Model):
    """
    计算机信息表
    """
    DId = models.TextField(default="", verbose_name="计算ID")
    DMac = models.TextField(default="", verbose_name="Mac地址")
    DIp = models.TextField(default="", verbose_name="IP地址")
    DName = models.TextField(default="", verbose_name="计算机名")
    UName = models.TextField(default="", verbose_name="用户名")
    DSystem = models.TextField(default="", verbose_name="计算机系统")
    Remarks = models.TextField(default="", verbose_name="备注")
    Other = models.TextField(default="", verbose_name="数据写入时间")

    def __str__(self):
        return self.DMac


class UserApplication(models.Model):
    """
    软件安装表
    """
    AName = models.TextField(default="", verbose_name="软件名")
    AVer = models.TextField(default="", verbose_name="软件版本")
    ACompany = models.TextField(default="", verbose_name="软件厂家")
    AInTime = models.TextField(default="", verbose_name="安装时间")
    AUninstall = models.TextField(default="", verbose_name="软件卸载信息")    # 不显示
    AALink = models.TextField(default="", verbose_name="软件网址")
    AILink = models.TextField(default="", verbose_name="软件信息网址")
    AULink = models.TextField(default="", verbose_name="软件更新地址")
    Other = models.TextField(default="", verbose_name="数据写入时间")

    def __str__(self):
        return self.AName


class UserDevHistory(models.Model):
    """
    USB设备记录表
    """
    DName = models.TextField(default="", verbose_name="USB设备名称")
    SNumber = models.TextField(default="", verbose_name="USB设备序号")
    UseTime = models.TextField(default="", verbose_name="USB设备使用时间")
    DType = models.TextField(default="", verbose_name="USB设备类型")
    Other = models.TextField(default="", verbose_name="数据写入时间")

    def __str__(self):
        return self.DName


class UserFileCopy(models.Model):
    """
    文件拷贝
    """
    Did = models.TextField(default="", verbose_name="计算机ID")
    VName = models.TextField(default="", verbose_name="USB设备卷名")
    DName = models.TextField(default="", verbose_name="USB设备名称")
    DModel = models.TextField(default="", verbose_name="USB设备厂家")
    SNumber = models.TextField(default="", verbose_name="USB设备序号")
    Action = models.IntegerField(default=0, verbose_name="1拷入U盘、2拷出U盘")
    ATime = models.TextField(default="", verbose_name="操作时间")
    FileName = models.TextField(default="", verbose_name="文件名")
    FileSize = models.IntegerField(default=0, verbose_name="大小")
    FIleMD5 = models.TextField(default="", verbose_name="MD5")
    FileAttribute = models.TextField(default="", verbose_name="文件属性（可能是时间）")
    FileDesc = models.TextField(default="", verbose_name="文件描述")
    Other = models.TextField(default="", verbose_name="数据写入时间")

    def __str__(self):
        return self.VName


class UserRecords(models.Model):
    """
    文件访问记录表
    """
    AccTime = models.TextField(default="", verbose_name="文件访问时间")
    FileName = models.TextField(default="", verbose_name="文件名")
    FilePath = models.TextField(default="", verbose_name="文件路径")
    FileType = models.IntegerField(default=0, verbose_name="0文件不存在， 1文件，2目录")
    Other = models.TextField(default="", verbose_name="数据写入时间")

    def __str__(self):
        return self.FileName


class UserBroFile(models.Model):
    """
    文件下载表
    """
    Did = models.TextField(default="", verbose_name="计算机ID")
    Domain = models.TextField(default="", verbose_name="域名")
    Ip = models.TextField(default="", verbose_name="IP")
    PName = models.TextField(default="", verbose_name="进程（全路径）")
    FileName = models.TextField(default="", verbose_name="下载文件名")
    FileSize = models.IntegerField(default=0, verbose_name="下载文件大小")
    FileMd5 = models.TextField(default="", verbose_name="下载文件MD5")
    FCTime = models.TextField(default="", verbose_name="下载文件创建时间")
    KeyDesc = models.TextField(default="", verbose_name="描述")
    sTag = models.IntegerField(default=0, verbose_name="1敏感文件、2木马文件")
    Other = models.TextField(default="", verbose_name="数据写入时间")

    def __str__(self):
        return self.Did


class UserNetWork(models.Model):
    """
    网络信息表
    """
    Did = models.TextField(default="", verbose_name="计算机ID")
    Domain = models.TextField(default="", verbose_name="域名")
    IP = models.TextField(default="", verbose_name="IP")
    Port = models.IntegerField(default=0, verbose_name="端口")
    PName = models.TextField(default="", verbose_name="进程名")
    FileMd5 = models.TextField(default="", verbose_name="进程MD5")
    IpName = models.TextField(default="", verbose_name="IP的地域")
    IsHost = models.IntegerField(default=0, verbose_name="是不是本地")
    IpAddress = models.TextField(default="", verbose_name="IP归属")
    Action = models.IntegerField(default=0, verbose_name="国内还是国外")
    xAddress = models.IntegerField(default=0, verbose_name="精度")
    yAddress = models.IntegerField(default=0, verbose_name="精度")
    Other = models.TextField(default="", verbose_name="数据写入时间")

    def __str__(self):
        return self.Did


class UserServices(models.Model):
    PID = models.IntegerField(default=0, verbose_name="进程ID")
    SName = models.TextField(default="", verbose_name="服务名")
    IName = models.TextField(default="", verbose_name="服务进程路径")
    SCommand = models.TextField(default="", verbose_name="服务参数")
    DName = models.TextField(default="", verbose_name="服务描述")
    OName = models.TextField(default="", verbose_name="服务用户组")
    Status = models.TextField(default="", verbose_name="服务当前状态")
    StartUp = models.TextField(default="", verbose_name="服务是手动不是自动启")
    SDesc = models.TextField(default="", verbose_name="服务描述")
    FVer = models.TextField(default="", verbose_name="文件版本")
    FPName = models.TextField(default="", verbose_name="文件厂家")
    FCName = models.TextField(default="", verbose_name="文件公司")
    FDesc = models.TextField(default="", verbose_name="文件描述")
    DllName = models.TextField(default="", verbose_name="DLL信息")
    IsRun = models.IntegerField(default=0, verbose_name="是否启动")
    Other = models.TextField(default="", verbose_name="数据写入时间")

    def __str__(self):
        return self.SName


class UserDevAccess(models.Model):
    Did = models.TextField(default="", verbose_name="计算机ID")
    VName = models.TextField(default="", verbose_name="USB设备卷名")
    DName = models.TextField(default="", verbose_name="USB设备名")
    DModel = models.TextField(default="", verbose_name="USB设备厂家")
    SNumber = models.TextField(default="", verbose_name="USB设备序列号")
    DSize = models.IntegerField(default=0, verbose_name="USB设备大小")
    DAction = models.IntegerField(default=0, verbose_name="1插入中、2已拔出")
    Ctime = models.TextField(default="", verbose_name="插入时间")
    Dtime = models.TextField(default="", verbose_name="拔出时间")
    DType = models.IntegerField(default=0, verbose_name="是什么类别，移动盘还是U盘")
    DStatus = models.IntegerField(default=0, verbose_name="状态")
    Other = models.TextField(default="", verbose_name="数据写入时间")

    def __str__(self):
        return self.VName


class CacheFile(models.Model):
    identifier = models.TextField(default="", verbose_name="设备标志")
    CacheName = models.TextField(default="", verbose_name="CacheName")
    FileName = models.TextField(default="", verbose_name="")
    JpgFileName = models.TextField(default="", verbose_name="")
    ZipName = models.TextField(default="", verbose_name="")
    FileEx = models.TextField(default="", verbose_name="")
    SaveName = models.TextField(default="", verbose_name="")
    MD5 = models.TextField(default="", verbose_name="")
    FileSize = models.IntegerField(default=0, verbose_name="")
    ZipFileSize = models.IntegerField(default=0, verbose_name="")
    JpgFileSize = models.IntegerField(default=0, verbose_name="")
    UpSize = models.IntegerField(default="", verbose_name="")
    IsOK = models.TextField(default="", verbose_name="")
    IsZip = models.IntegerField(default=0, verbose_name="")
    IsImge = models.IntegerField(default=0, verbose_name="")
    InsterTime = models.TextField(default="", verbose_name="")

    def __str__(self):
        return self.identifier


class UserFile(models.Model):
    """
    文件记录表，文件风控
    智慧-打印
    """
    Did = models.TextField(default="", verbose_name="计算机ID")
    FileType = models.IntegerField(default=0, verbose_name="1敏感文档 2木马")
    KeyDesc = models.TextField(default="", verbose_name="命中关键字")
    ContentRemark = models.TextField(default="", verbose_name="摘要")
    FileName = models.TextField(default="", verbose_name="文件名")
    FileSize = models.IntegerField(default=0, verbose_name="文件大小")
    FileTag = models.IntegerField(default=0, verbose_name="1敏感、2木马、3重复、4打印、6伪装")
    IsDup = models.IntegerField(default=0, verbose_name="是否重复")
    FileMd5 = models.TextField(default="", verbose_name="文件MD5", unique=True)
    FileAttribute = models.TextField(default="", verbose_name="文件属性")
    FileNumber = models.IntegerField(default=0, verbose_name="文件访问次数")
    FileDesc = models.TextField(default="", verbose_name="文件描述")
    PName = models.TextField(default="", verbose_name="进程名")
    PUName = models.TextField(default="", verbose_name="进程用户名")
    PPID = models.IntegerField(default=0, verbose_name="进程父PID")
    PPName = models.TextField(default="", verbose_name="进程父进程名")
    Other = models.TextField(default="", verbose_name="数据写入时间")

    def __str__(self):
        return self.FileName


class UserProcess(models.Model):
    """
    进程信息表
    """
    Did = models.TextField(default="", verbose_name="计算机ID")
    PID = models.IntegerField(default=0, verbose_name="进程ID")
    PName = models.TextField(default="", verbose_name="进程名")
    PCmd = models.TextField(default="", verbose_name="进程参数")
    PSession = models.IntegerField(default=0, verbose_name="进程SessionID")
    PUser = models.TextField(default="", verbose_name="进程用户名")
    PMem = models.IntegerField(default=0, verbose_name="进程使用内存")
    PIO = models.IntegerField(default=0, verbose_name="进程使用IO速率")
    PVer = models.TextField(default="", verbose_name="进程版本")
    PStart = models.TextField(default="", verbose_name="进程创建时间")
    Verified = models.TextField(default="", verbose_name="进程签名")
    IsVerified = models.IntegerField(default=0, verbose_name="进程是否签名")
    Other = models.TextField(default="", verbose_name="数据写入时间")

    def __str__(self):
        return self.PName


class UserStartup(models.Model):
    """
    开机启动表
    """
    KRoot = models.TextField(default="", verbose_name="注册表主键")
    KName = models.TextField(default="", verbose_name="注册表名")
    KValue = models.TextField(default="", verbose_name="进程表值")
    FName = models.TextField(default="", verbose_name="文件名")
    FCommand = models.TextField(default="", verbose_name="文件参数")
    FCName = models.TextField(default="", verbose_name="文件厂家")
    Verified = models.TextField(default="", verbose_name="文件签名")
    IsVerified = models.IntegerField(default=0, verbose_name="文件是否签名")
    Other = models.TextField(default="", verbose_name="数据写入时间")
    
    def __str__(self):
        return self.KName


class IntelliAnalysis(models.Model):
    action_choice = [
        (0, "下载"),
        (1, "打印"),
        (2, "拷贝"),
        (3, "外发")
    ]

    did = models.TextField(default=0, verbose_name="计算机ID")
    filename = models.TextField(verbose_name="文件名")
    filepath = models.TextField(verbose_name="文件路径")
    filesize = models.IntegerField(default=0, verbose_name="文件大小")
    md5 = models.TextField(verbose_name="MD5")
    description = models.TextField(default="", verbose_name="描述")
    duplicate = models.BooleanField(default=False, verbose_name="是否重复")
    # filetype = models.IntegerField(default=0, verbose_name="0文件不存在， 1文件，2目录")
    action = models.IntegerField(choices=action_choice, verbose_name="行为")
    Other = models.DateTimeField(auto_now_add=True, verbose_name="操作时间")

    def __str__(self):
        return self.md5

    def get_action_string(self):
        return self.action_choice[self.action][1]

#
#
# class PcInfo(models.Model):
#     PcName = models.TextField(default="", verbose_name="PcName")
#     UserName = models.TextField(default="", verbose_name="UserName")
#     PcMac = models.TextField(default="", verbose_name="PcMac")
#     PcIp = models.TextField(default="", verbose_name="PcIp")
#     PcOs = models.TextField(default="", verbose_name="PcOs")
#     Location = models.TextField(default="", verbose_name="Location")
#     InsterTime = models.TextField(default="", verbose_name="InsterTime")
#
#     def __str__(self):
#         return self.PcName
#
#
# class ProcList(models.Model):
#
#     PID = models.IntegerField(default=0, verbose_name="PID")
#     ProcName = models.TextField(default="", verbose_name="ProcName")
#     ProcCmd = models.TextField(default="", verbose_name="ProcCmd")
#     ProcSession = models.IntegerField(default=0, verbose_name="ProcSession")
#     ProcUser = models.TextField(default="", verbose_name="ProcUser")
#     ProcMem = models.IntegerField(default=0, verbose_name="ProcMem")
#     ProcIO = models.IntegerField(default=0, verbose_name="ProcIO")
#     ProVer = models.TextField(default="", verbose_name="ProVer")
#     Created = models.TextField(default="", verbose_name="Created")
#     Verified = models.TextField(default="", verbose_name="Verified")
#     IsSinge = models.IntegerField(default=0, verbose_name="IsSinge")
#     InsterTime = models.TextField(default="", verbose_name="InsterTime")
#
#     def __str__(self):
#         return self.PID
#
#
# class WinUser(models.Model):
#     UserName = models.TextField(default="", verbose_name="UserName")
#     UserTime = models.TextField(default="", verbose_name="UserTime")
#     InsterTime = models.TextField(default="", verbose_name="InsterTime")
#     IsCurrent = models.IntegerField(default=0, verbose_name="IsCurrent")
#
#     def __str__(self):
#         return self.UserName
#
#
# class Recents(models.Model):
#     AccTime = models.TextField(default="", verbose_name="AccTime")
#     FileName = models.TextField(default="", verbose_name="FileName")
#     FilePath = models.TextField(default="", verbose_name="FilePath")
#     FileType = models.IntegerField(default=0, verbose_name="FileType")
#     InsterTime = models.TextField(default="", verbose_name="InsterTime")
#
#     def __str__(self):
#         return self.AccTime
#
#
# class fileinfo(models.Model):
#     file_type = models.IntegerField(default=0, verbose_name="1敏感文件，2木马文件")
#     task_id = models.TextField(default="", verbose_name="task_id")
#     rule_id = models.TextField(default="", verbose_name="rule_id")
#     rule_feature = models.TextField(default="", verbose_name="rule_feature")
#     rule_keyword = models.TextField(default="", verbose_name="rule_keyword")
#     Keyword_Type = models.IntegerField(default=0, verbose_name="Keyword_Type")
#     Proc_Name = models.TextField(default="", verbose_name="Proc_Name")
#     Proc_UserName = models.TextField(default="", verbose_name="Proc_UserName")
#     Proc_ParentID = models.IntegerField(default=0, verbose_name="Proc_ParentID")
#     Proc_ParentName = models.TextField(default="", verbose_name="Proc_ParentName")
#     src_file_name = models.TextField(default="", verbose_name="src_file_name")
#     file_size = models.IntegerField(default=0, verbose_name="file_size")
#     file_md5 = models.TextField(default="", verbose_name="file_md5")
#     file_flag = models.IntegerField(default=0, verbose_name="1.敏感 2木马 3重复 4伪装")
#     file_content = models.TextField(default="", verbose_name="file_content")
#     file_Count = models.IntegerField(default=0, verbose_name="file_Count")
#     feature_content = models.TextField(default="", verbose_name="feature_content")
#     file_property = models.TextField(default="", verbose_name="file_property")
#     disc_type = models.IntegerField(default=0, verbose_name="disc_type")
#     identifier = models.TextField(default="", verbose_name="identifier")
#     dev_machinetime = models.TextField(default="", verbose_name="dev_machinetime")
#     file_remark = models.TextField(default="", verbose_name="file_remark")
#     block_info = models.TextField(default="", verbose_name="block_info")
#     rojanhorse_type = models.IntegerField(default=0, verbose_name="rojanhorse_type")
#     rojanhorse_behavior = models.TextField(default="", verbose_name="rojanhorse_behavior")
#     rojanhorse_outlink = models.TextField(default="", verbose_name="rojanhorse_outlink")
#     is_background = models.IntegerField(default=0, verbose_name="is_background")
#     score = models.IntegerField(default=0, verbose_name="score")
#     InsterTime = models.TextField(default=0, verbose_name="InsterTime")
#
#     def __str__(self):
#         return self.task_id
#
#
# class stFileDownload_Net(models.Model):
#     dev_ident = models.TextField(default="", verbose_name="dev_ident")
#     file_name = models.TextField(default="", verbose_name="file_name")
#     local_file_path = models.TextField(default="", verbose_name="local_file_path")
#     FileSize = models.IntegerField(default=0, verbose_name="FileSize")
#     CreateTime = models.TextField(default="", verbose_name="CreateTime")
#     key_word = models.TextField(default="", verbose_name="key_word")
#     sensitive_flag = models.TextField(default="", verbose_name="sensitive_flag")
#     file_from_net = models.TextField(default="", verbose_name="file_from_net")
#     file_md5 = models.TextField(default="", verbose_name="file_md5")
#     file_from_domain = models.TextField(default="", verbose_name="file_from_domain")
#     file_from_ip = models.TextField(default="", verbose_name="file_from_ip")
#     InsterTime = models.TextField(default="", verbose_name="InsterTime")
#
#     def __str__(self):
#         return self.file_name
#
#
# class RunInfo(models.Model):
#     RootKey = models.TextField(default="", verbose_name="RootKey")
#     KeyName = models.TextField(default="", verbose_name="KeyName")
#     KeyValue = models.TextField(default="", verbose_name="KeyValue")
#     FileName = models.TextField(default="", verbose_name="FileName")
#     FileCmd = models.TextField(default="", verbose_name="FileCmd")
#     FileCompanyName = models.TextField(default="", verbose_name="FileCompanyName")
#     IsSigner = models.IntegerField(default=0, verbose_name="IsSigner")
#     SignerName = models.TextField(default="", verbose_name="SignerName")
#     InsterTime = models.TextField(default="", verbose_name="InsterTime")
#
#     def __str__(self):
#         return self.KeyValue
#
#
# class sTaskList(models.Model):
#     Name = models.TextField(default="", verbose_name="Name")
#     Path = models.TextField(default="", verbose_name="Path")
#     Description = models.TextField(default="", verbose_name="Description")
#     Author = models.TextField(default="", verbose_name="Author")
#     Version = models.TextField(default="", verbose_name="Version")
#     ImagePath = models.TextField(default="", verbose_name="ImagePath")
#     Args = models.TextField(default="", verbose_name="Args")
#     LastRun = models.TextField(default="", verbose_name="LastRun")
#     Logon = models.TextField(default="", verbose_name="Logon")
#     Boot = models.TextField(default="", verbose_name="Boot")
#     Enabled = models.TextField(default="", verbose_name="Enabled")
#     Status = models.TextField(default="", verbose_name="Status")
#     InsterTime = models.TextField(default="", verbose_name="InsterTime")
#
#     def __str__(self):
#         return self.Name
#
#
# class IPvisit_Net(models.Model):
#     dev_ident = models.TextField(default="", verbose_name="dev_ident")
#     ip_address = models.TextField(default="", verbose_name="ip_address")
#     domain_name = models.TextField(default="", verbose_name="domain_name")
#     Proc_Name = models.TextField(default="", verbose_name="Proc_Name")
#     rPort = models.IntegerField(default=0, verbose_name="rPort")
#     file_md5 = models.TextField(default="", verbose_name="file_md5")
#     province_name = models.TextField(default="", verbose_name="province_name")
#     datail_address = models.TextField(default="", verbose_name="datail_address")
#     domestic_flag = models.IntegerField(default=0, verbose_name="domestic_flag")
#     longitude = models.TextField(default="", verbose_name="longitude")
#     latitude = models.TextField(default="", verbose_name="latitude")
#     InsterTime = models.TextField(default="", verbose_name="InsterTime")
#     IsLocal = models.BooleanField(default="", verbose_name="IsLocal")
#     Local_address = models.TextField(default="", verbose_name="Local_address")
#     lPort = models.IntegerField(default=0, verbose_name="lPort")
#     status = models.TextField(default="", verbose_name="status")
#
#     def __str__(self):
#         return self.dev_ident
#
#
# class Security_Center(models.Model):
#     Product = models.TextField(default="", verbose_name="Product")
#     Name = models.TextField(default="", verbose_name="Name")
#     sType = models.IntegerField(default=0, verbose_name="sType")
#     InsterTime = models.TextField(default="", verbose_name="InsterTime")
#
#     def __str__(self):
#         return self.Product
#
#
# class usb_conn(models.Model):
#     identifier = models.TextField(default="", verbose_name="identifier")
#     guid = models.TextField(default="", verbose_name="guid")
#     stor_ident = models.TextField(default="", verbose_name="stor_ident")
#     stor_name = models.TextField(default="", verbose_name="stor_name")
#     stor_sign = models.TextField(default="", verbose_name="stor_sign")
#     stor_model = models.TextField(default="", verbose_name="stor_model")
#     stor_factory = models.TextField(default="", verbose_name="stor_factory")
#     stor_vid = models.TextField(default="", verbose_name="stor_vid")
#     stor_pid = models.TextField(default="", verbose_name="stor_pid")
#     stor_size = models.IntegerField(default=0, verbose_name="stor_size")
#     dev_type = models.IntegerField(default=0, verbose_name="dev_type")
#     dev_machinetime = models.TextField(default="", verbose_name="dev_machinetime")
#     con_time = models.TextField(default="", verbose_name="con_time")
#     dis_time = models.TextField(default="", verbose_name="dis_time")
#     state = models.IntegerField(default=0, verbose_name="state")
#     InsterTime = models.TextField(default="", verbose_name="InsterTime")
#
#     def __str__(self):
#         return self.guid
#
#
# class ServiceList(models.Model):
#     PID = models.IntegerField(default=0, verbose_name="进程ID")
#     Name = models.TextField(default="", verbose_name="服务名")
#     ImageName = models.TextField(default="", verbose_name="ImageName")
#     CmdLine = models.TextField(default="", verbose_name="服务参数")
#     DisplayName = models.TextField(default="", verbose_name="DisplayName")
#     ObjectName = models.TextField(default="", verbose_name="服务用户组")
#     Status = models.TextField(default="", verbose_name="服务当前状态")
#     StartUp = models.TextField(default="", verbose_name="服务是手动还是自动启动")
#     Description = models.TextField(default="", verbose_name="服务描述")
#     FileVersion = models.TextField(default="", verbose_name="文件版本")
#     FileProductName = models.TextField(default="", verbose_name="文件厂家")
#     FileCompanyName = models.TextField(default="", verbose_name="文件公司")
#     FileDescription = models.TextField(default="", verbose_name="文件描述")
#     DllName = models.TextField(default="", verbose_name="DLL信息")
#     IsNow = models.IntegerField(default=0, verbose_name="IsNow")
#     InsterTime = models.TextField(default="", verbose_name="写入时间")
#
#     def __str__(self):
#         return self.PID
#
#
# class usb_exchange(models.Model):
#     identifier = models.TextField(default="", verbose_name="identifier")
#     stor_ident = models.TextField(default="", verbose_name="stor_ident")
#     stor_name = models.TextField(default="", verbose_name="stor_name")
#     stor_sign = models.TextField(default="", verbose_name="stor_sign")
#     stor_model = models.TextField(default="", verbose_name="stor_model")
#     stor_factory = models.TextField(default="", verbose_name="stor_factory")
#     stor_vid = models.TextField(default="", verbose_name="stor_vid")
#     stor_pid = models.TextField(default="", verbose_name="stor_pid")
#     ex_action = models.IntegerField(default=0, verbose_name="ex_action")
#     ex_time = models.TextField(default="", verbose_name="ex_time")
#     src_file_name = models.TextField(default="", verbose_name="src_file_name")
#     src_dir = models.TextField(default="", verbose_name="src_dir")
#     file_size = models.IntegerField(default=0, verbose_name="file_size")
#     up_dir = models.TextField(default="", verbose_name="up_dir")
#     file_md5 = models.TextField(default="", verbose_name="file_md5")
#     failed_des = models.TextField(default="", verbose_name="failed_des")
#     InsterTime = models.TextField(default="", verbose_name="InsterTime")
#
#     def __str__(self):
#         return self.identifier
#
#
# class NetApp(models.Model):
#     Name = models.TextField(default="", verbose_name="Name")
#     Path = models.TextField(default="", verbose_name="Path")
#     des = models.TextField(default="", verbose_name="des")
#
#     def __str__(self):
#         return self.Name
#
#
# class UsbHistory(models.Model):
#     Name = models.TextField(default="", verbose_name="Name")
#     SerialNumber = models.TextField(default="", verbose_name="SerialNumber")
#     Timestamp = models.TextField(default="", verbose_name="Timestamp")
#     DeviceClass = models.TextField(default="", verbose_name="DeviceClass")
#     InsterTime = models.TextField(default="", verbose_name="InsterTime")
#
#     def __str__(self):
#         return self.Name
#
#
# class InstallApp(models.Model):
#     Name = models.TextField(default="", verbose_name="Name")
#     Version = models.TextField(default="", verbose_name="Version")
#     Company = models.TextField(default="", verbose_name="Company")
#     InstallDate = models.TextField(default="", verbose_name="InstallDate")
#     Uninstall = models.TextField(default="", verbose_name="Uninstall")
#     HelpLink = models.TextField(default="", verbose_name="HelpLink")
#     AboutLink = models.TextField(default="", verbose_name="AboutLink")
#     InfoLink = models.TextField(default="", verbose_name="InfoLink")
#     UpdateLink = models.TextField(default="", verbose_name="UpdateLink")
#     InsterTime = models.TextField(default="", verbose_name="InsterTime")
#
#     def __str__(self):
#         return self.Name
