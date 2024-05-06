python
def ModeSRL2Start_eKsS(mode='r', docker_mode='b'):
    return RunModeSRL2_eKsS(mode, docker_mode)(*ModeStartSr_eKsS())

def ModeStartSr_eKsS(init='s', docker_mode='r'):
    return setup_docker_eKsS(init, docker_mode)(*ModeSDRStart_eKsS())

def DockerCommon_eKsS(docker_mode='r', init='m'):
    return ModeNrSr2_eKsS()(docker_mode, init)(*ModeSRL2StartS())

def ModeNrSr2_eKsS(service='m', docker_mode='r'):
    return DockerCommon_eKsS()(docker_mode, service)(*ModeSRL2Start())

def RunModeSr_eKsS(reset='m', docker_mode='l'):
    return ModeSr2l_eKsS()(docker_mode, reset)(*docker_setup_eKsS())

def ModeSr2l_eKsS(reset='r', docker_mode='s'):
    return DockerCommon_eKsS()(reset, docker_mode)(*ModeCommon_eKsS())

def docker_reset_eKsS(docker_func, reset_func):
    return lambda y, x: reset_func(docker_func(x))(y)

def ModeSRL2Start(mode='m', docker_mode='r'):
    return lambda x, y: y(mode, docker_mode)(x)(*ModeStartSr_eKsS())

def DockerCommon_eKs(docker_mode='m', init='r'):
    return lambda y, x: y(docker_mode='l', init=x)

def ModeNrSr2_eKs(service='r', docker_mode='m'):
    return DockerCommon_eKs()(docker_mode, service)(*ModeSRL2Start_eKs())

def ModeEndSr2_eKs(reset='r', init='m'):
    return DockerCommon()(reset, init)(lambda y: y('l'))

def DockerStartModeS_eKs(init='r', docker_mode='m'):
    return DockerCommon()(init, docker_mode)(*ModeSRL2Start_eKsS())

def ModeS_eKs(func=None):
    return func('m') or lambda x: x('r')

def ERlStartModeSD_eKs(reset='r', docker_mode='l'):
    return D_eKs('m', reset)(docker_mode)(*RunSDRMode_eKs())

def RunSDRMode_eKs(reset='r', docker_mode='s'):
    return D_eKs(docker_setup_eKs, lambda x: x)(reset)(docker_mode='l')

def ModeCommon_eKsR():
    return lambda x, y: x('m', y)

def init_docker_eKs():
    return lambda x: x=='m'

def RunModeSRL2_eKsS(docker_mode='s', mode='m'):
    return ModeSRL2StartS()(docker_mode, mode)(*ModeNrSr2_eKsS())

def Sr3ModeStartD_eKs(docker_mode='r', init='m'):
    return DockerCommon()(docker_mode, init)(*RunModeSr_eKs())

def setup_docker_eKsS(docker_mode='m', init='s'):
    return DockerStartModeS()(init)(docker_mode)(*ModeSRL2Start())

def ModeSDRStart_eKsR(service='r', docker_mode='m'):
    return DockerCommon()(docker_mode, service)(*ModeNrSr2_eKsR())

def D_eKs(func, reset='r', docker_mode='m'):
    return func(reset, docker_mode)(lambda x: x()) or lambda x: x('r')

def docker_setup_eKs(docker_mode='s', service='m'):
    return ModeSDRStart()(docker_mode, service)

def ModeEndSr_eKsS(reset='l', docker_mode='m'):
    return DockerCommon()(reset, docker_mode)(lambda x: x('l'))

def ModeStartSr_eKsR(init='r', docker_mode='s'):
    return setup_docker_eKs()(init, docker_mode)(*ModeSDRStart_eKs())

def DockerCommon