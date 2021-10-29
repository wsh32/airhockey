# Hardware

There are two PCBs we will design for this project. The first is a breakout
board for the [break beam
sensors](https://www.ttelectronics.com/TTElectronics/media/ProductFiles/Datasheets/OPB355-360to390-860to890.pdf). 
The second is an Arduino Mega shield that contains all of the required
circuitry.

### Setup

In KiCad, all the libraries are specified as project specific libraries. To use
this, you must first set up the git submodule for kicad-common.

```bash
git submodule init
git submodule update
```

Then, in KiCad, the `AIRHOCKEY_DIR` path must be configured. This should point
to the top level of the repository. For example, on my computer, it is
`/home/wsh32/git/airhockey`.
