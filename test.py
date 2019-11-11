from datetime import datetime, timedelta
from ipaddress import ip_address
from pymongo import MongoClient


def get_short_date(days_interval=0, sdate=None):
    sdate = datetime.strptime(str(sdate), '%y%m%d') if sdate else datetime.today()
    return int((sdate + timedelta(days=days_interval)).strftime('%y%m%d'))


dcf_db = MongoClient("mongodb://172.30.96.230:27017", connect=False)['dcf']
adf_db = MongoClient("mongodb://172.30.96.230:27017", connect=False)['adf']
dlm_db = MongoClient("mongodb://172.30.96.230:27017", connect=False)['dlm']

ips = ["172.31.114.24", "172.31.114.27", "172.31.114.29", "172.31.114.7", "172.31.114.8", "172.31.114.12", "172.31.114.16", "172.31.114.6", "172.31.114.30", "172.31.114.32", "172.31.114.25", "172.31.114.9", "172.31.114.11", "172.31.114.15",  "172.31.114.19", "172.31.114.5", "172.31.114.33", "172.31.114.37", "172.31.114.34", "172.31.114.35", "172.31.114.23", "172.31.114.28", "172.31.114.13", "172.31.114.45", "172.31.114.39", "172.31.114.4", "172.31.114.31", "172.31.114.36", "172.31.64.12", "172.31.64.9", "172.31.64.7",  "172.31.64.8", "172.31.64.16", "172.31.64.18", "10.199.41.3", "172.31.64.23", "172.31.64.4", "172.31.64.6", "172.31.64.10", "172.31.64.14", "172.31.64.15", "172.31.64.19", "172.31.64.20", "172.31.64.21", "10.199.41.2", "172.31.64.22", "10.199.41.1", "172.31.64.5", "172.31.64.17", "172.31.64.11", "172.31.64.13", "10.41.80.10", "10.41.80.11", "10.41.80.12", "10.41.80.14", "10.41.80.16", "10.41.80.21", "10.41.80.13", "10.41.80.19", "10.41.80.23", "10.41.80.17", "10.41.80.26", "10.41.80.25", "10.41.80.22", "10.41.80.28", "10.41.80.20", "10.41.80.18", "10.41.80.31", "10.4.255.10", "10.41.80.15", "10.41.80.29", "10.41.80.30", "10.41.80.32", "10.41.80.35", "10.41.80.33", "10.41.80.34", "10.41.80.36", "172.31.131.132", "172.31.131.134", "172.31.131.135", "172.31.131.136", "172.31.131.140", "172.31.131.138", "172.31.131.141", "172.31.84.144", "172.31.84.137", "172.31.84.145", "172.31.84.136", "172.31.84.132", "172.31.84.133", "172.31.84.134", "172.31.84.147", "172.31.84.148", "172.31.84.152", "172.31.84.135", "172.31.84.138", "172.31.84.139", "172.31.84.143", "172.31.84.142", "172.31.84.149", "172.31.84.150", "172.31.84.151", "172.31.84.153", "172.31.84.154", "172.31.84.140", "10.6.255.10", "172.31.84.155", "172.31.84.156", "10.61.0.10", "172.31.18.12", "172.31.18.10", "172.31.18.7", "172.31.18.9", "172.31.18.15", "172.31.18.16", "172.31.18.18", "172.31.18.19", "172.31.18.21", "172.31.18.22", "172.31.18.11", "172.31.18.28", "172.31.18.5", "172.31.18.6", "172.31.18.13", "172.31.18.17", "172.31.18.23", "172.31.18.24", "172.31.18.25", "172.31.18.26", "172.31.18.8", "10.7.255.74",  "10.7.255.74", "172.31.18.14", "172.31.18.20", "172.31.48.7", "172.31.48.12", "172.31.48.13", "172.31.48.5", "172.31.48.6", "172.31.48.47", "172.31.48.49", "172.31.48.32", "172.31.48.22", "172.31.48.24", "172.31.48.27", "172.31.48.8", "172.31.48.50", "172.31.48.51", "172.31.48.4", "172.31.48.48", "172.31.48.31", "172.31.48.33", "172.31.48.23", "10.81.0.6", "10.8.255.2", "172.31.34.4", "172.31.34.5", "172.31.34.6", "172.31.34.29", "172.31.34.30", "172.31.34.31", "172.31.34.42", "172.31.34.35", "172.31.34.36", "172.31.34.37", "172.31.34.8", "172.31.34.51", "172.31.34.9", "172.31.34.49", "172.31.34.7", "172.31.34.50", "10.21.176.11", "10.21.176.13", "10.21.176.20", "10.21.176.22", "172.31.34.47", "172.31.34.48", "172.31.34.53", "10.21.176.12", "10.21.176.16", "10.21.176.17", "10.21.176.18", "10.21.176.19", "10.21.176.10", "10.21.176.23", "172.31.34.45", "10.21.176.14", "172.31.161.132"]

dcf_failed_singular_ips = []
adf_failed_singular_ips = []
dlm_failed_singular_ips = []
dcf_failed_bucket_ips = []
adf_failed_bucket_ips = []
dlm_failed_bucket_ips = []

for ip in ips:
    collection = "ne" + str(int(ip_address(ip)))

    dcf_res = dcf_db[collection].find_one({"ptype": "s/i", "sdate": get_short_date(-1)})
    if not dcf_res:
        dcf_failed_singular_ips += [ip]
    else:
        print(ip + ": DCF-DB Singular OK!")

        adf_res = adf_db[collection].find_one({"ptype": "s/i", "sdate": get_short_date(-1)})
        if not adf_res:
            adf_failed_singular_ips += [ip]
        else:
            print(ip + ": ADF-DB Singular OK!")

            dlm_res = dlm_db[collection].find_one({"ptype": "s/i", "sdate": get_short_date(-1)})
            if not dlm_res:
                dlm_failed_singular_ips += [ip]
            else:
                print(ip + ": DLM-DB Singular OK!")

    dcf_res = dcf_db[collection].find_one({"ptype": "b/i", "sdate": get_short_date(-1)})
    if not dcf_res:
        dcf_failed_bucket_ips += [ip]
    else:
        print(ip + ": DCF-DB Bucket OK!")

        adf_res = adf_db[collection].find_one({"ptype": "b/i", "sdate": get_short_date(-1)})
        if not adf_res:
            adf_failed_bucket_ips += [ip]
        else:
            print(ip + ": ADF-DB Bucket OK!")

            dlm_res = dlm_db[collection].find_one({"ptype": "b/i", "sdate": get_short_date(-1)})
            if not dlm_res:
                dlm_failed_bucket_ips += [ip]
            else:
                print(ip + ": DLM-DB Bucket OK!")

if dcf_failed_singular_ips:
    print("\nDCF-DB Failed Singular IPs:\n")
    print(dcf_failed_singular_ips)

if adf_failed_singular_ips:
    print("\nADF-DB Failed Singular IPs:\n")
    print(adf_failed_singular_ips)

if dlm_failed_singular_ips:
    print("\nDLM-DB Failed Singular IPs:\n")
    print(dlm_failed_singular_ips)

if dcf_failed_bucket_ips:
    print("\nDCF-DB Failed Bucket IPs:\n")
    print(dcf_failed_bucket_ips)

if adf_failed_bucket_ips:
    print("\nADF-DB Failed Bucket IPs:\n")
    print(adf_failed_bucket_ips)

if dlm_failed_bucket_ips:
    print("\nDLM-DB Failed Bucket IPs:\n")
    print(dlm_failed_bucket_ips)
