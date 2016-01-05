
CC=gcc
CFLAGS=-Wall

OUT_DIR=bin

all: directories $(OUT_DIR)/p100

directories:
	mkdir -p $(OUT_DIR)

$(OUT_DIR)/p100: p100.c
	$(CC) $(CFLAGS) -o $(OUT_DIR)/p100 p100.c

run100: $(OUT_DIR)/p100
	$(OUT_DIR)/p100

clean:
	rm $(OUT_DIR)/*
