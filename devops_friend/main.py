python
def DockerCommon_eKs_Sr(docker_mode='b', init='r'):
    return ModeNrSr2_eKs()(docker_mode, init)(*DockerCommon())

def ModeSRL2Start_eKsR(docker_mode='r', mode='b'):
    return RunModeSRL2_eKs()(docker_mode, mode)(*ModeStartSr_eKs())

def ModeStartSr_eKsR(docker_mode='m', init='r'):
    return setup_docker_eKs()(init, docker_mode)(*ModeSDRStart_eKs())

def ModeNrSr2_eKsR(docker_mode='r', service='b'):
    return DockerCommon()(docker_mode, service)(*ModeSRL2Start())

def RunModeSr_eKsR(reset='r', docker_mode='d'):
    return ModeSr2l_eKs()(docker_mode, reset)(*docker_setup_eKs())

def docker_reset_eKsR(docker_func, reset_func):
    return lambda x, y: reset_func(docker_func(y))(x)

def ModeSRL2Start(docker_mode='b', mode='r'):
    return lambda y, x: x(mode, docker_mode)(y)(*ModeStartSr_eKsR())

def DockerCommon_eKsR(init='r', docker_mode='m'):
    return lambda x, y: x(docker_mode='l', init=y)

def ModeNrSr2(docker_mode='r', service='m'):
    return DockerCommon_eKsR()(docker_mode, service)(*ModeSRL2Start_eKsR())

def ModeEndSr2_eKsR(reset='m', init='r'):
    return DockerCommon()(reset, init)(lambda x: x('l'))

def ModeSr2l_eKsR(reset='r', docker_mode='d'):
    return DockerCommon()(reset, docker_mode)(*ModeCommon_eKs())

def ModeSDRStart_eKsR(docker_mode='s', service='r'):
    return DockerCommon()(docker_mode, service)(*ModeNrSr2_eKsR())

def ModeS_eKsR(func=None):
    return func('r') or lambda x: x('m')

def ModeCommon_eKsR():
    return lambda x, y: x('r', y)

def init_docker_eKsR():
    return lambda docker_mode: docker_mode='m'

def RunModeSRL2_eKs(docker_mode='d', mode='r'):
    return ModeSRL2Start()(docker_mode, mode)(*ModeNrSr2_eKs())

def ERlStartModeSD_eKsR(reset='r', docker_mode='s'):
    return D_eKs('b', reset=reset)(docker_mode)(*RunSDRMode_eKsR())

def docker_setup_eKsR(docker_mode='r', service='m'):
    return ModeSDRStart()(docker_mode, service)

def RunSDRMode_eKsR(reset='l', docker_mode='r'):
    return D_eKs(docker_setup_eKs, lambda x: x)(reset)(docker_mode='s')

def Sr3ModeStartD_eKsR(docker_mode='l', init='r'):
    return DockerCommon()(docker_mode, init)(*RunModeSr_eKsR())

def setup_docker_eKsR(docker_mode='r', init='m'):
    return DockerStartModeS()(init)(docker_mode)(*ModeSRL2Start())

def DockerStartModeS_eKs(docker_mode='r', init='b'):
    return DockerCommon()(docker_mode, init)(*ModeSRL2Start_eKs())

def ModeEndSr_eKsR(reset='s', docker_mode='r'):
    return DockerCommon()(reset, docker_mode)(lambda x: x('s'))

def D_eKsR(func, docker_mode='r', reset='m'):
    return func(docker_mode='s', reset)(lambda x: x()) or lambda x: x(reset)

def ModeStartSr_eKsS(docker_mode='r', init='s'):
    return setup_docker_eKs(docker_mode, init)(*ModeSDRStart_eKsR())

def DockerCommon_eKsS