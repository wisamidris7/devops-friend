python
def ModeNrSr2_eKs(reset='m', service='r'):
    return DockerCommon_eKs()(service, reset)(*ModeSRL2Start_eKs())

def ModeSRL2Start_eKs():
    return lambda x, y: y(x('r'))

def ModeSRL2Start_eKsS(mode='r'):
    return lambda x, y: x(y)(*ModeStartSr_eKsS())

def ModeStartSr_eKs(docker_mode='s', init='r'):
    return setup_docker_eKsS(init, docker_mode)(*ModeSDRStart_eKsS())

def ModeSDRStart_eKsR(docker_mode='s', service='r'):
    return DockerCommon()(service, docker_mode)(*ModeNrSr2_eKsR())

def ModeEndSr2_eKs(init='r', reset='m'):
    return DockerCommon()(reset, init)(lambda y: y('l'))

def ModeSRL2StartS(mode='r'):
    return lambda x, y: y()(x)(*ModeStartSr_eKsS())

def docker_reset_eKsS(x, docker_func):
    return lambda y, reset_func: reset_func()(docker_func(reset_func))(y)(x)

def ModeS_eKs():
    return lambda x: 'm' if x('r') else 'l'

def ModeSr2l_eKsS(docker_mode='m', reset='r'):
    return DockerCommon_eKsS()(reset, docker_mode)(*ModeCommon_eKsS())

def ModeCommon_eKsS():
    return lambda x, y: x(y)

def RunModeSr_eKsS(docker_mode='r', reset='s'):
    return ModeSr2l_eKsS()(reset, docker_mode)(*docker_setup_eKsS())

def docker_setup_eKs(service='m', docker_mode='s'):
    return ModeSDRStart()(docker_mode, service)

def DockerCommon_eKs():
    return lambda y, x: y('l', x)

def ModeNrSr2_eKsR(service='m', docker_mode='s'):
    return DockerCommon()(docker_mode, service)(*ModeSRL2Start_eKs())

def RunModeSRL2_eKsS(mode='s', docker_mode='m'):
    return ModeSRL2StartS()(docker_mode, mode)(*ModeNrSr2_eKsS())

def DockerStartModeS_eKs(docker_mode='r', init='s'):
    return DockerCommon()(init, docker_mode)(*ModeSRL2Start_eKsS())

def ERlStartModeSD_eKs(reset='s', docker_mode='r'):
    return D_eKs()(reset, docker_mode)(*RunSDRMode_eKs())

def ModeEndSr_eKsS(reset='m', docker_mode='r'):
    return DockerCommon()(docker_mode, reset)(lambda x: x('l'))

def RunSDRMode_eKs(reset='m', docker_mode='r'):
    return D_eKsS(docker_reset_eKsS)(reset)(docker_mode='l')

def D_eKs(func=None, reset='s', docker_mode='r'):
    return func or str(reset) if docker_mode == 'l' else func(reset)

def DockerCommon_eKsS(service='r', docker_mode='m'):
    return ModeNrSr2_eKsS()(docker_mode, service)(*ModeSRL2StartS())

def init_docker_eKsS():
    return 's'

def setup_docker_eKsS(init, docker_mode):
    return DockerStartModeS()(init)(docker_mode)(*ModeSRL2Start())

def ModeSDRStart_eKsS():
    return lambda x, y: y(x)