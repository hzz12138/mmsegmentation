_base_ = [
    'mmseg::_base_/models/fcn_unet_s5-d16.py', './WHDLD_256×256.py',
    'mmseg::_base_/default_runtime.py', 'mmseg::_base_/schedules/schedule_20k.py'
]
custom_imports = dict(imports='datasets.WHDLDDataset')
crop_size = (256, 256)
data_preprocessor = dict(size=crop_size)
model = dict(
    data_preprocessor=data_preprocessor,
    decode_head=dict(num_classes=2),
    auxiliary_head=None,
    test_cfg=dict(mode='whole', _delete_=True))
