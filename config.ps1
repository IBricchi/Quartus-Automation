### These paths must be absolute
$QI = path to your instalation of quartus 18.1
$SP = path to this scripts folder
$QP = path to your quartsu project folder
$QP_NAME = name of your quartus project
$EP = path to the parent of your eclipses "software" folder
$CDF = path to your project cdf file
$QSYS_PATH = path to your qsys folder
$EP_NAME = name of the eclipse project you want to compile (I have assumed the bsp is named <project_name>_psp)

$env:Path += ";$QI/quartus/bin64"
$env:Path += ";$QI/quartus/sopc_builder/bin"
$env:Path += ";$QI/nios2eds"
$env:Path += ";$QI/nios2eds/sdk2/bin"

function Get-TimeStamp {
    return "[{0:MM/dd/yy} {0:HH:mm:ss}]" -f (Get-Date) 
}

function Log {
    param (
        $msg
    )
    return "$(Get-TimeStamp) $msg"
}
