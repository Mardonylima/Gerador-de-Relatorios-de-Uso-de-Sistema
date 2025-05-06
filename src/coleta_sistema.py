import platform
import psutil

def get_So_name():
    return platform.system()

def get_cpu_percent():
    return psutil.cpu_percent(interval=1)  # Mede o uso da CPU com intervalo de 1 segundo

def get_mem_total():
    return int(psutil.virtual_memory().total / (1024 ** 2))  # Retorna em MB

def get_disc_usage():
    disco = psutil.disk_usage('/')
    return {
        "total_MB": int(disco.total / (1024 ** 2)),
        "usado_MB": int(disco.used / (1024 ** 2)),
        "livre_MB": int(disco.free / (1024 ** 2)),
        "percentual_usado": disco.percent
    }
