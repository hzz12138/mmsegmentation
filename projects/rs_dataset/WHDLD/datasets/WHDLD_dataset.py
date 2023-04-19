from mmseg.datasets import BaseSegDataset
from mmseg.registry import DATASETS


@DATASETS.register_module()
class WHDLDDataset(BaseSegDataset):
    """WHDLDDataset dataset.
    In segmentation map annotation for WHDLDDataset,
    ``reduce_zero_label`` is fixed to True. The ``img_suffix``
    is fixed to '.jpg' and ``seg_map_suffix`` is fixed to '.png'.
    Args:
        img_suffix (str): Suffix of images. Default: '.jpg'
        seg_map_suffix (str): Suffix of segmentation maps. Default: '.png'
        reduce_zero_label (bool): Whether to mark label zero as ignored.
            Default to False.
    """
    METAINFO = dict(classes=('background', 'artefacts'))

    def __init__(self,
                 img_suffix='.jpg',
                 seg_map_suffix='.png',
                 reduce_zero_label=True,
                 **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix,
            seg_map_suffix=seg_map_suffix,
            reduce_zero_label=reduce_zero_label,
            **kwargs)
