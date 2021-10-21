# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/home/htang2')
import kaldiark
home_dir = "/home/s1964832/speech-processing/self-supervised"

with open('/home/htang2/kaldi/librispeech/fbank/raw_fbank_train_clean_360.1.ark', 'rb') as f:
    f.seek(16)
    mat = kaldiark.parse_feat_mat(f)
    print(mat.shape)

with open(home_dir+'test_shape.txt', 'w', encoding='utf-8') as f:
    f.write(str(mat.shape))