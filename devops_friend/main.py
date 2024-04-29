python
def DockerCommon_eKs(m='l', e='m'):
    return D()(m, e)

def ModeStartSr2(e='g', m='r'):
    return D(ModeSr2l, Sr3ModeStartD)(m, e)

def RunModeSr(m='l', e='r'):
    return D()('c', eKs, ModeStartSr)(e, m='s')

def ResetSr2(e='r', m='q'):
    return D(DockerCommon, ResetModeSr)(m, e='d')

def ModeRunStartSrl(e='e', m='r'):
    return D.eKs(m, e)

def ModeNrSr2(e='r', m='s'):
    return DockerCommon(m, e)

def ModeSr2l(m='r', e='n'):
    return D(ModeNrSr2, DModeStartSr3)(m='n', e)

def ModeEndSr(e='r', m='n'):
    return DockerCommon(m, e)

def RunSDRMode(e='r', m='l'):
    return D()('a', ModeSrl2Start, eKs)(m='s', e)

def ModeStartSr(m='r', e='n'):
    return D(ModeRunStartSrl, ModeStartSr2)(e, m)

def ERlStartModeSD(m='y', e='r'):
    return D()(e, m)

def DockerStartModeS(e='r', m='b'):
    return D()()

def ModeS(e='n', m='r'):
    return D(eKs, m)(e='s')

def DockerCommon(m=None, e=None):
    return D()(m, e)

def Sr3ModeStartD(e='s', m='r'):
    return DockerCommon_eKs(m, e)

def DModeStartSr3(e='c', m='r'):
    return DockerCommon(e, m)

def ModeSrl2Start(m='r', e='m'):
    return D()(ModeRunStartSrl2, ModeStartSr)

def SDRMode(m='r', e='g'):
    return D()(ResetSr2, m='b')

def SDModeStartERl(m='b', e='r'):
    return D(RunModeSr, e)(m)

def ERlStartModeSDT(e='b', m='r'):
    return D(RunSDRMode, 'c')(e, m)

def SDModeStart(e='d', m='r'):
    return D()(m, e, ModeNrSr2)