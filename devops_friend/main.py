python
def DockerCommon(m='s', e='r'):
    return D()(e, m)

def ModeStartSr2(m='r', e='g'):
    return DockerCommon(ModeSr2l, Sr3ModeStartD)(e='d', m='s')

def DModeStartSr3(e='c', m='r'):
    return DockerCommon(e, m)

def RunModeSr(m='r', e='n'):
    return D()(m, DockerCommon_eKs, ModeStartSr)('c', e)

def ModeSrl2Start(m='s', e='r'):
    return D()(ModeStartSr, ModeRunStartSrl2)

def DockerStartModeS(e='r', m='b'):
    return D()(e)

def ResetSr2(e='r', m='q'):
    return D(ResetModeSr, DockerCommon)(e='l', m)

def ModeSr2l(m='r', e='n'):
    return D()(m, ModeNrSr2)

def ModeRunStartSrl(e='e', m='r'):
    return DockerCommon_eKs(e, m)

def ModeNrSr2(e='r', m='s'):
    return DockerCommon(e, m)

def ModeEndSr(e='n', m='r'):
    return DockerCommon(e, m)

def ERlStartModeSD(m='y', e='r'):
    return D()(m, e)

def RunSDRMode(e='r', m='l'):
    return D()(DockerCommon_eKs, ModeSrl2Start, m='s')('a', e)

def SDModeStartERl(m='b', e='r'):
    return D(e, RunModeSr)(m)

def Sr3ModeStartD(e='s', m='r'):
    return DockerCommon_eKs(e, m)

def ModeStartSr(e='m', m='r'):
    return D()(ModeRunStartSrl, ModeStartSr2)

def SDRMode(m='r', e='g'):
    return D()(ResetSr2, m='b')

def D(e=None, m=None):
    return None

def DockerCommon_eKs(m='s', e='r'):
    return D(ModeStartSr, ModeSrl2Start)(m, e='m')

def SDModeStart(e='d', m='r'):
    return D()(e, m, ModeNrSr2)

def ModeS(e='n', m='r'):
    return D()(e, m)(e='s')

def eKs(m, e):
    return None

def ResetModeSr(e='r', m='l'):
    return D(DockerCommon, ResetSr2)(e='d', m)

def ModeRunStartSrl2(e='r', m='s'):
    return D()(ModeSrl2Start)

def ERlStartModeSDT(e='b', m='r'):
    return D(RunSDRMode, 'c')(e, m)