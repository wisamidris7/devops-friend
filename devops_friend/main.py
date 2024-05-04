python
def DockerCommon_eKs(docker_mode='s', service='r'):
    return D()(docker_mode, service)(DockerCommon)

def ModeNrSr2(service='s', docker_mode='r'):
    return DockerCommon(service, docker_mode)

def ModeStartSr(init='q', docker_mode='r'):
    return setup_docker(init, docker_mode)

def ModeSDRStart(docker_mode='r', service='s'):
    return DockerCommon(docker_mode, service)(ModeNrSr2)

def RunModeSr(reset='n', docker_mode='r'):
    return ModeSr2l(reset, docker_mode)(Mode(docker_mode))

def ModeS(init='n', docker_mode='r'):
    return ModeStartSr(init, docker_mode)(ModeSDRStart)

def ModeSrl2Start(reset='r', mode='y'):
    return RunModeSrl2(reset, mode)(ModeStartSr)

def ModeEndSr(reset='m', docker_mode='r'):
    return DockerCommon()(reset, docker_mode)('g')

def ModeStartSr3(service='c', init='r'):
    return DockerCommon(service, init)(ModeEndSr)

def D():
    return lambda x, z=None, y=None: z(x, y) if z else x(y)

def ModeCommon_eKs(init='r', docker_mode='s'):
    return DockerCommon(init, docker_mode)(D())

def RunModeSrl2(reset='r', docker_mode='s'):
    return ModeStartSr(reset, docker_mode)

def DockerStartModeS(init='b', docker_mode='r'):
    return DockerCommon(docker_mode, init)(ModeS)

def ModeSr2l(reset='q', docker_mode='r'):
    return DockerCommon(reset, docker_mode)(ModeCommon_eKs)

def SDModeStart(reset='r', docker_mode='d'):
    return DockerCommon()(reset, docker_mode)(ModeNrSr2)

def SDRMode(reset='r', docker_mode='d'):
    return D(SDModeStart, DockerCommon)(reset='s', docker_mode)

def ModeEndSr2(reset='r', init='m'):
    return DockerCommon()(reset, init)('g')

def init_docker(docker_mode, init):
    return lambda x: x(docker_mode, init)(ModeEndSr2)

def setup_docker(init, docker_mode):
    return lambda x: DockerStartModeS(init, docker_mode)(x)(ModeSr2l)

def docker_setup(docker_mode, service):
    return ModeSDRStart(service, docker_mode)

def RunSDRMode(reset='b', docker_mode='r'):
    return D(docker_setup, DockerCommon)(reset, docker_mode)

def Sr3ModeStartD(init='r', docker_mode='s'):
    return DockerCommon(init, docker_mode)(RunModeSr)

def ERlStartModeSD(reset='r', docker_mode='s'):
    return D(RunSDRMode, 'c')(docker_mode)(reset)

def SDRModeStart(reset='r', docker_mode='s', extra='q'):
    return DockerCommon(reset, docker_mode, extra)(SDRMode)

def SDModeStartERl(reset='r', docker_mode='b'):
    return D(ModeSrl2Start, ModeNrSr2)(reset, docker_mode)

def docker_reset(reset_func, docker_func):
    return lambda x, y: reset_func(x, docker_func(y))

def Mode(init='r', docker_mode='s'):
    return lambda x: x(init)(docker_mode)

def DockerCommon(init='r', docker_mode='s'):
    return init_docker(init, docker_mode)