// A Multiplayer PK Game | 2.5D Game | Single World Map | 3 Bosses

#include "raylib.h"
#include "rlgl.h"
#include "raymath.h"
#include <iostream>
// #include <cmath>
using namespace std;

float GetFloorHeight(Vector3 position, Mesh collisionMesh, Matrix transform) {
    Ray ray = {0};
    ray.position = {position.x, position.y+1.0f, position.z};
    ray.direction = {0, -1, 0};

    RayCollision hit = GetRayCollisionMesh(ray, collisionMesh, transform);

    if (hit.hit) {
        // if (hit.normal.y >= 0.707f) {
            return hit.point.y;
        // }
    }

    return position.y-1000.0f;
}

Vector3 GetHorizontalCollisionPosition(Vector3 position, float radius, Mesh collisionMesh, Matrix transform) {
    Vector3 directions[] = {{-1, 0, 0}, {1, 0, 0}, {0, 0, -1}, {0, 0, 1}};

    for (int i = 0; i < 4; i++) {
        Ray ray = {0};
        ray.position = position;
        ray.direction = directions[i];
        RayCollision hit = GetRayCollisionMesh(ray, collisionMesh, transform);

        if (hit.hit and hit.distance < radius) {
            if (hit.normal.y < 0.3f) {
                float overlap = hit.distance - radius;
                position = Vector3Add(position, Vector3Scale(directions[i], overlap));
            }
        }
    }

    return position;
}

int main() {
    cout << "Hello World!";

    int const screenWidth = 1000;
    int const screenHeight = 500;

    InitWindow(screenWidth, screenHeight, "Game");

    // Sphere
    float radius = 5.0f;
    Vector3 centerPos = {-3.0f, radius+20.0f, -3.0f};
    Vector3 centerVel = {0.0f, 0.0f, 0.0f};
    Vector3 centerAcc = {0.0f, -9.8f, 0.0f};
    // float e = 0.7;
    // float neglectingVel = 1.18f;

    // Plane
    Vector3 planeCenterPos = {0.0f, 0.0f, 0.0f};
    Vector2 planeSize = {200.0f, 200.0f};
    // Mesh floorMesh = GenMeshPlane(planeSize.x, planeSize.y, 1, 1);
    // Model floorModel = LoadModelFromMesh(floorMesh);
    // Model floorModel = LoadModel("assets/basicArena.glb");
    Model floorModel = LoadModel("assets/basicArena1.glb");
    // Model floorModel = LoadModel("assets/minecraftArena.glb");
    Mesh floorMesh = floorModel.meshes[0];
    Matrix floorTransform = MatrixTranslate(0, 0, 0);

    Camera3D camera = {0};
    camera.position = {0.0f, 10.0f, 0.0f};
    camera.target = centerPos;
    camera.up = {0.0f, 1.0f, 0.0f};
    camera.fovy = 45.0f;
    camera.projection = CAMERA_PERSPECTIVE;

    SetTargetFPS(120);

    // UpdateCamera(&camera, CAMERA_FREE);

    while (!WindowShouldClose()) {
        // CALCULATIONS
        float dt = GetFrameTime();

        for (int index = 0; index < 3; index++) {
            centerPos = Vector3Add(centerPos, Vector3Scale(centerVel, dt));
        }

        for (int index = 0; index < 3; index++) {
            centerVel = Vector3Add(centerVel, Vector3Scale(centerAcc, dt));
        }

        float new_y = GetFloorHeight(centerPos, floorMesh, floorTransform) + radius;
        // cout << new_y << endl;
        if (new_y > centerPos.y) {
            // centerVel.y = (-1) * e * centerVel.y;
            // if ((centerVel.y > 0 and centerVel.y < neglectingVel) or (centerVel.y < 0 and centerVel.y > (-1) * neglectingVel)) {
            //     centerVel.y = 0;
            // }
            centerVel.y = 0;
            // centerPos = Vector3Lerp(centerPos, {centerPos.x, new_y, centerPos.z}, dt);
            centerPos.y = new_y;
        }

        centerPos = GetHorizontalCollisionPosition(centerPos, radius, floorMesh, floorTransform);

        float playerVelocityCapability = 360.0f*3.0f;
        if (IsKeyPressed(KEY_SPACE) and new_y >= centerPos.y-1.0f) {
            centerVel.y = 15.0f;
        }
        if (IsKeyDown(KEY_W)) {
            centerVel.x = -playerVelocityCapability*dt;
        }
        if (IsKeyDown(KEY_A)) {
            centerVel.z = playerVelocityCapability*dt;
        }
        if (IsKeyDown(KEY_S)) {
            centerVel.x = playerVelocityCapability*dt;
        }
        if (IsKeyDown(KEY_D)) {
            centerVel.z = -playerVelocityCapability*dt;
        }
        centerAcc.x = (-1) * centerVel.x * 2;
        centerAcc.z = (-1) * centerVel.z * 2;
        if (sqrtf(centerVel.x * centerVel.x + centerVel.z * centerVel.z) > playerVelocityCapability*dt) {
            // centerVel.x = playerVelocityCapability*dt*centerVel.x/sqrtf(centerVel.x * centerVel.x+centerVel.z * centerVel.z);
            // centerVel.z = playerVelocityCapability*dt*centerVel.z/sqrtf(centerVel.x * centerVel.x+centerVel.z * centerVel.z);
            centerVel.x = centerVel.x/sqrtf(2);
            centerVel.z = centerVel.z/sqrtf(2);
        } else if (sqrtf(centerVel.x * centerVel.x + centerVel.z * centerVel.z) < 0.1f) {
            centerVel.x = 0.0f;
            centerVel.z = 0.0f;
        }
        // cout << sqrtf(centerVel.x * centerVel.x + centerVel.z * centerVel.z) << endl;

        camera.target = centerPos;
        camera.position = {centerPos.x + 20.0f, centerPos.y + 20.0f, centerPos.z + 20.0f};

        // DRAWING
        BeginDrawing();
            ClearBackground(RAYWHITE);
            // DrawText("GAME STARTS NOW!", 220, 230, 10, BLACK);
            BeginMode3D(camera);
                // rlDisableBackfaceCulling();
                DrawSphere(centerPos, radius, LIGHTGRAY);
                DrawSphereWires(centerPos, radius, 10, 10, BLACK);
                // DrawPlane(planeCenterPos, planeSize, BLACK);
                DrawModel(floorModel, planeCenterPos, 1.0f, GRAY);
                // rlEnableBackfaceCulling();
            EndMode3D();
        EndDrawing();

        // cout << centerPos.x << " " << centerPos.y << " " << centerPos.z << endl;
    }

    CloseWindow();

    return 0;
}