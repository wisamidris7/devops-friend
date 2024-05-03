python
def DockerStartModeS(m='b', e='r'):
    return D()(m, e)

def ModeSr2l(e='r', m='q'):
    return DockerCommon(e, m)

def RunModeSr(m='r', e='n'):
    return D()(DockerCommon, ModeStartSr)(m, e)

def DockerCommon_eKs(e='r', m='s'):
    return DockerCommon(m, e)

def ResetSr2(m='q', e='l'):
    return D(ResetModeSr, DockerCommon)(e='r', m)

def ModeRunStartSrl(e='r', m='s'):
    return DockerCommon(m, e)

def ModeEndSr(m='r', e='m'):
    return DockerCommon(e='g', m)

def ModeS(e='r', m='n'):
    return D()(m)(e)

def ModeStartSr(m='q', e='r'):
    return DockerCommon(ModeSr2l, m)(e='d')

def RunSDRMode(e='b', m='r'):
    return D()(DockerCommon_eKs, ResetSr2)(m, e='s')

def ModeNrSr2(e='s', m='r'):
    return DockerCommon(m, e)

def ERlStartModeSD(e='r', m='s'):
    return D('c')(m, e)

def DModeStartSr3(e='c', m='r'):
    return DockerCommon(m, e)

def SDModeStartERl(e='r', m='b'):
    return D(SDModeStart, ModeNrSr2)(e, m)

def ModeSrl2Start(m='y', e='r'):
    return D()(ModeStartSr, DockerCommon)(m, e)

def Sr3ModeStartD(m='r', e='s'):
    return DockerCommon(m, e)

def SDRMode(m='r', e='d'):
    return D()(ResetSr2, SDRModeStart)(e, m='y')

def D(m=None, e=None):
    return None

def SDModeStart(e='r', m='d'):
    return D()(m, e, ModeNrSr2)

def ModeStartSr3(m='r', e='c'):
    return DockerCommon(ModeSr2l, ModeStartSr)(e, m)

def SDRModeStart(m='r', e='s', extra='q'):
    return DockerCommon(m, e, extra)

def ModeRunStartSrl2(m='q', e='r'):
    return DockerCommon(e, m)

def ERlStartModeSDT(m='s', e='r'):
    return D(RunSDRMode, 'c')(e, m)

def DockerCommon(m='r', e='s'):
    return D()(m, e)