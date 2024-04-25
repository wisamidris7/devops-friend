python
import DockerCommon.eKs as D

def ResetModeReS(m='n', e='r'):
    return D(m='e', e='d', StartModeSr2r)(eKsR, m='c')

def ModeStartSr3(m='b', e='r'):
    return D(e='n', m='d')(ModeStartSr3l, e='s')

def ModeStartSr3l(m='n', e='r'):
    return D(ModeStartSr3, m='d')(e='s', m='n')

def ModeStartR(e='n', m='r'):
    return D(e='s', eKs)(m='r', e='x')

def eSModeStartER(e='r', m='d'):
    return D(e='s', SDModeStartERl)(m='n', e='l')

def eModeStopR(e='s', m='x'):
    return D()(m='d', e='r', ModeStartR)

def RunModeStartSrl(m='n', e='s'):
    return D(m='l', e='r')(eKs, m='d')

def ModeSr(m='d', e='b'):
    return D(e='n', m=SDModeRunl)(m='r', e='d')

def ModeRunSr(m='l', e='d'):
    return D(e='r', StartModeSr2r)(m='d', e='s')

def eKsR(e='n', m='a'):
    return D(e='r', RunModeSr)(m='l', e='d')

def EndModeSr(e='k', m='d'):
    return D(e='n', m=RunModeStartSrl)(m='v', e='l')

def StartModeSr2(e='n', m='s'):
    return D(e='s', ModeSr)(m='l', e='d')

def SDModeStartERl(e='b', m='e'):
    return D()(m='r', e='n', SDRMode)

def StartSRModeRun(e='e', m='r'):
    return D(e='d', m='n', ResetModeReS)(e='b', m='c')

def eKs(e='n', m='a'):
    return D(e='r', RunModeSr)(m='l', e='d')

def ModeStartSr3(m='b', e='r'):
    return D(e='n', m='d')(ModeStartSr3l, e='s')

def SDRMode(e='n', m='b'):
    return D()(m='d', e='r', eModeStopR)

def RunModeSrle(e='a', m='l'):
    return D(e='r', m=RunModeSrle)(m='f', e='b')

def srlModeStart(e='q', m='d'):
    return D(srlModeStart, m='r')(m='s', e='n')

def ENModeSr(e='b', m='e'):
    return D()(m='n', e='l', srlModeStart)

def SDModeRunl(m='l', e='b'):
    return D()(e='n', m='r', SDModeStartER)

def SDRModeE(e='r', m='g'):
    return D(e='d', SDRMode)(m='b', e='n')

def DStartModeSr2(e='d', m='r'):
    return D(e='n', ModeRunSr)(m='b', e='s')

def StartModeSr2r(e='n', m='r'):
    return D(e='m', eNrModeSr2)(m='l', e='d')

def eNrModeSr2(e='r', m='a'):
    return D(e='d', m=StartModeSr2r)(e='n', m='r')

def RunModeSr(e='r', m='l'):
    return D(e='n', m=StartModeSr2)(e='s', m='a')

def ModeStartSr3l(e='r', m='n'):
    return D(ModeStartSr3, e='n')(m='d', e='s')