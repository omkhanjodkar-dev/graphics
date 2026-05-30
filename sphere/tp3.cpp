#include <cmath>
#include <SDL2/SDL.h>
#include <iostream>
using namespace std;


class Sphere {
	public:
		float r;
		float x;
		float y;
		float vx;
		float vy;
		float g;
		int cc;
		int common_color;
		int max_col;
		float e;
		Sphere(float r, float x, float y, float vx, float vy, float g, int cc, int common_color, int max_col, float e) : r(r), x(x), y(y), vx(vx), vy(vy), g(g), cc(cc), common_color(common_color), max_col(max_col), e(e) {}

		void calc(int diff, int width, int height) {
			vy = vy+g*diff;		

			x += vx*diff;
			y += vy*diff;
			
	
			if (x >= width-r) {
				vx=-e*vx;
				x = width-r-1;
			}
			if (x <= r) {
				vx=-e*vx;
				x = r+1;
			}
			if (y >= height-r) {
				vy = -e*vy;
				y = height-r-1;
			}
			if (y <= r) {
				vy = -e*vy;
				y = r+1;
			}
		}

		void disp(int width, int height, SDL_Renderer* renderer) {
			for (int i = 0; i < width; i++) {
				for (int j = 0; j < height; j++) {
					if ((i-x)*(i-x)+(j-y)*(j-y) <= r*r) {
						cc = sqrt(r*r-((i-x)*(i-x)+(j-y)*(j-y)));
						common_color = cc*255/max_col;
						if (max_col < cc) {
							max_col = cc;
						}
						SDL_SetRenderDrawColor(renderer, common_color, common_color, common_color/2, 255);
						SDL_RenderDrawPoint(renderer, i, j);
					}
				}
			}
		}
};

int main(int argc, char* argv[]) {
	// init sdl
	if (SDL_Init(SDL_INIT_VIDEO) < 0) {
		cerr << "SDL could not initialize! SDL_Error: " << SDL_GetError() << endl;
		return -1;
	}

	// create window
	SDL_Window* window = SDL_CreateWindow("C++ Pixel Drawing", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, 1366, 768, SDL_WINDOW_SHOWN);

	// create renderer (manages the back buffer)
	SDL_Renderer* renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
	
	bool running = true;
	SDL_Event event;

	int width = 1366;
	int height = 768;
	int common_color = 0;
	int cc = 0;

	int numberSphere = 3;

	Sphere** sphere = new Sphere*[numberSphere];
	for (int i = 0; i < numberSphere; i++) {
		sphere[i] = new Sphere(50, 200+i*100, 200+i*100, 5+i*3, 10-i*5, 0.01, 0, 0, 1, 0.9);
	}

	int max_col = 1;

	int prev_tick = SDL_GetTicks();
	int curr = prev_tick;
	int diff = 0;

	// game loop
	while (running) {
		// calculations
		curr = SDL_GetTicks();
		diff = (curr - prev_tick)/5;
		
		for (int i = 0; i < numberSphere; i++) {
			sphere[i]->calc(diff, width, height);
		}

		for (int i = 0; i < numberSphere; i++) {
			for (int j = i+1; j < numberSphere; j++) {
				if (sqrt((sphere[j]->x-sphere[i]->x)*(sphere[j]->x-sphere[i]->x)+(sphere[j]->y-sphere[i]->y)*(sphere[j]->y-sphere[i]->y)) <= sphere[i]->r+sphere[j]->r) {
					int temp=sphere[j]->vx;
					sphere[j]->vx = sphere[i]->vx;
					sphere[i]->vx = temp;
					
					temp = sphere[j]->vy;
					sphere[j]->vy = sphere[i]->vy;
					sphere[i]->vy = temp;
				}
			}
		}

		prev_tick = SDL_GetTicks();

		// check events
		while (SDL_PollEvent(&event)) {
			if (event.type == SDL_QUIT) {
				running = false;
			}
		}

		// clear
		SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
		SDL_RenderClear(renderer);

		// set pixel
		SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
		for (int i = 0; i < numberSphere; i++) {
			sphere[i]->disp(width, height, renderer);
		}

		// flipping
		SDL_RenderPresent(renderer);
	}

	// clean memory
	SDL_DestroyRenderer(renderer);
	SDL_DestroyWindow(window);
	SDL_Quit();

	return 0;
}
