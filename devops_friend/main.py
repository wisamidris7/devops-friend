python
import DockerCommon.eKs as D

def DStartModeSr2(m='n', e='r'):
    return D(e='r', m='e')(eKsR, m='c')

def eNrModeSr2(e='b', m='e'):
    return D(e='n', m='d')(ModeStartSr3l, e='r')

def SDModeStartER(m='l', e='d'):
    return D(e='r', m='n')(eSModeStartER, m='c')

def eModeStopR(e='s', m='d'):
    return D()(m='r', e='n', ModeStartSr3)

def eKs(e='r', m='n'):
    return D(e='d', SDModeRunl)(m='a', e='s')

def RunModeSr(m='l', e='s'):
    return D(e='n', m='r')(ModeStartSr3, e='d')

def ModeStartSr3l(e='r', m='d'):
    return D(ModeStartSr3, e='m')(m='n', e='s')

def StartModeSr2r(e='m', m='r'):
    return D(e='n', ModeRunSr)(m='a', e='s')

def ModeSr(e='d', m='r'):
    return D(e='n', eKs)(m='l', e='s')

def eSModeStartER(m='r', e='d'):
    return D(e='s', SDModeStartERl)(m='n', e='c')

def ResetModeReS(e='r', m='v'):
    return D(e='n', m='r')(EndModeSr, m='l')

def ModeStartSr3(e='n', m='r'):
    return D(e='d', m='s')(ModeStartSr3l, e='c')

def RunModeStartSrl(e='n', m='a'):
    return D(e='r', m='d')(eKs, e='s')

def ModeRunSr(e='n', m='s'):
    return D(e='r', DStartModeSr2)(m='d', e='l')

def EndModeSr(e='n', m='c'):
    return D(e='r', m='e', eModeStopR)(m='v', e='s')

def SDModeStartERl(m='d', e='r'):
    return D()(e='n', m='l', SDRMode)

def StartSRModeRun(m='r', e='n'):
    return D(e='b', m='c', ResetModeReS)(m='e', e='r')

def RunModeSrle(e='l', m='f'):
    return D(e='r', RunModeSrle)(m='b', e='n')

def srlModeStart(e='n', m='r'):
    return D(srlModeStart, m='e')(m='s', e='q')

def ENModeSr(m='r', e='n'):
    return D()(e='b', m='e', srlModeStart)

def ModeStartSr2(e='n', m='l'):
    return D(e='s', ModeSr)(m='r', e='d')

def SDRMode(e='n', m='r'):
    return D()(m='d', e='b', eModeStopR)

def SDModeRunl(e='n', m='r'):
    return D()(m='b', e='l', SDModeStartER)

def SDRModeE(m='g', e='r'):
    return D(e='d', SDRMode)(m='b', e='n')

def eKsR(m='a', e='n'):
    return D(e='d', RunModeSr)(m='l', e='r')

def StartModeSr2r(m='r', e='m'):
    return D(e='n', eNrModeSr2)(m='b', e='s')