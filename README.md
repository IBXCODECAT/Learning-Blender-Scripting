# Blender Python Learning Repository  

## About  

This repository is a personal learning resource for exploring Blender Python scripting. It is **not maintained** and does **not accept issues or pull requests**. The scripts and resources here are for educational purposes and experimentation only.  

This repository tracks my progress and experiments in learning Blender scripting with Python. It’s a collection of scripts, examples, and notes designed to help explore Blender’s Python API and understand how to automate tasks, create tools, or extend Blender’s functionality.  

You can clone this repository to test the scripts and experiment with Blender Python scripting as part of your own learning journey.  

---

## Setting Up  

Follow these steps to get started:  

### Step 1: Clone This Repository  

1. Install Git on your system if you haven’t already: [Download Git](https://git-scm.com/).  
2. Open a terminal and run the following commands:  
   ```bash
   git clone https://github.com/your-username/blender-python-learning.git
   cd blender-python-learning
   ```  

### Step 2: Install Blender  

Download and install Blender from [blender.org](https://www.blender.org/). Once installed, you’ll use Blender’s **Scripting** workspace to load and run the scripts from this repository.  

### Step 3: Running Blender Scripts  

1. Open Blender and switch to the **Scripting** workspace.  
2. Load a script from this repository using Blender’s text editor:
   - Click **Open** and navigate to the script you want to test.  
3. Press the **Run Script** button in Blender.  

---

## Optional: Enhancing Development Workflows with an External Editor!  

While not required, using an external text editor and version control can make Blender scripting more efficient and enjoyable.  

### Benefits of Using an External Text Editor  

Blender has a built-in scripting editor, but external editors like Visual Studio Code provide:  
- **Autocompletion:** Suggests API functions and parameters as you type.  
- **Version Control:** Track changes, manage different script versions, and revert easily.  
- **Debugging and Search Tools:** Helps troubleshoot and explore large scripts.  
- **AI Assistance:** Tools like [GitHub Copilot](https://github.com/features/copilot) can speed up learning by providing code suggestions.  

### Setting Up Visual Studio Code  

1. **Download and Install:**  
   Get Visual Studio Code from [code.visualstudio.com](https://code.visualstudio.com/).  

2. **Install Python Extension:**  
   - Open VS Code and click the **Extensions** icon (or press `Ctrl+Shift+X`).  
   - Search for “Python” and install the extension by Microsoft.  

3. **Install Fake `bpy` Module:**  
   - Open a terminal in VS Code and run:  
     ```bash
     python -m pip install fake-bpy-module-latest
     ```  
   - This provides Blender API type hints for autocompletion but does not run Blender functions outside Blender.  

   ** IMPORTANT ** You will need to reference the "fake bpy" via changing your Visual Studio Code user setting `"python.autoComplete.extraPaths"` to the path of your site packages!

4. **Configure VS Code:**  
   - Select your Python interpreter in the bottom-left corner of VS Code (ensure it’s the one installed on your system, not Blender’s internal Python).  

---

## Optional: Automate Script Execution  

For repetitive testing, automate script execution with a batch file:  

1. Create a new `.bat` file and add:  
   ```batch
   blender --python path\to\your_script.py
   ```  
   Replace `path\to\your_script.py` with the full path to your Blender script.  

2. Run the batch file to execute your script in Blender automatically.  
