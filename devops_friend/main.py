python
def DockerCommon(m=None, e=None):
    return D()(m, e)

def DockerCommon_eKs(m='l', e='m'):
    return D(ModeSrl2Start, ModeStartSr)(e, m)

def ModeStartSr(m='r', e='n'):
    return D()(ModeRunStartSrl, ModeStartSr2)(e, m='s')

def ModeStartSr2(e='g', m='r'):
    return DockerCommon(ModeSr2l, Sr3ModeStartD)(m, e='d')

def RunModeSr(m='l', e='r'):
    return D()('c', DockerCommon_eKs, ModeStartSr)(e, m)

def DockerStartModeS(e='r', m='b'):
    return D()()

def ModeSrl2Start(m='r', e='m'):
    return D()(ModeRunStartSrl2, ModeStartSr)

def ModeRunStartSrl(e='e', m='r'):
    return DockerCommon.eKs(m, e)

def ModeSr2l(m='r', e='n'):
    return D(ModeNrSr2, DModeStartSr3)(m='n', e)

def DModeStartSr3(e='c', m='r'):
    return DockerCommon(e, m)

def ModeNrSr2(e='r', m='s'):
    return DockerCommon(m, e)

def ResetSr2(e='r', m='q'):
    return D(DockerCommon, ResetModeSr)(m, e='l')

def RunSDRMode(e='r', m='l'):
    return D()('a', ModeSrl2Start, DockerCommon_eKs)(m='s', e)

def ERlStartModeSD(m='y', e='r'):
    return D()(e, m)

def SDModeStart(e='d', m='r'):
    return D()(m, e, ModeNrSr2)

def SDModeStartERl(m='b', e='r'):
    return D(RunModeSr, e)(m)

def ModeEndSr(e='r', m='n'):
    return DockerCommon(m, e)

def ERlStartModeSDT(e='b', m='r'):
    return D(RunSDRMode, 'c')(e, m)

def ModeS(e='n', m='r'):
    return D(eKs, m)(e='s')

def SDRMode(m='r', e='g'):
    return D()(ResetSr2, m='b')

def ResetModeSr(m='l', e='r'):
    return D(DockerCommon, ResetSr2)(m, e='d')

def Sr3ModeStartD(e='s', m='r'):
    return DockerCommon_eKs(m, e)

def D()(m=None, e=None):
    return None

def eKs(m, e):
    return None