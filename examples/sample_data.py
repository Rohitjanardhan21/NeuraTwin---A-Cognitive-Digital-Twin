"""
📦 SAMPLE DATA - Populate your twin with realistic decisions
"""

import sys
sys.path.append('..')

from twin import CognitiveTwin
from datetime import datetime, timedelta
import random


def populate_sample_data():
    """Populate twin with sample decisions for demo"""
    twin = CognitiveTwin()
    
    # Sample decisions spanning different areas
    decisions = [
        {
            "decision": "Chose PyTorch over TensorFlow for research project",
            "reason": "More flexible API, better for experimentation, stronger research community",
            "alternatives": ["TensorFlow", "JAX", "MXNet"],
            "constraints": {"learning_curve": "moderate", "team_size": "small"},
            "outcome": "success",
            "tags": ["deep-learning", "framework", "research"]
        },
        {
            "decision": "Implemented custom attention mechanism instead of standard",
            "reason": "Standard attention was too memory-intensive for our use case",
            "alternatives": ["Standard attention", "Linear attention"],
            "constraints": {"gpu_memory": "8GB", "inference_time": "real-time"},
            "outcome": "success",
            "tags": ["deep-learning", "optimization", "architecture"]
        },
        {
            "decision": "Used Restormer for image restoration task",
            "reason": "Better SSIM scores and memory efficiency compared to alternatives",
            "alternatives": ["SwinIR", "NAFNet", "Custom CNN"],
            "constraints": {"gpu_memory": "4GB", "quality": "high"},
            "outcome": "success",
            "tags": ["computer-vision", "image-processing", "model-selection"]
        },
        {
            "decision": "Switched from Jupyter notebooks to Python scripts",
            "reason": "Better version control, easier collaboration, more reproducible",
            "alternatives": ["Keep Jupyter", "Use both"],
            "constraints": {"team_workflow": "git-based"},
            "outcome": "success",
            "tags": ["workflow", "tooling", "collaboration"]
        },
        {
            "decision": "Implemented early stopping instead of fixed epochs",
            "reason": "Prevents overfitting and saves training time",
            "alternatives": ["Fixed epochs", "Learning rate scheduling"],
            "constraints": {"training_time": "limited"},
            "outcome": "success",
            "tags": ["training", "optimization", "efficiency"]
        },
        {
            "decision": "Used mixed precision training",
            "reason": "2x speedup with minimal accuracy loss",
            "alternatives": ["Full precision", "Quantization"],
            "constraints": {"gpu": "RTX 3090", "speed": "critical"},
            "outcome": "success",
            "tags": ["optimization", "performance", "training"]
        },
        {
            "decision": "Chose to fine-tune pretrained model instead of training from scratch",
            "reason": "Limited data and compute budget",
            "alternatives": ["Train from scratch", "Few-shot learning"],
            "constraints": {"data": "5000 samples", "compute": "limited"},
            "outcome": "success",
            "tags": ["transfer-learning", "efficiency", "pragmatic"]
        },
        {
            "decision": "Implemented custom data augmentation pipeline",
            "reason": "Standard augmentations weren't diverse enough for our domain",
            "alternatives": ["Standard augmentations", "AutoAugment"],
            "constraints": {"time": "1 week", "complexity": "moderate"},
            "outcome": "success",
            "tags": ["data-engineering", "preprocessing", "custom-solution"]
        },
        {
            "decision": "Used Docker for deployment instead of bare metal",
            "reason": "Easier reproducibility and deployment across environments",
            "alternatives": ["Bare metal", "Virtual machines"],
            "constraints": {"deployment_complexity": "moderate"},
            "outcome": "success",
            "tags": ["deployment", "infrastructure", "devops"]
        },
        {
            "decision": "Chose to optimize for inference speed over model size",
            "reason": "Real-time requirements more critical than storage",
            "alternatives": ["Optimize for size", "Balance both"],
            "constraints": {"latency": "<100ms", "storage": "flexible"},
            "outcome": "success",
            "tags": ["optimization", "tradeoffs", "performance"]
        },
        {
            "decision": "Implemented gradient accumulation for larger batch sizes",
            "reason": "GPU memory limited but needed larger effective batch size",
            "alternatives": ["Smaller batches", "Distributed training"],
            "constraints": {"gpu_memory": "8GB", "batch_size": "target 64"},
            "outcome": "success",
            "tags": ["training", "optimization", "memory-management"]
        },
        {
            "decision": "Used WandB for experiment tracking instead of TensorBoard",
            "reason": "Better collaboration features and cloud sync",
            "alternatives": ["TensorBoard", "MLflow"],
            "constraints": {"team_size": "3", "remote_work": "yes"},
            "outcome": "success",
            "tags": ["tooling", "mlops", "collaboration"]
        }
    ]
    
    # Add decisions with timestamps spread over time
    base_date = datetime.now() - timedelta(days=180)
    
    for i, dec in enumerate(decisions):
        # Spread decisions over 6 months
        days_offset = (180 / len(decisions)) * i
        
        twin.add_decision(
            decision=dec["decision"],
            reason=dec["reason"],
            alternatives=dec.get("alternatives", []),
            constraints=dec.get("constraints", {}),
            outcome=dec.get("outcome"),
            tags=dec.get("tags", [])
        )
    
    print(f"✓ Added {len(decisions)} sample decisions")
    print("\nYour cognitive twin is now populated with realistic data!")
    print("\nTry these commands:")
    print("  twin.show_stats()")
    print("  twin.detect_biases()")
    print("  twin.predict_future()")
    
    return twin


if __name__ == "__main__":
    twin = populate_sample_data()
    twin.show_stats()
