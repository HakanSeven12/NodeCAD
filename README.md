# NodeCAD

NodeCAD is an easy-to-use, open-source CAD software that allows users to create and edit 2D and 3D models.


![example1](https://github.com/HakanSeven12/NodeCAD/blob/main/screenshots/example1.png)

![example2](https://github.com/HakanSeven12/NodeCAD/blob/main/screenshots/example2.png)

## Underlying Technologies

- **[PythonOCC-Core](https://github.com/tpaviot/pythonocc-core):** A powerful geometry kernel for 3D CAD applications. An API for Python created by [Thomas Paviot](https://github.com/tpaviot).
- **[Ryven](https://github.com/leon-thomm/Ryven):** A node editor written in Python by [Leon Thomm](https://github.com/leon-thomm), enabling visual programming.
- **[PythonOCC Nodes for Ryven](https://github.com/Tanneguydv/Pythonocc-nodes-for-Ryven):** NodeCAD nodes based on PythonOCC, written by [Tanneguy](https://github.com/Tanneguydv).

These technologies form the foundation of our project, providing robust tools for geometry processing and visual programming.

## Features

- **User-Friendly Interface**: A simple node based user interface that anyone can use.
- **Cross-Platform Support**: Runs on Windows, macOS, and Linux.
- **Node Package Support**: Allows users to add node packages to enhance functionality.
- **Flow Save**: Allows users to save flow.

## Installation

### Prerequisites

To run NodeCAD, you need the following software installed on your system:

- Miniconda: https://docs.anaconda.com/free/miniconda/

### Step-by-Step Installation

1. Clone the NodeCAD repository:
```
git clone https://github.com/HakanSeven12/NodeCAD.git
cd NodeCAD
```

2. Create Conda environment:
```
conda create --name=nodecadenv python=3.10
conda activate nodecadenv
```

3. Install the required dependencies:
```
conda install -c conda-forge pythonocc-core=7.7.2 ryven=3.4.3
pip install git+https://github.com/tpaviot/pythonocc-utils.git
pip install pyqtribbon
```

4. Add PythonOCC Nodes:

After the installation, you need to add this nodes: https://github.com/HakanSeven12/PythonOCC-Nodes-for-NodeCAD

4. Run NodeCAD:
```
python main.py
```

## Contributing

NodeCAD is an open-source project, and we welcome contributions.

## License

NodeCAD is licensed under the GPL v3.0 License. For more information, see the `LICENSE` file.

## Contact

For questions or feedback, please contact us:

- Email: [hakanseven12@gmail.com](mailto:email@example.com)
- Help: [NodeCAD Issues](https://github.com/HakanSeven12/NodeCAD/issues)

## Thanks

Thank you to all the developers and users who have contributed to the NodeCAD project.
