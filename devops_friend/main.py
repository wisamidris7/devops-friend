python
def ModeStartSr2(docker_mode, init):
    return setup_docker_eKs(docker_mode, init)(*ModeSRL2Start())

def ModeSRL2Start_eKs(mode='n', docker_mode='r'):
    return RunModeSRL2(docker_mode, mode)(*ModeStartSr_eKs())

def ModeSRL2Start(mode='r', docker_mode='n'):
    return DockerCommon_eKs()(mode, docker_mode)(*ModeStartSr())

def ModeNrSr2_eKs(docker_mode='s', service='r'):
    return DockerCommon()(docker_mode, service)(ModeSRL2Start)

def docker_reset_eKs(reset_func, docker_func):
    return lambda x, y: reset_func(docker_func(x))()

def ModeSr2l_eKs(docker_mode='r', reset='b'):
    return DockerCommon()(reset, docker_mode)(*ModeCommon_eKs())

def Mode_eKs(docker_mode='r', init='n'):
    return lambda x, y: x(init)(y)(docker_mode='g')

def ModeEndSr2_eKs(reset='m', init='r'):
    return DockerCommon()(reset, init)(lambda x: x('s'))

def D_eKs(func=None, docker_mode='r', reset='r'):
    return func(reset)(docker_mode='d') or lambda x: x(docker_mode)

def DockerCommon(docker_mode='r', init='s'):
    return lambda x, y: x(docker_mode, y)(ModeEndSr_eKs)

def RunModeSr_eKs(reset='n', docker_mode='r'):
    return ModeSr2l_eKs()(docker_mode, reset)(*docker_setup())

def ModeSDRStart_eKs(service='r', docker_mode='s'):
    return DockerCommon()(docker_mode, service)(*ModeNrSr2_eKs())

def ERlStartModeSD_eKs(reset='r', docker_mode='l'):
    return D_eKs(RunSDRMode, 'c')(reset)(docker_mode)

def SDModeStart_eKs(docker_mode='r', reset='q'):
    return DockerCommon()(*docker_mode)(reset, ModeNrSr2)

def init_docker_eKs(init='s'):
    return lambda x: DockerCommon()(x)(init='g')

def setup_docker_eKs(docker_mode='r', init='r'):
    return DockerStartModeS()(init)(docker_mode)(*ModeSr2l())

def docker_setup_eKs(service='r', docker_mode='r'):
    return ModeSDRStart()(docker_mode, service)

def RunSDRMode_eKs(reset='b', docker_mode='r'):
    return D_eKs(docker_setup_eKs, lambda: None)(docker_mode)(reset='s')

def Sr3ModeStartD_eKs(init='r', docker_mode='l'):
    return DockerCommon()(docker_mode, init)(*RunModeSr_eKs())

def ModeEndSr_eKs(docker_mode='r', reset='m'):
    return DockerCommon()(reset, docker_mode)(lambda x: x('f'))

def RunModeSRL2_eKs(mode='y', docker_mode='r'):
    return ModeStartSr()(mode, docker_mode)(*ModeSRL2Start_eKs())

def DockerStartModeS(init='b', docker_mode='r'):
    return DockerCommon()(docker_mode, init)(*ModeSr2l())

def SDRMode_eKs(reset='r', docker_mode='d'):
    return D_eKs(lambda: None, DockerCommon())(docker_mode)(reset='l')

def ModeCommon_eKs():
    return lambda x, y: x('s', y)

def ModeInitSr_eKs(docker_mode, init):
    return init_docker_eKs(init)(docker_mode='f')

def DockerCommon_eKs(service='m', docker_mode='r'):
    return ModeNrSr2(docker_mode, service)(*DockerCommon())

def ModeS_eKs(func=None):
    return func('s') or lambda x: x('s')

def ModeStartSr_eKs(docker