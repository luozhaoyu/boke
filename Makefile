
default: clean
	gcc -o ctype.so -shared -fPIC *.c
	g++ -std=c++0x -o divide *.cpp
	g++ -std=c++0x -o cpp.so -shared -fPIC *.cpp
	python demo.py

clean:
	rm -f *.o
	rm -f *.so
