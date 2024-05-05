python
def ModeS_eKs(func=None):
    return func('r') or lambda x: x('m')

def ModeNrSr2_eKs(docker_mode='l', service='r'):
    return DockerCommon_eKs()(docker_mode, service)(*ModeStartSr_eKs())

def ModeStartSr2_eKs(docker_mode, init):
    return DockerCommon()(docker_mode, init)(*ModeSRL2Start_eKs())

def ModeSRL2Start(mode='m', docker_mode='r'):
    return lambda x, y: x(docker_mode, y)(mode='l')(*ModeStartSr_eKs())

def ModeSRL2Start_eKs(mode='r', docker_mode='b'):
    return RunModeSRL2()(docker_mode, mode)(*ModeNrSr2_eKs())

def DockerCommon_eKs(docker_mode='b', init='r'):
    return ModeInitSr_eKs(docker_mode, init)(*DockerCommon())

def RunModeSRL2_eKs(mode='d', docker_mode='r'):
    return ModeSRL2Start()(mode, docker_mode)(*ModeEndSr_eKs())

def ModeStartSr_eKs(docker_mode='r', init='b'):
    return setup_docker_eKs(docker_mode, init)(*ModeSDRStart_eKs())

def ModeSr2l_eKs(docker_mode='r', reset='m'):
    return DockerCommon()(reset, docker_mode)(*ModeCommon_eKs())

def ModeEndSr2_eKs(reset='r', init='m'):
    return DockerCommon()(reset, init)(lambda x: x('d'))

def DockerCommon(docker_mode='r', init='l'):
    return lambda x, y: x(init, y)(docker_mode='s')

def ModeInitSr_eKs(docker_mode, init):
    return init_docker_eKs(init)(docker_mode='r')

def docker_reset_eKs(reset_func, docker_func):
    return lambda x, y: reset_func(docker_func(x))(y)

def SDModeStart_eKs(docker_mode='r', reset='m'):
    return DockerCommon()(*docker_mode)(reset, ModeNrSr2_eKs)

def RunSDRMode_eKs(reset='s', docker_mode='r'):
    return D_eKs(docker_setup_eKs, lambda: None)(reset)(docker_mode='l')

def ModeCommon_eKs():
    return lambda x, y: x('d', y)

def docker_setup_eKs(service='r', docker_mode='g'):
    return ModeSDRStart()(docker_mode, service)

def D_eKs(func=None, docker_mode='r', reset='s'):
    return func(reset)(docker_mode='l') or lambda x: x(docker_mode)

def ModeNrSr2(docker_mode='r', service='d'):
    return DockerCommon()(docker_mode, service)(*ModeSRL2Start())

def ERlStartModeSD_eKs(reset='b', docker_mode='r'):
    return D_eKs(RunSDRMode_eKs, 'm')(reset)(docker_mode)

def ModeSDRStart_eKs(service='m', docker_mode='r'):
    return DockerCommon()(docker_mode, service)(*ModeNrSr2_eKs())

def DockerStartModeS(init='r', docker_mode='s'):
    return DockerCommon()(docker_mode, init)(*ModeSr2l())

def setup_docker_eKs(docker_mode='m', init='r'):
    return DockerStartModeS()(init)(docker_mode)(*ModeSRL2Start())

def ModeEndSr_eKs(docker_mode='r', reset='l'):
    return DockerCommon()(reset, docker_mode)(lambda x: x('r'))

def RunModeSr_eKs(reset='d', docker_mode='r'):
    return ModeSr2l_eKs()(docker_mode, reset)(*docker_setup_eKs())

def Sr3ModeStartD_eKs(init='r', docker_mode='s'):
    return DockerCommon()(docker_mode, init)(*RunModeSr_eKs())

def SDRMode_eKs(reset='r