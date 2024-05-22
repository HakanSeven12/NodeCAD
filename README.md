![patreon-banner](https://github.com/HakanSeven12/NodeCAD/assets/3831435/0f2c1c7a-4f03-45a4-9cc7-481d9cf3f389)


https://www.patreon.com/HakanSeven12


 NodeCAD

NodeCAD is an easy-to-use, open-source CAD software that allows users to create and edit 2D and 3D models.


![Ekran Görüntüsü - 2024-05-21 23-19-40](https://github.com/HakanSeven12/NodeCAD/assets/3831435/c2352d06-354b-4310-9dd7-a1b31249171a)

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
