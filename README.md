# This is a set of scripts for automating some parts of the quartus pipelining using NIOS2

## How the scripts work

In the example folder you'll find a simple example of the scripts being used to automate looping over a range of possible icache and dcache values. These files include comments to explain everything the uses script is doing.

The outline of the process is to:
1. Modify any files required for particular run
1. Check for cached version of quartus build if found copy over and ignore steps 3 and 4
1. Syntesis verilog for qsys file changes
1. Compile quartus project
1. Programme FPGA
1. Regenerate eclipse bsp
1. Build eclipse projects
1. Download elf
1. Read nios2-terminal and wait for data

## Modifications to get running

To get things running on your computer a few files need to be updated

1. You need to write your own script similar to example to acomplish your particular goal
1. You need to update config.ps1 with your particular paths as outlined in the file
1. You need to update quartus/programme.ps1 to point to your cdf file for programming the fpga
1. You need to update a path in the eclipse/build.ps1 file, there is an explanation of modifications required for your programme there
1. In build-all.ps1 look for the comment with "---START---" there is an explanation of modifications required for your programme there

## Notice

This has only ever been tested on windwos 11 (although I don't see why other versions of windows shouldn't work), and runnign quartus 18.1 Lite. I imagine most of this should work on different versions of quartus but haven't tried it yet.

The general concepts should be transferable to linux alhtough most of the scripts would need to be re-written, in future I might update this to include a linux version, but for the moment it'll be windows only.