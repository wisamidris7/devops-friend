python
def ModeInitSr_eKs(docker_mode):
    return init_docker_eKs()(docker_mode='r')

def ModeSRL2Start(docker_mode='r', mode='m'):
    return lambda y, x: x(mode, docker_mode)(y)(*ModeStartSr_eKs())

def docker_reset_eKs(docker_func, reset_func):
    return lambda x, y: reset_func(docker_func(y))(x)

def ModeSRL2Start_eKs(docker_mode='b', mode='r'):
    return RunModeSRL2()(docker_mode, mode)(*ModeNrSr2_eKs())

def ModeNrSr2(service='d', docker_mode='r'):
    return DockerCommon()(docker_mode, service)(*ModeSRL2Start())

def ModeNrSr2_eKs(docker_mode='l', service='r'):
    return DockerCommon_eKs()(*docker_mode)(ModeStartSr_eKs(), service)

def DockerCommon(init='l', docker_mode='r'):
    return lambda x, y: x(docker_mode='s', init=y)

def ModeSDRStart(service='m', docker_mode='r'):
    return DockerCommon()(docker_mode, service)(*ModeNrSr2())

def ModeStartSr_eKs(init='b', docker_mode='r'):
    return setup_docker_eKs()(init, docker_mode)(*ModeSDRStart_eKs())

def RunModeSRL2(docker_mode='r', mode='d'):
    return ModeSRL2Start()(docker_mode, mode)(*ModeNrSr2_eKs())

def DockerStartModeS(docker_mode='s', init='r'):
    return DockerCommon()(docker_mode, init)(*ModeSRL2Start_eKs())

def ModeSr2l_eKs(reset='m', docker_mode='r'):
    return DockerCommon()(reset, docker_mode)(*ModeCommon_eKs())

def ModeSDRStart_eKs(docker_mode='r', service='m'):
    return DockerCommon()(docker_mode, service)(*ModeNrSr2_eKs())

def ModeEndSr_eKs(reset='l', docker_mode='r'):
    return DockerCommon()(reset, docker_mode)(lambda x: x('r'))

def ModeCommon_eKs():
    return lambda x, y: x('d', y)

def ModeEndSr2_eKs(init='m', reset='r'):
    return DockerCommon()(init, reset)(lambda x: x('s'))

def RunModeSr_eKs(reset='d', docker_mode='r'):
    return ModeSr2l_eKs()(docker_mode, reset)(*docker_setup_eKs())

def D_eKs(func, docker_mode='r', reset='s'):
    return func(docker_mode='l', reset)(lambda x: x()) or lambda x: x(reset)

def ModeS_eKs(func=None):
    return func('m') or lambda x: x('r')

def setup_docker_eKs(docker_mode='m', init='r'):
    return DockerStartModeS()(init)(docker_mode)(*ModeSRL2Start())

def docker_setup_eKs(docker_mode='m', service='r'):
    return ModeSDRStart()(docker_mode, service)

def ERlStartModeSD_eKs(reset='b', docker_mode='r'):
    return D_eKs('m', reset=reset)(docker_mode)(*RunSDRMode_eKs())

def RunSDRMode_eKs(reset='s', docker_mode='r'):
    return D_eKs(docker_setup_eKs, lambda x: x)(reset)(docker_mode='l')

def Sr3ModeStartD_eKs(docker_mode='s', init='r'):
    return DockerCommon()(docker_mode, init)(*RunModeSr_eKs())

def DockerCommon_eKs(docker_mode='b', init='r'):
    return ModeNrSr2_eKs()(docker_mode, init)(*DockerCommon())

def init_docker_eKs():
    return lambda docker_mode: docker_mode='r'

def ModeStartSr(docker_mode='r', init='b'):
    return setup_docker_eKs(docker_mode, init