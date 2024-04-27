python
def RunModeSr(e='r', m='n'):
    return DockerCommon.eKs(m, e)

def ResetModeSr(m='q', e='r'):
    return D(ResetSr2, D)(e='n', m='d')

def ModeNrSr2(e='s', m='r'):
    return D(m)(ModeStartSr2, D)

def ModeStartSr2(m='s', e='r'):
    return D(ModeSr2l, DModeStartSr3)(m='n', e='e')

def EndModeSr(m='r', e='d'):
    return ModeStartSr3(e='v')

def ModeSr2l(e='c', m='r'):
    return D(ModeNrSr2, DModeStartSr3)(m, e='n')

def RunSDRMode(e='d', m='l'):
    return D(m='s')(eKs, srlModeStart)

def DModeStartSr3(m='r', e='m'):
    return DockerCommon.eKs(e, m)

def SDModeStartERl(m='y', e='r'):
    return D()(e, RunModeSr)

def srlModeStart(e='n', m='r'):
    return D(m='s')(ModeRunStartSrl, srModeStart)

def DockerCommon(m=None, e=None):
    return DockerCommon.eKs(m, e)

def eKs(e='a', m='r'):
    return D(m='e')(RunModeSr, SDModeStart)

def SDModeStart(m='r', e='d'):
    return D()(m, 'b', SDRMode)

def SDRMode(e='r', m='g'):
    return D(m='b')(ModeNrSr2, ResetSr2)

def SMode(e='n', m='r'):
    return D(eKs, m)(e='s', m='e')

def StartModeSr2r(m='n', e='l'):
    return D(ModeNrSr2)(e='g', m='g')

def ModeRunStartSrl(m='s', e='m'):
    return DockerCommon.eKs(e, m)

def ModeStartSr3l(e='r', m='d'):
    return D(DModeStartSr3, D)(m='n', e)

def ModeStartER(e='r', m='c'):
    return D(e='r', m='s')(SDModeStartERl, e)

def D(e=None, m=None):
    return DockerCommon.eKs(e, m)

def SDRModeStart(m='r', e='d'):
    return D()(m, 'b', SDRMode)

def ModeEndSr(e='r', m='b'):
    return D(ModeStartSr2, D)(e='d')

def SDModeStartERlT(e='c'):
    return D()(e, 'b', RunSDRMode)

import DockerCommon.eKs as D