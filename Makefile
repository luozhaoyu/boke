
default: clean
	gcc -I ~/install/Python-2.7.8 -I ~/install/Python-2.7.8/Include/ -I ~/local/anaconda/lib/python2.7/site-packages/numpy/core/include/numpy/ -o ctype.so -shared -fPIC *.c
	g++ -std=c++0x -o divide *.cpp
	g++ -std=c++0x -o cpp.so -shared -fPIC *.cpp
	python demo.py

clean:
	rm -f *.o
	rm -f *.so
