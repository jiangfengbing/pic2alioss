BIN=Pic2AliOSS.alfredworkflow

$(BIN): src/info.plist
	@cd src && zip -r ../$(BIN) . && cd ..

all: clean $(BIN)


clean:
	@rm -f *.o
