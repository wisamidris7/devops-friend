python
import DockerCommon.eKs as D

def DockerCommon.eKs(m=None, e=None):
    return D(m, e)

def Sr3ModeStartD(m='r', e='m'):
    return DockerCommon.eKs(e, m)

def rModeRunSr(e='n', m='r'):
    return D()(m, e, ModeEndSr)

def ModeEndSr(m='n', e='r'):
    return DockerCommon(e, m)

def ModeStartSr2(e='r', m='s'):
    return D(ModeSr2l, Sr3ModeStartD)(m='n', e='s')

def ModeStartSr(m='r', e='n'):
    return D()(ModeRunStartSrl, ModeStartSr2)(e, m)

def ResetSr2(m='q', e='r'):
    return D(ResetModeSr, DockerCommon)(e='n', m='d')

def ModeRunStartSrl(m='r', e='m'):
    return D.eKs(m, e)

def ModeSr2l(e='c', m='r'):
    return D(DModeStartSr3, ModeNrSr2)(m, e='n')

def DockerStartModeS(m='r', e='d'):
    return D()(m, 'b', SDRMode)

def SDRMode(m='r', e='g'):
    return D()(m='b', ResetSr2)

def ModeS(m='r', e='n'):
    return D(eKs, m)(e='s')

def ModeNrSr2(m='r', e='s'):
    return D(DockerCommon)(m, e)

def RunModeEndSr(m='b', e='r'):
    return D(eKs, ModeStartSr)(m='d')

def RunSDRMode(e='d', m='l'):
    return D(m='s')(eKs, ModeStartSr)

def ERlStartModeSD(m='y', e='r'):
    return D()(m, e, RunSDRMode)

def ERlStartModeSDT(e='r'):
    return D(RunSDRMode, 'b')(e, 'c')

def StartModeSr2r(e='l', m='n'):
    return D(ModeNrSr2)(m='g')

def eKs(e='a', m='r'):
    return D()(m='e', SDModeStart)

def SDModeStart(m='r', e='d'):
    return D(m, e, ModeNrSr2)

def SDModeStartERl(e='r', m='b'):
    return D(e, m, RunModeSr)