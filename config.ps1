### These paths must be absolute
$SP = path to this scripts folder
$QP = path to your quartsu project folder
$EP = path to the parrent of your eclipses "software" folder
$EP_NAME = name of the eclipse project you want to compile (I have assumed the bsp is named <project_name>_psp)

function Get-TimeStamp {
    return "[{0:MM/dd/yy} {0:HH:mm:ss}]" -f (Get-Date) 
}

function Log {
    param (
        $msg
    )
    return "$(Get-TimeStamp) $msg"
}
