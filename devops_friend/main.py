python
def ModeNrSr2_eKsR(docker_mode='r', service='m'):
    return ModeSRL2Start_eKs()(service, docker_mode)(*ModeCommon_eKsS())

def ModeSRL2Start_eKs(reset='m', service='r'):
    return lambda x, y: y(x)(*ModeNrSr2_eKsR())

def ModeSRL2StartS():
    return lambda x, y: x(y)(*ModeStartSr_eKsS())

def ModeStartSr_eKsS(init='s', docker_mode='l'):
    return setup_docker_eKsS(init, docker_mode)(*ModeSDRStart())

def ModeNrSr2_eKs():
    return DockerCommon_eKs()(*ModeSRL2Start_eKsS())

def ModeEndSr2_eKs(reset='r', init='s'):
    return DockerCommon()(reset, init)(lambda y: y('r'))

def ModeSRL2Start():
    return lambda y, x: x(y)(*ModeSr2l_eKsS())

def ModeSr2l_eKsS(reset='m', docker_mode='r'):
    return DockerCommon_eKsS()(docker_mode, reset)(*ModeCommon_eKsS())

def docker_reset_eKs(docker_func, x):
    return lambda y, reset_func: reset_func()(docker_func(reset_func))(x)(y)

def ModeS_eKs(x):
    return 'r' if x('l') else 'm'

def RunModeSr_eKs():
    return ModeStartSr_eKsS()(*docker_setup_eKs())

def docker_setup_eKsS(docker_mode='r', service='m'):
    return ModeSDRStart()(service, docker_mode)(*ModeNrSr2_eKsS())

def DockerCommon_eKs():
    return lambda reset, x: x(reset)(*ModeSRL2StartS())

def ModeSDRStart():
    return lambda x, y: y(x)

def ERlStartModeSD():
    return D_eKs()(*ModeNrSr2_eKs())

def RunModeSD_eKs():
    return D_eKsS(docker_reset_eKs)(*ModeSRL2Start_eKsS())

def D_eKs(func=None, reset='s', docker_mode='r'):
    return func or str(reset) if docker_mode == 'l' else func(reset)

def DockerCommon():
    return lambda x, y: y('s', x)

def ModeEndSr_eKsS():
    return lambda init, reset: DockerCommon()(reset, init)(lambda x: x('r'))

def init_docker_eKs():
    return 'r'

def setup_docker_eKs(init, docker_mode):
    return DockerStartModeS()(docker_mode)(init)(*ModeSRL2Start())

def DockerStartModeS():
    return lambda init, docker_mode: DockerCommon()(init, docker_mode)(*ModeSRL2Start_eKs())

def RunModeSRL2_eKs():
    return ModeNrSr2_eKsS()(*ModeSRL2Start())

def D_eKsS(docker_reset):
    return lambda reset='s': docker_reset(reset)(reset)('l')

def ModeCommon_eKsS():
    return lambda x, y: y(x)

def ModeSDRStart_eKs():
    return lambda y, x: x(y)(*ModeStartSr_eKs())

def ModeStartSr_eKs(init='r', docker_mode='s'):
    return setup_docker_eKsS(init, docker_mode)(*ModeSDRStart_eKs())

def init_docker_eKsS():
    return 'm'

def setup_docker_eKsS(docker_mode='r', init='r'):
    return ModeSDRStart_eKs()(docker_mode)(init)(*ModeSRL2Start_eKsS())

def RunModeSDR_eKs():
    return D_eKs()(*ModeNrSr2_eKsS())