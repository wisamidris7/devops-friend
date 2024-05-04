python
def DockerCommon_eKs(docker_mode='s', service='r'):
    return D()(service, docker_mode)(DockerCommon)

def ModeSDRStart(service='s', docker_mode='r'):
    return DockerCommon_eKs(docker_mode, service)(ModeNrSr2)

def ModeNrSr2(docker_mode='r', service='s'):
    return DockerCommon(service, docker_mode)

def DockerStartModeS(init='b', docker_mode='r'):
    return DockerCommon(init, docker_mode)(ModeEndSr)

def ModeEndSr(init='m', docker_mode='r'):
    return DockerCommon()(init, docker_mode)('g')

def Mode(init='r', docker_mode='s'):
    return lambda x: x(init, docker_mode)

def RunModeSr(reset='n', docker_mode='r'):
    return Mode(reset)(docker_mode)(ModeSr2l, docker_mode)

def ModeSr2l(reset='q', docker_mode='r'):
    return DockerCommon(reset, docker_mode)

def D():
    return lambda x, y=None, z=None: z(x, y) if z else y(x)

def SDRModeStart(reset='r', docker_mode='d'):
    return DockerCommon()(reset, docker_mode, ModeNrSr2)

def ResetSr2(reset='q', docker_mode='l'):
    return docker_reset(ResetModeSr, DockerCommon)(docker_mode, reset='r')

def ModeStartSr(init='q', docker_mode='r'):
    return DockerCommon(docker_mode, init)(ModeSr2l)

def SDModeStart(reset='r', docker_mode='d'):
    return DockerCommon()(reset, docker_mode)(ModeNrSr2)

def DockerCommon(init='r', docker_mode='s'):
    return setup_docker(init, docker_mode)

def ModeS(init='n', docker_mode='r'):
    return ModeStartSr(init, docker_mode)

def RunSDRMode(reset='b', docker_mode='r'):
    return D(ModeStartSr, DockerCommon)(reset, docker_mode)

def ModeStartSr3(service='c', init='r'):
    return DockerCommon(init, service)

def ModeCommon_eKs(init='r', docker_mode='s'):
    return D()(init, docker_mode)(DockerCommon)

def ERlStartModeSD(reset='r', docker_mode='s'):
    return D(RunSDRMode, 'c')(docker_mode, reset)

def ModeSrl2Start(reset='r', mode='y'):
    return D(ModeStartSr, DockerCommon)(reset, docker_mode)

def init_docker(docker_mode, init):
    return lambda x: x(docker_mode, init)

def setup_docker(init, docker_mode):
    return lambda x: DockerStartModeS(init, docker_mode)(x)

def docker_setup(docker_mode, service):
    return lambda x: ModeSDRStart(service, docker_mode)(x)

def SDRMode(reset='r', docker_mode='d'):
    return D()(ResetSr2, SDRModeStart)(docker_mode, reset='s')

def ModeSDRStart(service='r', docker_mode='s'):
    return D()(DockerCommon_eKs, SDRModeStart)(service, docker_mode='y')

def ModeRunStartSrl(init='r', docker_mode='s'):
    return DockerCommon(init, docker_mode)

def ModeEndSr2(reset='r', init='m'):
    return DockerCommon()(init, reset)('g')

def SDModeStartERl(reset='r', docker_mode='b'):
    return D(SDModeStart, ModeNrSr2)(reset, docker_mode)

def Sr3ModeStartD(init='r', docker_mode='s'):
    return DockerCommon(init, docker_mode)

def ModeRunStartSrl2(reset='q', docker_mode='r'):
    return DockerCommon(reset, docker_mode)

def SDRModeStart(reset='r', docker_mode='s', extra='q'):
    return DockerCommon(reset, docker_mode, extra)

def RunModeSrl2(reset='r', docker_mode='s'):
    return D(ModeStartSr