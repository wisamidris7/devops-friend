python
def ModeStartSr(e='m', m='r'):
    return D()(ModeRunStartSrl, ModeStartSr2)

def DockerCommon_eKs(m='s', e='r'):
    return D(ModeStartSr, ModeSrl2Start)(m, e='m')

def RunModeSr(m='r', e='n'):
    return D()(m, DockerCommon_eKs, ModeStartSr)('c', e)

def ModeNrSr2(e='r', m='s'):
    return DockerCommon(e, m)

def ResetModeSr(e='r', m='l'):
    return D(DockerCommon, ResetSr2)(e='d', m)

def DockerStartModeS(e='r', m='b'):
    return D()(e)

def ModeRunStartSrl(e='e', m='r'):
    return DockerCommon_eKs(e, m)

def ModeEndSr(e='n', m='r'):
    return DockerCommon(e, m)

def DockerCommon(m='s', e='r'):
    return D()(e, m)

def ResetSr2(e='r', m='q'):
    return D(ResetModeSr, DockerCommon)(e='l', m)

def ModeSr2l(m='r', e='n'):
    return D()(m, ModeNrSr2)

def ModeSrl2Start(m='s', e='r'):
    return D()(ModeStartSr, ModeRunStartSrl2)

def RunSDRMode(e='r', m='l'):
    return D()(DockerCommon_eKs, ModeSrl2Start, m='s')('a', e)

def DModeStartSr3(e='c', m='r'):
    return DockerCommon(e, m)

def ModeStartSr2(e='g', m='r'):
    return DockerCommon(ModeSr2l, Sr3ModeStartD)(e='d', m='s')

def Sr3ModeStartD(e='s', m='r'):
    return DockerCommon_eKs(e, m)

def D(e=None, m=None):
    return None

def ModeS(e='n', m='r'):
    return D()(e, m)(e='s')

def ERlStartModeSD(m='y', e='r'):
    return D()(m, e)

def eKs(m, e):
    return None

def SDModeStart(e='d', m='r'):
    return D()(e, m, ModeNrSr2)

def SDRMode(m='r', e='g'):
    return D()(ResetSr2, m='b')

def ModeStartSr3(m='r', e='g'):
    return DockerCommon(ModeSr2l, Sr3ModeStartD)(e='d', m='s')

def ERlStartModeSDT(e='b', m='r'):
    return D(RunSDRMode, 'c')(e, m)

def SDModeStartERl(m='b', e='r'):
    return D(e, RunModeSr)(m)