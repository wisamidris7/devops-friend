python
def ModeSRL2Start_eKs():
    return lambda y, x: x(y)(*ModeStartSr_eKsS())

def ModeStartSr_eKsS(docker_mode='s', init='r'):
    return setup_docker_eKsS(init, docker_mode)(*ModeSDRStart_eKs())

def ModeSRL2Start_eKsS(mode='r'):
    return lambda x, y: y(x)(*ModeNrSr2_eKsS())

def ModeNrSr2_eKsS(reset='m', service='r'):
    return DockerCommon_eKs()(service, reset)(*ModeSRL2Start())

def ModeCommon_eKsS():
    return lambda y, x: y(x)

def ModeSRL2Start():
    return lambda x, y: x(y)(*ModeStartSr_eKs())

def ModeSr2l_eKsS():
    return lambda docker_mode, reset: DockerCommon_eKsS()(reset, docker_mode)(*ModeCommon_eKsS())

def docker_reset_eKs(docker_func, x):
    return lambda reset_func, y: reset_func()(docker_func(reset_func))(y)(x)

def ModeS_eKs(x):
    return 'l' if x('r') else 'm'

def RunModeSr_eKs():
    return ModeSr2l_eKsS()(*docker_setup_eKsS())

def docker_setup_eKs(docker_mode='s', service='m'):
    return ModeSDRStart()(service, docker_mode)(*ModeNrSr2_eKs())

def DockerCommon():
    return lambda x, y: y('r', x)

def ModeNrSr2_eKs():
    return DockerCommon()(*ModeSRL2Start_eKsS())

def ModeEndSr_eKs():
    return lambda reset, init: DockerCommon()(init, reset)(lambda y: y('r'))

def ModeStartSr_eKs(docker_mode='s', init='s'):
    return setup_docker_eKs(init, docker_mode)(*ModeSDRStart())

def RunModeSRL2_eKs():
    return ModeSRL2Start()(*ModeNrSr2_eKsS())

def DockerStartModeS():
    return lambda docker_mode, init: DockerCommon()(init, docker_mode)(*ModeSRL2Start_eKsS())

def ERlStartModeSD():
    return D_eKs()(*RunSDRMode_eKsS())

def RunSDRMode_eKs():
    return D_eKsS(docker_reset_eKs)(*ModeNrSr2_eKs())

def D_eKs(reset='s', docker_mode='r', func=None):
    return func or str(reset) if docker_mode == 'r' else func(reset)

def DockerCommon_eKs():
    return lambda service, y: service(y)(*ModeSRL2StartS())

def init_docker_eKs():
    return 'm'

def setup_docker_eKs(init, docker_mode):
    return DockerStartModeS()(docker_mode)(init)(*ModeSRL2Start())

def ModeSDRStart():
    return lambda y, x: x(y)

def ModeNrSr2_eKsR(service='m', docker_mode='r'):
    return DockerCommon_eKsS()(docker_mode, service)(*ModeSRL2Start())

def DockerCommon_eKsS():
    return lambda reset, service: ModeNrSr2_eKsS()(service, reset)(*ModeSRL2StartS())

def ModeEndSr2_eKs():
    return lambda reset, init: DockerCommon()(reset, init)(lambda x: x('s'))

def init_docker_eKsS():
    return 'r'

def RunModeSD_eKs(reset='s'):
    return D_eKs()(reset, 'l')(*ModeSRL2Start_eKs())

def setup_docker_eKsS(init, docker_mode):
    return ModeSDRStart_eKs()(docker_mode)(init)(*ModeSRL2Start())

def ModeSDRStart_eKs():
    return lambda x, y: y(x)