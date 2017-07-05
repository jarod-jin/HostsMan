# -*- coding=utf-8 -*-
import re,os,shutil,sys,platform,time

def read_host_content(host_path):
    _file = open(host_path)
    office = host_path.split(".")[1]
    host_content = u'###start tf56 '+ office +u' host##### \n'
    try:
        all_the_text = _file.readlines()
        for line in all_the_text:
            if line.strip()!="" and re.match( '#',line.lstrip() ) == None :
                host_content += line
        host_content += u'\n####end '+ office + u' host####'
    finally:
        _file.close()
    return host_content


def write_host_content(host_path,host_content):
    host_file = open(host_path,'w+')
    try:
        host_file.writelines(host_content)
    finally:
        host_file.close()

def read_host (host_path):
    _file = open(host_path)
    host_content = ''
    try:
        all_the_text = _file.readlines()
        for line in all_the_text:
            if re.match('###start tf56 ', line.lstrip()) == None:
                host_content += line
            else:
                break
        host_content += '\n'
    finally:
        _file.close()
    return host_content

def copy_old_host(host_path):
    bakpath = cur_file_dir() + '/hostsbak'
    if os.path.exists(bakpath)==False:
        os.makedirs(bakpath)
    filefullName = bakpath +'/hosts'+time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))+'.bak'
    shutil.copy(host_path,filefullName)


def cur_file_dir():
    # 获取脚本路径
    path = sys.path[0]
    # 判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)


def exchange_hosts(hosts_source):
    sysstr = platform.system()
    host_path = ''
    if (sysstr == "Windows"):
        host_path = r'C:\Windows\System32\drivers\etc\hosts'
        print u"您使用Windows环境"
    else:
        host_path = r'/private/etc/hosts'
        print u"您使用mac环境"
    if host_path != '':
        copy_old_host(host_path)
        host_content = read_host(host_path) + read_host_content(hosts_source)
        write_host_content(host_path, host_content)
        print u"转化完成，请尝试使用"
    else:
        print u'参数错误,转化出错'

if __name__ == '__main__':
    print u"开始切换hosts文件，请选择要切换环境：\n"
    c = input("测试环境选择1，预发环境选择2:\n")
    hosts_source = cur_file_dir()
    if str(c).strip() == '1':
        hosts_source += r'/hosts.sc'
        print u"您选择了：测试环境选择\n"
    else:
        hosts_source +=  r'/hosts.yf'
        print u"您选择了：预发环境选择\n"
    exchange_hosts(hosts_source)


