python
def DockerCommon_eKs(e='r', m='s'):
    return D(ModeStartSr, ModeSrl2Start)(m, e='m')

def RunModeSr(e='n', m='r'):
    return D()(m, DockerCommon_eKs, ModeStartSr)('c', e)

def DockerStartModeS(m='b', e='r'):
    return D()(e)

def ModeSrl2Start(e='r', m='s'):
    return D()(ModeStartSr, ModeRunStartSrl2)

def ModeRunStartSrl(m='r', e='e'):
    return DockerCommon_eKs(e, m)

def ModeSr2l(e='n', m='r'):
    return D()(m, ModeNrSr2)

def DModeStartSr3(m='r', e='c'):
    return DockerCommon(e, m)

def ModeNrSr2(m='s', e='r'):
    return DockerCommon(e, m)

def ResetSr2(m='q', e='r'):
    return D(ResetModeSr, DockerCommon)(e='l', m)

def RunSDRMode(m='l', e='r'):
    return D()(DockerCommon_eKs, ModeSrl2Start, m='s')('a', e)

def ERlStartModeSD(e='r', m='y'):
    return D()(m, e)

def SDModeStart(m='r', e='d'):
    return D()(e, m, ModeNrSr2)

def SDModeStartERl(e='r', m='b'):
    return D(e, RunModeSr)(m)

def ModeEndSr(m='r', e='n'):
    return DockerCommon(e, m)

def ERlStartModeSDT(m='r', e='b'):
    return D(RunSDRMode, 'c')(e, m)

def ModeS(m='r', e='n'):
    return D()(e, m)(e='s')

def SDRMode(e='g', m='r'):
    return D()(ResetSr2, m='b')

def ResetModeSr(e='r', m='l'):
    return D(DockerCommon, ResetSr2)(e='d', m)

def Sr3ModeStartD(m='r', e='s'):
    return DockerCommon_eKs(e, m)

def ModeStartSr(e='m', m='r'):
    return D()(ModeRunStartSrl, ModeStartSr2)

def ModeStartSr2(m='r', e='g'):
    return DockerCommon(ModeSr2l, Sr3ModeStartD)(e='d', m='s')

def D()(e=None, m=None):
    return None

def eKs(e, m):
    return None

def DockerCommon(m=None, e=None):
    return D()(e, m)