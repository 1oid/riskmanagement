import sqlite3
import sys
import os
# 环境变量配置
#
path = "/Users/loid/PycharmProjects/manage"
sys.path.append(path)

from manage.wsgi import *
from stu.models import *
from manage.settings import DATASOURCE, DATASOURCE_FILEINFO_DAT3


def importDb(keyarray, _table, objects, db_file):
    db = sqlite3.connect(db_file)
    cursor = db.cursor()
    count = 0

    query = cursor.execute("select * from {}".format(_table))
    for row in query:
        if objects.objects.filter(**dict(zip(keyarray, row[1:]))).count() > 0:
            continue

        try:
            objects.objects.create(**dict(zip(keyarray, row[1:])))
        except Exception as e:
            print("[ERROR] {}".format(e))
            continue

        count += 1
    print("\t{} 增加{}条数据".format(_table, count))
    cursor.close()
    db.close()


def run(db_file):
    importDb([
        "AName", "AVer", "ACompany", "AInTime", "AUninstall",
        "AALink", "AILink", "AULink", "Other"
    ], "UserApplication", UserApplication, db_file)

    importDb([
        "DName", "SNumber", "UseTime", "DType", "Other"
    ], "UserDevHistory", UserDevHistory, db_file)
    
    importDb([
        "Did", "VName", "DName", "DModel", "SNumber",
        "Action", "ATime", "FileName", "FileSize",
        "FIleMD5", "FileAttribute", "FileDesc", "Other"
    ], "UserFileCopy", UserFileCopy, db_file)
    
    importDb([
        "AccTime", "FileName", "FilePath", "FileType", "Other"
    ], "UserRecords", UserRecords, db_file)
    
    importDb([
        "Did", "Domain", "Ip", "PName", "FileName",
        "FileSize", "FileMd5", "FCTime", "KeyDesc",
        "sTag", "Other"
    ], "UserBroFile", UserBroFile, db_file)
    
    importDb([
        "DId", "DMac", "DIp", "DName", "UName", "DSystem",
        "Remarks", "Other"
    ], "UserDevice", UserDevice, db_file)

    importDb([
        "Did", "Domain", "IP", "Port", "PName",
        "FileMd5", "IpName", "IsHost", "IpAddress",
        "Action", "xAddress", "yAddress", "Other"
    ], "UserNetWork", UserNetWork, db_file)
    
    importDb([
        "PID", "SName", "IName", "SCommand", "DName",
        "OName", "Status", "StartUp", "SDesc", "FVer",
        "FPName", "FCName", "FDesc", "DllName", "IsRun",
        "Other"
    ], "UserServices", UserServices, db_file)

    importDb([
        "Did", "VName", "DName", "DModel", "SNumber",
        "DSize", "DAction", "Ctime", "Dtime", "DType",
        "DStatus", "Other"
    ], "UserDevAccess", UserDevAccess, db_file)

    importDb([
        "Did", "FileType", "KeyDesc", "ContentRemark",
        "FileName", "FileSize", "FileTag", "IsDup", "FileMd5",
        "FileAttribute", "FileNumber", "FileDesc", "PName",
        "PUName", "PPID", "PPName", "Other"
    ], "UserFile", UserFile, db_file)
    
    importDb([
        "Did", "PID", "PName", "PCmd", "PSession",
        "PUser", "PMem", "PIO", "PVer", "PStart",
        "Verified", "IsVerified", "Other"
    ], "UserProcess", UserProcess, db_file)

    importDb([
        "KRoot", "KName", "KValue", "FName", "FCommand",
        "FCName", "Verified", "IsVerified", "Other"
    ], "UserStartup", UserStartup, db_file)

    """
    智慧分析数据合成部分
    文件下载    UserBroFile
    文件拷贝    UserFileCopy
    文件打印    UserFile - FileTag == 4
    网络信息表  UserNetWork
    
    通过文件风控表中的数据的MD5和文件名，找到对应文件属性
    """
    objects = UserFile.objects.all()
    querysets = []
    querysets_save = []

    def is_duplicate(_did, _filename, _md5, _action):
        """
        以后优化
        :param _did:
        :param _filename:
        :param _md5:
        :param _action:
        :return:
        """
        return IntelliAnalysis.objects.filter(
            did=_did, filename=_filename, md5=_md5, action=_action
        ).count() > 0

    for item in objects:
        _md5 = item.FileMd5
        _filename = item.FileName
        _did = item.Did
        _size = item.FileSize

        # 打印保存
        if item.FileTag == 4:
            querysets.append(IntelliAnalysis(
                did=item.Did,
                filename=_filename,
                filepath=_filename,
                filesize=item.FileSize,
                md5=item.FileMd5,
                description=item.KeyDesc,
                duplicate=False if _md5 not in querysets_save else True,
                action=1,
                Other=item.Other
            ))
    
        # 下载
        objects_download = UserBroFile.objects.filter(
            FileName=_filename, FileMd5=_md5
        )
    
        for dowload_item in objects_download:
            if is_duplicate(_did=_did, _filename=_filename, _md5=_md5, _action=0):
                continue
    
            querysets.append(IntelliAnalysis(
                did=dowload_item.Did,
                filename=_filename,
                filepath=_filename,
                filesize=dowload_item.FileSize,
                md5=dowload_item.FileMd5,
                description=item.KeyDesc,
                duplicate=False if _md5 not in querysets_save else True,
                action=0,
                Other=dowload_item.Other
            ))

        # 拷贝
        objects_copy = UserFileCopy.objects.filter(
            Did=_did, FileName=_filename, FIleMD5=_md5
        )
    
        for copy_item in objects_copy:
            if is_duplicate(_did=_did, _filename=_filename, _md5=_md5, _action=2):
                continue
    
            querysets.append(IntelliAnalysis(
                did=copy_item.Did,
                filename=_filename,
                filepath=_filename,
                filesize=copy_item.FileSize,
                md5=copy_item.FIleMD5,
                description=item.KeyDesc,
                duplicate=False if _md5 not in querysets_save else True,
                action=2,
                Other=copy_item.Other
            ))
    
        # 外发
        objects_net = UserNetWork.objects.filter(
            Did=_did, FileMd5=_md5
        )
    
        for net_item in objects_net:
            if is_duplicate(_did=_did, _filename=_filename, _md5=_md5, _action=3):
                continue
    
            querysets.append(IntelliAnalysis(
                did=net_item.Did,
                filename=_filename,
                filepath=_filename,
                filesize=_size,
                md5=net_item.FileMd5,
                description=item.KeyDesc,
                duplicate=False if _md5 not in querysets_save else True,
                action=3,
                Other=net_item.Other
            ))
    
    IntelliAnalysis.objects.bulk_create(querysets)


def cache_read(db_file):
    importDb([
        "identifier", "CacheName", "FileName",
        "JpgFileName", "ZipName", "FileEx", "SaveName",
        "MD5", "FileSize", "ZipFileSize", "JpgFileSize",
        "UpSize", "IsOK", "IsZip", "IsImge", "InsterTime"
    ], "CacheFile", CacheFile, db_file)


def dir_scans(path):
    files = os.listdir(path)

    for _file in files:
        ext = _file.strip().split(".")[-1]
        _fullpath = path + "/" + _file

        if ext == "dat3" and "DataInfo" in _file:
            print("READ {}".format(_fullpath))
            run(_fullpath)
            print("DELETE {}".format(_fullpath))
            os.remove(_fullpath)
        elif ext == "txt":
            print("READ {}".format(_fullpath))
            read_txt(_fullpath)
            print("DELETE {}".format(_fullpath))
            os.remove(_fullpath)
            # os.remove(path + "/" + _file)

    print("READ {}".format(DATASOURCE_FILEINFO_DAT3))
    cache_read(DATASOURCE_FILEINFO_DAT3)
    print("DELETE {}".format(DATASOURCE_FILEINFO_DAT3))


def read_txt(txt):
    with open(txt, encoding="utf-8") as f:
        read = f.read().strip()

        DName, DMac, Dsystem, _1, DIP, _2, _3 = read.split("|")
        if UserDevice.objects.filter(
            DName=DName, DMac=DMac, DSystem=Dsystem,
            Remarks="|".join([_1, _2, _3]), DIp=DIP
        ).count() > 0:
            return


dir_scans(DATASOURCE)
# from manage.wsgi import *



