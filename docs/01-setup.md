# Django

## 1/ Setup

---

### 1.1 Virtual Environments

A virtual environment allows to create a virtual installation of packages on the computer. They won’t conflict with already existing different version of the same packages on the computer. Useful for testing updated packages without breaking the original software/website.

### 1.2 Installing Miniconda

1. Go to [conda.io](https://conda.io/projects/conda/en/stable/user-guide/install/linux.html) to download the Miniconda installer.

2. In terminal, run

   ```bash
   bash Miniconda3-latest-Linux-x86_64.sh
   ```

3. Follow the prompts (safe to accept the defaults)
4. Add the `miniconda3/bin/` directory to PATH in `.bashrc` or equivalent.
5. Run `conda list` to check if installed correctly.

### 1.3 Creating a Virtual Environment

1. Create a new environment and install packages in it.

   This command will create a new environment named `djangoDev`

   ```bash
   conda create --name djangoEnv django
   ```

   Before creating the venv, conda will list the packages that will be installed. Check if the version is correct. For example, if you don’t have python 3 already installed, creating django environment may list python-2.x.x in the list of packages. 

   ```bash
   Proceed ([y]/n)? y
   ```

   Type “y” to proceed.

2. To configure the terminal (eg, bash, zsh, fish), type:

   ```bash
   # conda init <shell-name>
   conda init zsh
   ```

3. To activate a particular environment, run:

   ```bash
   conda activate djangoEnv
   ```

   Use `deactivate` instead to deactivate the environment

4. To see a list of environments, type:

   ```bash
   conda info --envs
   ```

   The active environment is the one with the `*` mark.