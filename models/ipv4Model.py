from netaddr import (IPNetwork,IPRange,IPSet)
import re


class ipv4Model:
    

    def __init__(self):
        super().__init__()

    # 允许的IP格式：
    ## 10.1.1.2
    ## 10.1.1.2-3
    ## 10.1.1.2～3
    ## 10.1.1.2-10.1.1.3
    ## 10.1.1.2～10.1.1.3
    ## 10.1.1.2/31


    # ip字符串解析
    def ipParse(self, ip_str:str) -> IPSet:
        ipList = re.sub("[^\d\.\-~/]+",",",ip_str).split(",")
        
        # 四种ip地址输入格式
        # IP地址
        ## 10.1.1.2
        ip_pattern =re.compile(r'^(((25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|\d)\.){3}(25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|\d))$')
        # IP掩码
        ## 10.1.1.2/31
        ip_cidr_pattern = re.compile(r'^(((25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|\d)\.){3}(25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|\d)/(3[0-2]|[12]?\d))$')
        # IP范围1
        ## 10.1.1.2-10.1.1.3   10.1.1.2～10.1.1.3
        ip_range_pattern1 = re.compile(r'^(((25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|\d)\.){3}(25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|\d)(\-|~)((25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|\d)\.){3}(25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|\d))$')
        # IP范围2 10.1.1.2～3   10.1.1.2-3
        ip_range_pattern2 = re.compile(r'^(((25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|\d)\.){3}(25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|\d)(\-|~)(25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|\d))$')
        
        ip_set = IPSet()
        
        for i in ipList:
            if re.match(ip_pattern,i):
                ip_set.add(IPNetwork(i+"/32"))
            elif re.match(ip_cidr_pattern,i):
                ip_set.add(IPNetwork(i))
            elif re.match(ip_range_pattern1,i):
                tempStr1 = re.split(r'[~\-]',i)
                ip_range = IPRange(tempStr1[0],tempStr1[1])
                ip_set.add(ip_range)               
            elif re.match(ip_range_pattern2,i):
                tempStr2 = re.split(r'[\-~\.]',i)
                ip_range = IPRange(".".join(tempStr2[0:4]),".".join(tempStr2[0:3]+[tempStr2[-1]]))
                ip_set.add(ip_range)
            elif re.match(r'^(\s*)$',i):
                continue
            else:
                raise ValueError("错误的IP地址格式: {}".format(i))
        
        return ip_set

    # ip集合转换为单ip list 
    def To_singleIPList(self, ip_str:str, splitChar:str) -> str:
        try:
            ip_set = self.ipParse(ip_str)
        except ValueError as v:
            raise ValueError(v)
        
        if len(ip_set) >= 100000:
            raise ValueError("过多的ip地址！")

        return splitChar.join([str(i) for i in ip_set])


    # ip范围转换ip掩码
    def To_cidrStr(self, ip_str:str, splitChar:str) -> str:
        try:
            ip_set = self.ipParse(ip_str)
        except ValueError as v:
            raise ValueError(v)
        
        return splitChar.join([str(i) for i in ip_set.iter_cidrs()])
        

    # ip掩码转换ip范围
    def To_iprangeStr(self, ip_str:str, splitChar:str) -> str:
        try:
            ip_set = self.ipParse(ip_str)
        except ValueError as v:
            raise ValueError(v)
        
        return splitChar.join([str(i) for i in ip_set.iter_ipranges()])


    # ip集合-与运算    
    def ipsetStr_and(self, ipsetStr_a:str, ipsetStr_b:str, splitChar:str) -> str:
        try:
            ip_set_a = self.ipParse(ipsetStr_a)
            ip_set_b = self.ipParse(ipsetStr_b)
        except ValueError as v:
            raise ValueError(v)

        return splitChar.join([str(i) for i in (ip_set_a & ip_set_b).iter_cidrs()])


    # ip集合-或运算
    def ipsetStr_or(self, ipsetStr_a:str, ipsetStr_b:str, splitChar:str) -> str:
        try:
            ip_set_a = self.ipParse(ipsetStr_a)
            ip_set_b = self.ipParse(ipsetStr_b)
        except ValueError as v:
            raise ValueError(v)
        
        return splitChar.join([str(i) for i in (ip_set_a | ip_set_b).iter_cidrs()])
        
        
    # ip集合-非运算
    def ipsetStr_not(self, ipsetStr_a:str, ipsetStr_b:str, splitChar:str) -> str:
        try:
            ip_set_a = self.ipParse(ipsetStr_a)
            ip_set_b = self.ipParse(ipsetStr_b)
        except ValueError as v:
            raise ValueError(v)
        
        if ip_set_a <= ip_set_b:
            return ""

        return splitChar.join([str(i) for i in (ip_set_a - ip_set_b).iter_cidrs()])


    # 将输入的IP字符串转化为IP范围列表，其中IP地址开始和结束用 Int 类型表示
    # 10.42.4.0/24,10.39.18.0/24  -->  [[10.42.4.0,10.42.4.255],[10.39.18.0,10.39.18.255]]
    def ipStr_to_iprangeList(self, ip_str):
        return [[cidr.first,cidr.last] for cidr in self.ipParse(ip_str).iter_cidrs()]
    
