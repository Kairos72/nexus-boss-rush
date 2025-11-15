# Unity Setup Guide for Nexus: Boss Rush

## Step 1: Create Unity Project

1. **Open Unity Hub**
   - Download from https://unity3d.com/get-unity/download if not installed
   - Sign in with your Unity account

2. **Install Unity 2022 LTS**
   - Go to "Installs" tab in Unity Hub
   - Click "Install Editor"
   - Select "Unity 2022.3.x" (latest LTS)
   - Include these modules:
     - Android Build Support
     - iOS Build Support (if on Mac)
     - Windows Build Support (IL2CPP)

3. **Create New Project**
   - Go to "Projects" tab
   - Click "New project"
   - Select "3D (Core)" template
   - Project name: `Nexus`
   - Location: `C:\Users\Al\Desktop\Nexus\src`
   - Click "Create project"

## Step 2: Configure Project Settings

Once Unity opens:

1. **Project Settings**
   - Edit → Project Settings

2. **Player Settings**
   - Go to Player tab
   - Under Company Name: `Nexus Games`
   - Under Product Name: `Nexus Boss Rush`

3. **Mobile Settings**
   - Resolution and Presentation:
     - Default Orientation: Landscape Left
     - Allowed Orientations: Landscape Left, Landscape Right

4. **Quality Settings**
   - Set default quality for mobile
   - Disable VSync for initial testing

## Step 3: Create Initial Folder Structure

In Unity's Assets folder:
```
Assets/
├── Scripts/
├── Scenes/
├── Materials/
├── Prefabs/
├── Animations/
└── UI/
```

## Step 4: Test Build

1. **Build Settings**
   - File → Build Settings
   - Select Android platform
   - Switch Platform

2. **Player Settings**
   - Set minimum API level: Android 7.0 (API level 24)
   - Target API level: Latest

## Step 5: Save Scene

1. Create simple test scene
2. File → Save As
3. Save as: `Assets/Scenes/MainScene.unity`

## After Setup

Once Unity is set up, return to continue with:
1. Character controller setup
2. Mobile input implementation
3. Basic combat system

---

*Completed: Tell me when Unity project is created!*