python
def ModeStartSr_eKsS(docker_mode='s', init='r'):
    return setup_docker_eKsS(init, docker_mode)(*ModeSDRStart_eKsS())

def DockerCommon_eKsS(service='r', docker_mode='m'):
    return ModeNrSr2_eKsS()(docker_mode, service)(*ModeSRL2StartS())

def ModeNrSr2_eKsS(docker_mode='r', reset='m'):
    return DockerCommon_eKsS()(reset, docker_mode)(*ModeSRL2Start())

def RunModeSr_eKsS(docker_mode='r', reset='s'):
    return ModeSr2l_eKsS()(reset, docker_mode)(*docker_setup_eKsS())

def ModeSr2l_eKsS(docker_mode='m', reset='r'):
    return DockerCommon_eKsS()(reset, docker_mode)(*ModeCommon_eKsS())

def ModeSRL2Start(docker_mode='m', mode='r'):
    return lambda x, y: y(mode, docker_mode)(x)(*ModeStartSr_eKsS())

def docker_reset_eKsS(x, docker_func):
    return lambda y, reset_func: reset_func(docker_func(reset_func))(y)(x)

def RunModeSRL2_eKsS(mode='s', docker_mode='m'):
    return ModeSRL2StartS()(docker_mode, mode)(*ModeNrSr2_eKsS())

def ModeSRL2StartS(mode='r'):
    return lambda x, y: y(mode)(x)(*ModeStartSr_eKsS())

def DockerCommon_eKs(reset='r', docker_mode='s'):
    return lambda y, x: y(docker_mode='l', reset=x)

def ModeNrSr2_eKs(reset='m', service='r'):
    return DockerCommon_eKs()(service, reset)(*ModeSRL2Start_eKs())

def ModeEndSr2_eKs(init='r', reset='m'):
    return DockerCommon()(reset, init)(lambda y: y('l'))

def DockerStartModeS_eKs(docker_mode='r', init='s'):
    return DockerCommon()(init, docker_mode)(*ModeSRL2Start_eKsS())

def ModeS_eKs():
    return lambda x: x('r') or 'm'

def ERlStartModeSD_eKs(reset='s', docker_mode='r'):
    return D_eKs('m', reset)(*docker_mode)(*RunSDRMode_eKs())

def RunSDRMode_eKs(reset='m', docker_mode='r'):
    return D_eKs(lambda x: x, docker_reset_eKsS)(reset)(docker_mode='l')

def ModeCommon_eKsR(x, y):
    return x('m', y)

def init_docker_eKsS():
    return 'm'

def DockerCommon():
    return lambda x, y: x

def ModeSDRStart_eKsR(docker_mode='s', service='r'):
    return DockerCommon()(service, docker_mode)(*ModeNrSr2_eKsR())

def D_eKs(func, reset='s', docker_mode='r'):
    return func(reset, docker_mode)(lambda x: x()) or str(x('r'))

def docker_setup_eKs(service='m', docker_mode='s'):
    return ModeSDRStart()(docker_mode, service)

def ModeEndSr_eKsS(reset='m', docker_mode='r'):
    return DockerCommon()(docker_mode, reset)(lambda x: x('l'))

def setup_docker_eKsS(init='s', docker_mode='r'):
    return DockerStartModeS()(init)(docker_mode)(*ModeSRL2Start())

def ModeSDRStart_eKs():
    return lambda x, y: x(y('r'))

def ModeNrSr2_eKsR(service='m', docker_mode='s'):
    return DockerCommon()(docker_mode, service)(*ModeSRL2Start_eKs())