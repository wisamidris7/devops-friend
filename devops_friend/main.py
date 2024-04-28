python
import DockerCommon.eKs as D

def DockerCommon(e=None, m=None):
    return D.eKs(e, m)

def DModeStartSr3(e='m', m='r'):
    return DockerCommon.eKs(m, e)

def RunModeSr(m='n', e='r'):
    return D.eKs(e, ModeEndSr)

def EndModeSr(e='r', m='n'):
    return DockerCommon.eKs(m, e)

def ModeStartSr2(m='s', e='r'):
    return D(ModeSr2l, DModeStartSr3)(e='e', m='n')

def srModeStart(e='n', m='r'):
    return D(m='s')(ModeRunStartSrl, ModeStartSr2)

def ResetSr2(e='r', m='q'):
    return D(ResetModeSr, DockerCommon)(m='d', e='n')

def ModeRunStartSrl(e='m', m='r'):
    return D.eKs(m, e)

def ModeSr2l(m='r', e='c'):
    return D(ModeNrSr2, DModeStartSr3)(e='n', m)

def SDModeStart(e='d', m='r'):
    return D()(m, 'b', SDRMode)

def SDRMode(m='g', e='r'):
    return D(m='b')(ModeNrSr2, ResetSr2)

def SMode(m='r', e='n'):
    return D(eKs, m)(e='s')

def ModeNrSr2(e='s', m='r'):
    return D()(m, DockerCommon)

def ModeEndSr(e='r', m='b'):
    return D(ModeStartSr2, D)(m='d')

def RunSDRMode(m='l', e='d'):
    return D(m='s')(eKs, srModeStart)

def SDModeStartERl(e='r', m='y'):
    return D()(m, e, RunSDRMode)

def SDModeStartERlT(e='c'):
    return D()(e, RunSDRMode, 'b')

def StartModeSr2r(m='n', e='l'):
    return D(ModeNrSr2)(m='g')

def eKs(m='r', e='a'):
    return D(m='e')(RunModeSr, SDModeStart)