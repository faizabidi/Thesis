#include <iostream>
#include <random>

std::string printRandom(){
	int max = 844;
	int min = -500;
	std::string ans;
	for(int i = 0; i < 1000; i++){
		int range = max - min + 1;
		int x = rand() % range + min;
		int y = rand() % range + min;
		std::cout << "##############################\n";
		std::cout << "mouse.position = (872, 544)\n";
		std::cout << "mouse.press(Button.left)\n";
		std::cout << "mouse.move(" << x << " , " << y << ")\n";
		std::cout << "mouse.release(Button.left)\n";
		std::cout << "time.sleep(1)\n";
	}
}
int main(){
	printRandom();
	return 0;
}