#include "raylib.h"
#include "rlgl.h"
#include "raymath.h"
#include <iostream>
#include <cmath>

using namespace std;


int main() {
	cout << "Hello World!" << endl;

	int const width = 500;
	int const height = 500;

	InitWindow(width, height, "Cube");

	SetTargetFPS(120);

	float radius = 10.0f;
	float d = 1.0f;

	Vector3 c[27];

	int right[9];

	float angles[27];

	int counter = 0;
	for (float x = -10.0f-d; x <= 10.0f+d; x+=10.0f+d) {
		for (float y = -10.0f-d; y <= 10.0f+d; y+= 10.0f+d) {
			for (float z = -10.0f-d; z <= 10.0f+d; z+= 10.0f+d) {
				c[counter] = {x, y, z};
				counter += 1;
			}
		}
	}

	counter = 0;
	for (int i = 0; i < sizeof(c)/sizeof(c[0]); i++) {
		if (c[i].x == 10.0f+d) {
			right[counter] = i;
			counter++;
		}
	}

	for (int i = 0; i < sizeof(angles)/sizeof(angles[0]); i++) {
		angles[i] = atan(c[i].y/c[i].z);
	}

	Camera3D camera = {0};
    camera.position = {0.0f, 10.0f, 0.0f};
    camera.target = {0.0f, 0.0f, 0.0f};
    camera.up = {0.0f, 0.0f, 1.0f};
    camera.fovy = 45.0f;
    camera.projection = CAMERA_PERSPECTIVE;

    Vector3 cam = {c[0].x + 50.0f, c[0].y - 50.0f, c[0].z + 50.0f};

    float f = 1.0f;
    float r = 90.0f;

    float theta_rad = 0.0f;

    float theta_right = 0.0f;

	while (!WindowShouldClose()) {
		// calculations

		float dt = GetFrameTime();

		theta_rad += f*dt;

		cam.x = r*cos(theta_rad);
		cam.y = r*sin(theta_rad);
		cam.z = r*sin(cos(theta_rad));

 		camera.target = {0.0f, 0.0f, 0.0f};
        camera.position = cam;

        if (IsKeyDown(KEY_R)) {
			theta_right += f*dt;
    		for (int j = 0; j < sizeof(right)/sizeof(right[0]); j++) {
        		int pos = right[j];
    			float rad = sqrtf(pow(c[pos].y, 2)+pow(c[pos].z, 2)); // prospects for tiny errors?
        		c[pos].y = rad*cos(theta_right-angles[pos]);
    			c[pos].z = rad*sin(theta_right-angles[pos]);
        	}
        }

        int teller = 0;

		BeginDrawing();
			ClearBackground(RAYWHITE);
			BeginMode3D(camera);
				for (int i = 0; i < sizeof(c)/sizeof(c[0]); i++) {
					for (int j = 0; j < sizeof(right)/sizeof(right[0]); j++) {
						if (right[j] == i) {
							teller = 1;
						}
					}
					if (teller == 1) {
						DrawCube(c[i], radius, radius, radius, RED);
					} else {
						DrawCube(c[i], radius, radius, radius, BLUE);
					}
				}
			EndMode3D();
		EndDrawing();
	}
	CloseWindow();
	return 0;
}
