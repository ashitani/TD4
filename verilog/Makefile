TARGET = test_TD4
LIBRARY = ${HOME}/git/ice-chips-verilog/Source-7400/
SRC = ${LIBRARY}/tbhelper.v ${TARGET}.v TD4.v TD4_core.v TD4_rom.v
DUMPFILE = ${TARGET}.vcd

all: ${TARGET} ${DUMPFILE}

${TARGET}: ${SRC}
	iverilog -g2012 -o ${TARGET} -s ${TARGET} -I ${LIBRARY} ${SRC}

${DUMPFILE}: ${TARGET}
	./${TARGET}

.PHONY: clean wave

clean:
	rm -rf ${DUMPFILE} ${TARGET}

wave:
	open ${DUMPFILE}