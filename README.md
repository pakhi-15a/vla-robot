# VLA Robot: Vision-Language-Action for Natural Language Manipulation

Build a robotic system that understands natural language commands and performs object manipulation in simulation. This repo contains a PyBullet-based prototype with a modular pipeline for perception, language parsing, planning, and control.

## Problem Statement (Summary)
Develop a robotic system capable of understanding and executing object manipulation tasks from natural language commands (e.g., "Move the blue block to the right of the green cube"). The system integrates perception, language understanding, and action execution, and is evaluated against VLA benchmarks.

## Current Capabilities
- Natural language parsing for spatial relations and actions
- PyBullet simulation with a table, robot arm, cubes, spheres, and cylinders
- Pick-and-place, drop, and throw behaviors
- Modular code structure for perception, language, planning, and control

Supported actions and examples:
- Move: "move the blue cube to the right of the green cube"
- Drop: "drop the red sphere"
- Throw: "throw the yellow cylinder"

Supported relations:
`left`, `right`, `in front of`, `behind`, `above`, `below`, `near`, `far`, `on top of`

## Project Structure
```
vla-robot/
├── main.py
├── simulation/
│   └── env.py
├── perception/
│   └── detect.py
├── language/
│   ├── parser.py
│   └── speechinput.py
├── planning/
│   └── planner.py
├── control/
│   └── robot.py
└── utils/
```

## Setup (Windows PowerShell)
Create and activate a virtual environment, then install dependencies.

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install pybullet speechrecognition
```

Optional (voice input on Windows):
- Install PyAudio if you want microphone input. This can be tricky on Windows; if it fails, you can rely on typed input.

```powershell
pip install pyaudio
```

## Run
```powershell
python main.py
```

When prompted, speak or type a command.

## How It Works
- **Simulation**: [simulation/env.py](simulation/env.py) builds the PyBullet scene (table, robot, objects).
- **Perception**: [perception/detect.py](perception/detect.py) reads object positions from PyBullet.
- **Language**: [language/parser.py](language/parser.py) extracts action, objects, and relations.
- **Planning**: [planning/planner.py](planning/planner.py) computes target positions from relations.
- **Control**: [control/robot.py](control/robot.py) moves the robot end effector with IK and performs pick/place, drop, or throw.

## Deliverables (From the Problem Statement)
- **Code Repository**: Python/PyTorch implementation (this repo)
- **Demo Video**: 5+ distinct natural language commands in simulation
- **Final Report**: Methodology, challenges, and performance improvements

## Expected Capabilities
- Natural language command interpretation with object attributes and relations
- Multi-object manipulation
- Generalization to unseen tasks and objects

## Target KPIs & Benchmarks
| Metric | Target | Benchmark |
| --- | --- | --- |
| Task Success Rate (TSR) | 80-85% | 70-75% (RT-1-X or Octo) |
| Goal Condition Accuracy (GCA) | 90% | 80-85% |
| Command Interpretation Accuracy | 85% | 75-80% (CLIPort) |
| Task Completion Rate (TCR) | 80% | 65-70% |
| Error Analysis Coverage | 100% | N/A |

## Suggested Models and Datasets (Roadmap)
**Models**
- OpenVLA (7B) for VLA policy learning
- Detectron2 for detection and segmentation
- Hugging Face Transformers (BERT/GPT) or Llama 2 for language grounding

**Datasets**
- Open X-Embodiment
- COCO
- Something-Something V2
- RoboNet
- ALFRED
- VLA-3D
- LIBERO

**Simulation / Execution Tools**
- PyBullet (current)
- ROS (future integration)
- SigLIP + DinoV2 (visual backbones in OpenVLA)

## Notes
- Current parsing is rule-based; replace with a learned model for robustness.
- Pick-and-place uses simple IK with a fixed constraint; grasping is not fully physical yet.
- Table height is set by a constant; adjust `table_top_z` in [simulation/env.py](simulation/env.py) if needed.

## Next Steps (Suggested)
- Integrate a learned detector (Detectron2/OpenVLA)
- Replace rule-based parsing with a transformer model
- Add evaluation harness for KPIs and benchmarks
