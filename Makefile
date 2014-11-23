
default: clean
	gcc -o ctype.so -shared -fPIC *.c
	python demo.py

clean:
	rm -rf *.o
