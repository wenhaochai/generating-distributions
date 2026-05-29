"""gpic_eval — image generation evaluation metrics.

Provides FID, IS, Precision, Recall (TF Inception), and FD-DINOv2
(PyTorch) from NPZ batches.
"""

import warnings

# Suppress noisy warnings from third-party code; keep gpic_eval's own.
# Python checks filters most-recent-first, so "default" for gpic_eval must
# come AFTER the blanket "ignore" to take priority.
warnings.filterwarnings("ignore")
warnings.filterwarnings("default", module=r"gpic_eval\..*")



from .models import ALL_METRICS, DEFAULT_MODELS, FDStatistics, SUPPORTED_MODELS
from .utils import (
    ImageArrayDataset,
    ImagePathDataset,
    make_dataset,
    append_array_to_npz,
    collate_uint8,
    fd_stats_from_features,
    get_npz_keys,
    resize,
    save_or_append_npz,
    save_statistics,
)
from .metrics import compute_FD_with_stats, compute_mmd, compute_prdc, compute_statistics
from .eval import EvalResult, eval_from_embeddings, eval_with_ref_stats
from .backends import build_dinov2

__all__ = [
    # statistics
    "FDStatistics",
    "compute_statistics",
    "save_statistics",
    # metrics
    "compute_FD_with_stats",
    "compute_mmd",
    "compute_prdc",
    # utils
    "append_array_to_npz",
    "collate_uint8",
    "fd_stats_from_features",
    "get_npz_keys",
    "ImageArrayDataset",
    "ImagePathDataset",
    "resize",
    "save_or_append_npz",
    # models
    "ALL_METRICS",
    "DEFAULT_MODELS",
    "SUPPORTED_MODELS",
    # eval
    "EvalResult",
    "eval_from_embeddings",
    "eval_with_ref_stats",
    # backends
    "build_dinov2",
    # Inception: from gpic_eval.backends.inception import Evaluator
]
